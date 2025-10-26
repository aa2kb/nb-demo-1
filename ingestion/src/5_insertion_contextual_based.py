"""
Contextual Document insertion script using docling.
Processes markdown files using docling's DocumentConverter and HybridChunker with contextualization,
then inserts into PostgreSQL vector store.
"""

import os
import sys
from pathlib import Path
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.schema import TextNode
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.postgres import PGVectorStore
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from dotenv import load_dotenv

def get_config():
    """Load configuration from .env file."""
    # Load .env
    env_paths = [Path("../.env"), Path(".env")]
    for env_path in env_paths:
        if env_path.exists():
            load_dotenv(env_path)
            break
    
    return {
        'DB_HOST': os.getenv('DB_HOST', 'localhost'),
        'DB_PORT': int(os.getenv('DB_PORT', 5432)),
        'DB_USER': os.getenv('DB_USER', 'admin'),
        'DB_PASSWORD': os.getenv('DB_PASSWORD', 'admin'),
        'DB_NAME': os.getenv('DB_NAME', 'postgres'),
        'VECTOR_TABLE_NAME': os.getenv('VECTOR_TABLE_NAME', 'vectors'),
        'CHUNK_SIZE': int(os.getenv('CHUNK_SIZE', 1024)),
        'CHUNK_OVERLAP': int(os.getenv('CHUNK_OVERLAP', 200)),
        'EMBEDDING_DIM': int(os.getenv('EMBEDDING_DIM', 768)),
        'EMBEDDING_MODEL': os.getenv('EMBEDDING_MODEL', 'nomic-embed-text:v1.5'),
        'MARKDOWN_PATH_FOR_EMBEDDING': os.getenv('MARKDOWN_PATH_FOR_EMBEDDING', 'markdown'),
    }


