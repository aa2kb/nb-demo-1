"""
Document insertion script that reads pre-chunked JSON files.
Processes chunks from JSON files and inserts into PostgreSQL vector store.
"""

import os
import sys
import json
import time
from pathlib import Path
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.schema import TextNode
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.postgres import PGVectorStore
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
        'EMBEDDING_DIM': int(os.getenv('EMBEDDING_DIM', 768)),
        'EMBEDDING_MODEL': os.getenv('EMBEDDING_MODEL', 'nomic-embed-text:v1.5'),
        'CHUNKS_PATH': os.getenv('CHUNKS_PATH', 'chunks'),
    }

def main():
    print("🚀 Chunk Insertion Pipeline")
    print("=" * 40)
    
    # Load config
    try:
        config = get_config()
        print(f"Loaded config: embedding_model={config['EMBEDDING_MODEL']}")
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
            table_name='vectors_from_chunks',
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
        print(f"Using chunks path: {config['CHUNKS_PATH']}")

    except Exception as e:
        print(f"Failed to initialize embedding model: {e}")
        return 1
    
    # Find chunk JSON files
    chunks_dir = Path(f"../{config['CHUNKS_PATH']}")
    if not chunks_dir.exists():
        chunks_dir = Path(config['CHUNKS_PATH'])

    if not chunks_dir.exists():
        print(f"Chunks folder not found: {chunks_dir}")
        return 1
    
    json_files = list(chunks_dir.glob("*_chunks.json"))
    if not json_files:
        print("No chunk JSON files found")
        return 1
    
    print(f"Found {len(json_files)} chunk files")
    
    # Process each file
    success_count = 0
    error_count = 0
    total_chunks_processed = 0
    
    for json_file in json_files:
        print(f"\n📄 Processing: {json_file.name}")
        
        # Check if already processed (idempotency)
        doc_id = get_document_id(json_file)
        if check_document_exists(vector_store, doc_id):
            print(f"   ⏭️  Already processed, skipping")
            continue
        
        # Load chunks from JSON
        chunks_data = load_chunks_from_json(json_file)
        if not chunks_data:
            print(f"   ❌ Failed to load chunks")
            error_count += 1
            continue
        
        # Convert chunks to nodes
        nodes = create_nodes_from_chunks(chunks_data, json_file)
        if not nodes:
            print(f"   ❌ Failed to create nodes")
            error_count += 1
            continue
        
        # Insert into vector store
        if insert_nodes(nodes, vector_store, embedding_model):
            print(f"   ✅ Successfully inserted {len(nodes)} chunks")
            success_count += 1
            total_chunks_processed += len(nodes)
        else:
            print(f"   ❌ Failed to insert")
            error_count += 1
    
    # Summary
    print("\n" + "=" * 40)
    print("Insertion Results:")
    print(f"Successfully processed files: {success_count}")
    print(f"Total chunks inserted: {total_chunks_processed}")
    print(f"Errors: {error_count}")
    print(f"Total files: {len(json_files)}")
    
    if error_count == 0:
        print("\n🎉 All chunks inserted successfully!")
        return 0
    else:
        print(f"\n⚠️  Completed with {error_count} errors")
        return 1

def get_document_id(file_path):
    """Generate consistent document ID from file path."""
    return f"chunks_{file_path.stem}"

def check_document_exists(vector_store, doc_id):
    """Check if document is already in the vector store."""
    # For now, always process (can be enhanced with metadata table)
    # This avoids the embedding model initialization issue
    return False

def load_chunks_from_json(file_path):
    """Load chunks data from JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'chunks' not in data:
            print(f"Warning: No 'chunks' key found in {file_path.name}")
            return None
        
        chunks = data['chunks']
        if not chunks:
            print(f"Warning: Empty chunks in {file_path.name}")
            return None
        
        print(f"Loaded {len(chunks)} chunks from {file_path.name}")
        return data
    
    except Exception as e:
        print(f"Error loading {file_path.name}: {e}")
        return None

def create_nodes_from_chunks(chunks_data, file_path):
    """Convert chunk data to TextNode objects."""
    try:
        nodes = []
        chunks = chunks_data['chunks']
        source_markdown = chunks_data.get('source_markdown', file_path.stem)
        
        for chunk in chunks:
            # Create metadata combining chunk metadata with file info
            metadata = {
                'source_file': source_markdown,
                'chunk_index': chunk['chunk_index'],
                'file_path': str(file_path),
                'chunking_method': chunks_data.get('chunking_method', 'unknown'),
                'total_chunks': chunks_data.get('total_chunks', len(chunks)),
                'created_at': chunks_data.get('created_at'),
            }
            
            # Add chunk-specific metadata if available
            if 'metadata' in chunk:
                chunk_meta = chunk['metadata']
                metadata.update({
                    'start_pos': chunk_meta.get('start_pos'),
                    'end_pos': chunk_meta.get('end_pos'),
                    'chunk_size_config': chunk_meta.get('chunk_size_config'),
                    'chunk_overlap_config': chunk_meta.get('chunk_overlap_config'),
                })
            
            # Create TextNode
            node = TextNode(
                text=chunk['content'],
                metadata=metadata,
                id_=f"{source_markdown}_chunk_{chunk['chunk_index']}"
            )
            
            nodes.append(node)
        
        print(f"Created {len(nodes)} nodes from {len(chunks)} chunks")
        return nodes
    
    except Exception as e:
        print(f"Error creating nodes: {e}")
        return []

def insert_nodes(nodes, vector_store, embedding_model):
    """Insert nodes into vector store using VectorStoreIndex one by one."""
    if not nodes:
        return False
    
    # Process one node at a time to avoid overwhelming the embedding service
    total_nodes = len(nodes)
    successful_inserts = 0
    
    try:
        # Create storage context once
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        for i, node in enumerate(nodes, 1):
            print(f"   Processing node {i}/{total_nodes}")
            
            try:
                # Create index with single node
                index = VectorStoreIndex([node], storage_context=storage_context, embed_model=embedding_model)
                successful_inserts += 1
                
                # Small delay to avoid overwhelming the service
                time.sleep(0.01)
                
                if i % 10 == 0:  # Progress update every 10 nodes
                    print(f"   ✅ Successfully inserted {successful_inserts}/{i} nodes")
                
            except Exception as node_error:
                print(f"   ❌ Error inserting node {i}: {node_error}")
                # Continue with next node instead of failing completely
                continue
        
        if successful_inserts == 0:
            return False
        
        print(f"Successfully inserted {successful_inserts}/{total_nodes} nodes")
        return True
    
    except Exception as e:
        print(f"Error in insert process: {e}")
        return False

if __name__ == "__main__":
    sys.exit(main())