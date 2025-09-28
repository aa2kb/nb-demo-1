"""Vector storage service using LlamaIndex and PGVector."""

import logging
from typing import List, Optional, Dict, Any
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.schema import TextNode

from .config import settings
from .database import db_manager
from .document_processor import ProcessedDocument
from .embedding_service import EmbeddingService

logger = logging.getLogger(__name__)


class VectorStoreManager:
    """Manages vector storage operations."""
    
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store: Optional[PGVectorStore] = None
        self.index: Optional[VectorStoreIndex] = None
        self._initialize_vector_store()
    
    def _initialize_vector_store(self):
        """Initialize the PGVector store."""
        try:
            # Ensure database is set up
            if not db_manager.ensure_database_setup():
                raise Exception("Failed to set up database")
            
            # Create PGVector store
            self.vector_store = PGVectorStore.from_params(
                database=settings.db_name,
                host=settings.db_host,
                password=settings.db_password,
                port=settings.db_port,
                user=settings.db_user,
                table_name="document_chunks",
                embed_dim=768,  # embeddinggemma:300m actual dimension from test
            )
            
            # Create storage context
            storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
            
            # Create or load index with our embedding model
            self.index = VectorStoreIndex.from_vector_store(
                vector_store=self.vector_store,
                storage_context=storage_context,
                embed_model=self.embedding_service.embedding_model
            )
            
            logger.info("Vector store initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize vector store: {e}")
            raise
    
    def store_document(self, processed_doc: ProcessedDocument) -> bool:
        """Store a processed document in the vector store."""
        try:
            if not self.vector_store or not self.index:
                logger.error("❌ Vector store not initialized")
                return False
            
            logger.info(f"💾 Starting document storage: {processed_doc.name}")
            logger.info(f"📊 Document has {len(processed_doc.chunks)} chunks to process")
            
            # Create nodes for each chunk
            logger.info(f"🔄 Processing {len(processed_doc.chunks)} chunks for storage")
            nodes = []
            for i, chunk in enumerate(processed_doc.chunks):
                logger.debug(f"📝 Processing chunk {i+1}/{len(processed_doc.chunks)} (size: {len(chunk)} chars)")
                
                # Generate embedding for the chunk
                embedding = self.embedding_service.embed_text(chunk)
                
                if embedding is None:
                    logger.warning(f"⚠️ Failed to generate embedding for chunk {i+1}/{len(processed_doc.chunks)} of {processed_doc.name}")
                    continue
                logger.debug(f"✅ Embedding generated for chunk {i+1}/{len(processed_doc.chunks)}")
                
                # Create metadata for this chunk
                chunk_metadata = {
                    **processed_doc.metadata,
                    "document_id": processed_doc.document_id,
                    "chunk_index": i,
                    "chunk_size": len(chunk)
                }
                
                # Create text node
                node = TextNode(
                    text=chunk,
                    metadata=chunk_metadata,
                    embedding=embedding
                )
                
                nodes.append(node)
            
            if not nodes:
                logger.error(f"No valid nodes created for document: {processed_doc.name}")
                return False
            
            # Add nodes to the index
            self.index.insert_nodes(nodes)
            
            logger.info(f"Successfully stored {len(nodes)} chunks for document: {processed_doc.name}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to store document {processed_doc.name}: {e}")
            return False
    
    def store_documents(self, processed_docs: List[ProcessedDocument]) -> int:
        """Store multiple processed documents."""
        stored_count = 0
        
        for doc in processed_docs:
            if self.store_document(doc):
                stored_count += 1
        
        logger.info(f"Successfully stored {stored_count} out of {len(processed_docs)} documents")
        return stored_count
    
    def check_document_exists(self, document_id: str) -> bool:
        """Check if a document already exists in the vector store."""
        try:
            # Query the database directly to check for existing document
            engine = db_manager.get_engine()
            
            with engine.connect() as conn:
                from sqlalchemy import text
                result = conn.execute(
                    text("SELECT COUNT(*) FROM document_chunks WHERE metadata->>'document_id' = :doc_id"),
                    {"doc_id": document_id}
                )
                count = result.scalar()
                return count > 0
                
        except Exception as e:
            logger.error(f"Error checking document existence: {e}")
            return False
    
    def delete_document(self, document_id: str) -> bool:
        """Delete a document from the vector store."""
        try:
            engine = db_manager.get_engine()
            
            with engine.connect() as conn:
                from sqlalchemy import text
                result = conn.execute(
                    text("DELETE FROM document_chunks WHERE metadata->>'document_id' = :doc_id"),
                    {"doc_id": document_id}
                )
                conn.commit()
                deleted_count = result.rowcount
                
            logger.info(f"Deleted {deleted_count} chunks for document: {document_id}")
            return deleted_count > 0
            
        except Exception as e:
            logger.error(f"Error deleting document {document_id}: {e}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about stored documents."""
        try:
            engine = db_manager.get_engine()
            
            with engine.connect() as conn:
                from sqlalchemy import text
                
                # Get total chunks count
                total_chunks = conn.execute(
                    text("SELECT COUNT(*) FROM document_chunks")
                ).scalar()
                
                # Get unique documents count
                unique_docs = conn.execute(
                    text("SELECT COUNT(DISTINCT metadata->>'document_id') FROM document_chunks")
                ).scalar()
                
                # Get documents with their chunk counts
                doc_stats = conn.execute(
                    text("""
                        SELECT 
                            metadata->>'document_name' as doc_name,
                            COUNT(*) as chunk_count
                        FROM document_chunks 
                        GROUP BY metadata->>'document_name'
                        ORDER BY chunk_count DESC
                    """)
                ).fetchall()
                
            return {
                "total_chunks": total_chunks,
                "unique_documents": unique_docs,
                "document_details": [{"name": row[0], "chunks": row[1]} for row in doc_stats]
            }
            
        except Exception as e:
            logger.error(f"Error getting stats: {e}")
            return {"error": str(e)}