def main():
    print("🚀 Contextual Document Insertion Pipeline (Docling)")
    print("=" * 50)
    
    # Load config
    try:
        config = get_config()
        print(f"Loaded config: embedding_model={config['EMBEDDING_MODEL']}")
        print(f"Using embedding dimension: {config['EMBEDDING_DIM']}")
        print(f"Using markdown path: {config['MARKDOWN_PATH_FOR_EMBEDDING']}")
    except Exception as e:
        print(f"Failed to load config: {e}")
        return 1
    
    # Get vector store
    try:
        vector_store = PGVectorStore.from_params(
            database=config['DB_NAME'],
            host=config['DB_HOST'],
            password=config['DB_PASSWORD'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            table_name='vectors_contextual_chunks',
            embed_dim=config['EMBEDDING_DIM'],
            hybrid_search=True,
            text_search_config="english"
        )
        print("Connected to vector store")
    except Exception as e:
        print(f"Failed to connect to vector store: {e}")
        return 1
    
    # Initialize embedding model
    try:
        embedding_model = OllamaEmbedding(
            model_name=config['EMBEDDING_MODEL'],
            base_url="http://localhost:11434"
        )
        print(f"Initialized embedding model: {config['EMBEDDING_MODEL']}")
    except Exception as e:
        print(f"Failed to initialize embedding model: {e}")
        return 1
    
    # Initialize docling components
    try:
        doc_converter = DocumentConverter()
        chunker = HybridChunker()
        print("Initialized docling DocumentConverter and HybridChunker")
    except Exception as e:
        print(f"Failed to initialize docling components: {e}")
        return 1
    
    # Find markdown files
    markdown_dir = Path(f"../{config['MARKDOWN_PATH_FOR_EMBEDDING']}")
    if not markdown_dir.exists():
        markdown_dir = Path(config['MARKDOWN_PATH_FOR_EMBEDDING'])

    if not markdown_dir.exists():
        print(f"Markdown folder not found: {markdown_dir}")
        return 1
    
    md_files = list(markdown_dir.glob("*.md"))
    if not md_files:
        print("No markdown files found")
        return 1
    
    print(f"Found {len(md_files)} markdown files")
    
    # Process each file
    success_count = 0
    error_count = 0
    total_chunks_processed = 0
    
    for md_file in md_files:
        print(f"\n📄 Processing: {md_file.name}")
        
        # Check if already processed (idempotency)
        doc_id = get_document_id(md_file)
        if check_document_exists(vector_store, doc_id):
            print(f"   ⏭️  Already processed, skipping")
            continue
        
        # Convert document using docling
        try:
            print(f"   🔄 Converting document with docling...")
            doc = doc_converter.convert(source=str(md_file)).document
            print(f"   ✅ Document converted successfully")
        except Exception as e:
            print(f"   ❌ Failed to convert document: {e}")
            error_count += 1
            continue
        
        # Process with contextual chunking
        try:
            nodes = process_document_with_contextualization(doc, chunker, md_file)
            if not nodes:
                print(f"   ❌ Failed to create contextual chunks")
                error_count += 1
                continue
            
            print(f"   📊 Created {len(nodes)} contextual chunks")
            
        except Exception as e:
            print(f"   ❌ Error during contextual chunking: {e}")
            error_count += 1
            continue
        
        # Insert into vector store
        try:
            if insert_nodes(nodes, vector_store, embedding_model):
                print(f"   ✅ Successfully inserted {len(nodes)} chunks")
                success_count += 1
                total_chunks_processed += len(nodes)
            else:
                print(f"   ❌ Failed to insert chunks")
                error_count += 1
        except Exception as e:
            print(f"   ❌ Error inserting chunks: {e}")
            error_count += 1
    
    # Summary
    print("\n" + "=" * 50)
    print("Contextual Insertion Results:")
    print(f"Successfully processed files: {success_count}")
    print(f"Total contextual chunks inserted: {total_chunks_processed}")
    print(f"Errors: {error_count}")
    print(f"Total markdown files: {len(md_files)}")
    
    if error_count == 0:
        print("\n🎉 All documents processed with contextual chunking successfully!")
        return 0
    else:
        print(f"\n⚠️  Completed with {error_count} errors")
        return 1


def get_document_id(file_path):
    """Generate consistent document ID from file path."""
    return f"contextual_doc_{file_path.stem}"


def check_document_exists(vector_store, doc_id):
    """Check if document is already in the vector store."""
    # For now, always process (can be enhanced with metadata queries)
    # This avoids complex vector store queries for idempotency
    return False


def process_document_with_contextualization(doc, chunker, file_path):
    """Process document using docling's HybridChunker with contextualization."""
    try:
        nodes = []
        
        # Get chunks from docling HybridChunker
        print(f"   🔍 Chunking document...")
        chunk_iter = chunker.chunk(dl_doc=doc)
        
        chunk_count = 0
        for i, chunk in enumerate(chunk_iter):
            chunk_count += 1
            
            # Get base chunk text
            chunk_text = chunk.text
            
            # Apply contextualization
            try:
                enriched_text = chunker.contextualize(chunk=chunk)
                print(f"   📝 Chunk {i}: {len(chunk_text)} → {len(enriched_text)} chars (contextualized)")
            except Exception as e:
                print(f"   ⚠️  Contextualization failed for chunk {i}, using original: {e}")
                enriched_text = chunk_text
            
            # Create metadata
            node_metadata = {
                'filename': file_path.name,
                'file_path': str(file_path),
                'doc_id': get_document_id(file_path),
                'chunk_index': i,
                'chunk_id': f"{get_document_id(file_path)}_chunk_{i}",
                'chunking_method': 'docling_hybrid_contextual',
                'original_chunk_length': len(chunk_text),
                'enriched_chunk_length': len(enriched_text),
                'has_contextualization': len(enriched_text) != len(chunk_text)
            }
            
            # Create TextNode with enriched content
            node = TextNode(
                text=enriched_text,
                metadata=node_metadata,
                id_=node_metadata['chunk_id']
            )
            
            nodes.append(node)
        
        print(f"   ✅ Processed {chunk_count} chunks with contextual enrichment")
        return nodes
    
    except Exception as e:
        print(f"   ❌ Error processing document with contextualization: {e}")
        return []


def insert_nodes(nodes, vector_store, embedding_model):
    """Insert nodes into vector store using VectorStoreIndex."""
    if not nodes:
        return False
    
    try:
        # Create storage context with vector store
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        # Process in smaller batches for better memory management
        batch_size = 20  # Smaller batches for contextual chunks which might be larger
        total_inserted = 0
        
        for i in range(0, len(nodes), batch_size):
            batch = nodes[i:i + batch_size]
            
            try:
                # Create index - this will automatically generate embeddings and insert
                index = VectorStoreIndex(batch, storage_context=storage_context, embed_model=embedding_model)
                total_inserted += len(batch)
                print(f"   📦 Inserted batch {i//batch_size + 1}: {len(batch)} contextual nodes")
                
            except Exception as e:
                print(f"   ⚠️  Error inserting batch {i//batch_size + 1}: {e}")
                continue
        
        print(f"   ✅ Total inserted: {total_inserted}/{len(nodes)} contextual nodes")
        return total_inserted > 0
    
    except Exception as e:
        print(f"   ❌ Error inserting nodes: {e}")
        return False


if __name__ == "__main__":
    sys.exit(main())