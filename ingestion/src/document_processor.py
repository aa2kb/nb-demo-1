"""Document processing utilities using Docling."""

import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
import hashlib
from dataclasses import dataclass

from docling.document_converter import DocumentConverter
from llama_index.core.schema import Document
from llama_index.core.node_parser import SentenceSplitter

from .config import settings

logger = logging.getLogger(__name__)


@dataclass
class ProcessedDocument:
    """Represents a processed document with metadata."""
    document_id: str
    name: str
    content: str
    chunks: List[str]
    metadata: Dict[str, Any]


class DocumentProcessor:
    """Handles document processing using Docling."""
    
    def __init__(self):
        self.converter = DocumentConverter()
        self.text_splitter = SentenceSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
    
    def generate_document_id(self, file_path: Path) -> str:
        """Generate a unique document ID based on file path and content."""
        # Use file path and modification time for ID generation
        stat = file_path.stat()
        id_string = f"{file_path.name}_{stat.st_size}_{stat.st_mtime}"
        return hashlib.md5(id_string.encode()).hexdigest()
    
    def process_pdf(self, file_path: Path) -> Optional[ProcessedDocument]:
        """Process a single PDF file."""
        try:
            logger.info(f"📄 Starting PDF processing: {file_path.name}")
            logger.debug(f"Full path: {file_path}")
            
            # Convert document using docling
            logger.info(f"🔄 Converting document with Docling: {file_path.name}")
            result = self.converter.convert(str(file_path))
            
            if not result or not result.document:
                logger.error(f"❌ Failed to convert document: {file_path}")
                return None
            logger.info(f"✅ Document conversion successful: {file_path.name}")
            
            # Extract text content
            logger.info(f"📝 Extracting text content from: {file_path.name}")
            content = result.document.export_to_markdown()
            
            if not content.strip():
                logger.warning(f"⚠️ No content extracted from: {file_path}")
                return None
            logger.info(f"✅ Content extracted successfully: {len(content)} characters")
            
            # Generate document ID
            doc_id = self.generate_document_id(file_path)
            
            # Create LlamaIndex document for chunking
            llamaindex_doc = Document(
                text=content,
                metadata={
                    "file_name": file_path.name,
                    "file_path": str(file_path),
                    "document_id": doc_id
                }
            )
            
            # Split into chunks
            logger.info(f"✂️ Splitting document into chunks: {file_path.name}")
            nodes = self.text_splitter.get_nodes_from_documents([llamaindex_doc])
            chunks = [node.text for node in nodes]
            logger.info(f"✅ Document split into {len(chunks)} chunks")
            
            # Prepare metadata
            metadata = {
                "file_name": file_path.name,
                "file_path": str(file_path),
                "file_size": file_path.stat().st_size,
                "num_chunks": len(chunks),
                "processing_timestamp": str(file_path.stat().st_mtime)
            }
            
            processed_doc = ProcessedDocument(
                document_id=doc_id,
                name=file_path.name,
                content=content,
                chunks=chunks,
                metadata=metadata
            )
            
            logger.info(f"Successfully processed {file_path.name}: {len(chunks)} chunks")
            return processed_doc
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return None
    
    def process_directory(self, directory_path: Path) -> List[ProcessedDocument]:
        """Process all PDF files in a directory."""
        if not directory_path.exists() or not directory_path.is_dir():
            logger.error(f"Directory does not exist: {directory_path}")
            return []
        
        pdf_files = list(directory_path.glob("*.pdf")) + list(directory_path.glob("*.PDF"))
        
        if not pdf_files:
            logger.warning(f"No PDF files found in {directory_path}")
            return []
        
        logger.info(f"Found {len(pdf_files)} PDF files to process")
        
        processed_docs = []
        for pdf_file in pdf_files:
            processed_doc = self.process_pdf(pdf_file)
            if processed_doc:
                processed_docs.append(processed_doc)
        
        logger.info(f"Successfully processed {len(processed_docs)} out of {len(pdf_files)} documents")
        return processed_docs