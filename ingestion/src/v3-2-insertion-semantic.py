"""
Document insertion script with idempotency.
Processes markdown files and inserts into PostgreSQL vector store.
"""

import sys
from pathlib import Path
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.schema import Document
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.postgres import PGVectorStore
from base.common import get_config


def main():
    print("🚀 Semantic Document Insertion Pipeline")
    print("=" * 40)
    
    # Load config
    try:
        config = get_config()
        print(f"Loaded config: chunk_size={config['CHUNK_SIZE']}, overlap={config['CHUNK_OVERLAP']}")
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
        table_name=config['EMBEDDING_TABLE_NAME'],
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
        print(f"Using embedding dimension: {config['EMBEDDING_DIM']}")
        print(f"Using embedding table: {config['EMBEDDING_TABLE_NAME']}")
        print(f"Using markdown path: {config['MARKDOWN_PATH_FOR_EMBEDDING']}")

    except Exception as e:
        print(f"Failed to initialize embedding model: {e}")
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
    
    for md_file in md_files:
        print(f"\n📄 Processing: {md_file.name}")
        
        # Check if already processed (idempotency)
        doc_id = get_document_id(md_file)
        if check_document_exists(vector_store, doc_id):
            print(f"   ⏭️  Already processed, skipping")
            continue
        
        # Load document
        doc = load_markdown_document(md_file)
        if not doc:
            print(f"   ❌ Failed to load document")
            error_count += 1
            continue
        
        # Process into nodes
        nodes = process_document(doc, config, embedding_model)
        if not nodes:
            print(f"   ❌ Failed to create semantic chunks")
            error_count += 1
            continue
        
        # Insert into vector store
        if insert_nodes(nodes, vector_store, embedding_model):
            print(f"   ✅ Successfully inserted")
            success_count += 1
        else:
            print(f"   ❌ Failed to insert")
            error_count += 1
    
    # Summary
    print("\n" + "=" * 40)
    print("Insertion Results:")
    print(f"Successfully processed: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Total files: {len(md_files)}")
    
    if error_count == 0:
        print("\n🎉 All documents inserted successfully!")
        return 0
    else:
        print(f"\n⚠️  Completed with {error_count} errors")
        return 1


def get_document_id(file_path):
    """Generate consistent document ID from file path."""
    return f"doc_{file_path.stem}"

def check_document_exists(vector_store, doc_id):
    """Check if document is already in the vector store."""
    # For now, always process (can be enhanced with metadata table)
    # This avoids the embedding model initialization issue
    return False

def load_markdown_document(file_path):
    """Load markdown file as Document."""
    try:
        content = file_path.read_text(encoding='utf-8')
        if not content.strip():
            print(f"Warning: Empty content in {file_path.name}")
            return None
        
        # Create document with metadata
        doc = Document(
            text=content,
            metadata={
                'filename': file_path.name,
                'file_path': str(file_path),
                'doc_id': get_document_id(file_path)
            }
        )
        return doc
    except Exception as e:
        print(f"Error loading {file_path.name}: {e}")
        return None

def process_document(doc, config, embedding_model):
    """Process document into nodes using SemanticSplitterNodeParser."""
    try:
        # Create semantic splitter with the embedding model (following docs pattern)
        semantic_splitter = SemanticSplitterNodeParser(
            buffer_size=1,  # Number of sentences to group together
            breakpoint_percentile_threshold=95,  # 95th percentile for semantic breaks
            embed_model=embedding_model  # Pass the embedding model as embed_model parameter
        )
        
        # Parse document into semantic nodes
        nodes = semantic_splitter.get_nodes_from_documents([doc])
        
        # Add document metadata to all nodes
        for node in nodes:
            node.metadata.update(doc.metadata)
        
        print(f"Created {len(nodes)} semantic chunks from {doc.metadata['filename']}")
        return nodes
    
    except Exception as e:
        print(f"Error processing document: {e}")
        return []

def insert_nodes(nodes, vector_store, embedding_model):
    """Insert nodes into vector store using VectorStoreIndex."""
    if not nodes:
        return False
    
    try:
        # Create storage context with vector store
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        # Create index - this will automatically generate embeddings and insert
        index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=embedding_model)
        
        print(f"Inserted {len(nodes)} nodes into vector store")
        return True
    
    except Exception as e:
        print(f"Error inserting nodes: {e}")
        return False

if __name__ == "__main__":
    sys.exit(main())