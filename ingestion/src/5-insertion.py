import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
from typing import List, Dict, Any
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.core.schema import TextNode
from llama_index.core.vector_stores import VectorStoreQuery

def load_config():
    """Load configuration from .env file."""
    env_path = Path("../.env")
    if not env_path.exists():
        env_path = Path(".env")
    
    if env_path.exists():
        load_dotenv(env_path)
    
    return {
        'DB_HOST': os.getenv('DB_HOST', 'localhost'),
        'DB_PORT': int(os.getenv('DB_PORT', 5432)),
        'DB_USER': os.getenv('DB_USER', 'admin'),
        'DB_PASSWORD': os.getenv('DB_PASSWORD', 'admin'),
        'DB_NAME': os.getenv('DB_NAME', 'postgres'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO')
    }

def create_vector_store(config):
    """Create LlamaIndex PGVectorStore for document insertion."""
    try:
        # Create PGVectorStore with consistent configuration
        vector_store = PGVectorStore.from_params(
            database=config['DB_NAME'],
            host=config['DB_HOST'],
            password=config['DB_PASSWORD'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            table_name="vectors",  # Creates data_vectors table
            embed_dim=768,
            hybrid_search=False,
            text_search_config="english"
        )
        
        print("✅ Connected to LlamaIndex PGVectorStore")
        print(f"   Database: {config['DB_NAME']}@{config['DB_HOST']}:{config['DB_PORT']}")
        print(f"   Table: data_vectors")
        return vector_store
        
    except Exception as e:
        print(f"ERROR: Failed to create PGVectorStore - {e}")
        sys.exit(1)

def load_vectors_file(vectors_file_path):
    """Load vectors from JSON file."""
    try:
        with open(vectors_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"  ERROR: Failed to load vectors file - {e}")
        return None

def create_text_nodes(vectors_data, source_file):
    """Convert vector data to LlamaIndex TextNode objects."""
    chunks = vectors_data.get('chunks', [])
    nodes = []
    
    print(f"  Converting {len(chunks)} chunks to TextNodes...")
    
    # Extract metadata from vectors file
    embedding_metadata = vectors_data.get('embedding_metadata', {})
    processing_metadata = vectors_data.get('processing_metadata', {})
    
    for i, chunk_data in enumerate(chunks):
        # Create metadata for this chunk
        metadata = {
            'source_file': source_file,
            'chunk_index': chunk_data.get('chunk_index', i),
            'content_contextualized': chunk_data.get('content_contextualized', ''),
            'embedding_model': embedding_metadata.get('model', 'unknown'),
            'embedding_method': embedding_metadata.get('embedding_method', 'unknown'),
            'contextualization_method': processing_metadata.get('contextualization_method', 'unknown'),
            'llm_provider': processing_metadata.get('llm_provider', 'unknown'),
            'llm_model': processing_metadata.get('llm_model', 'unknown'),
            # Include original metadata
            **chunk_data.get('metadata', {})
        }
        
        # Create TextNode
        node = TextNode(
            text=chunk_data.get('content', ''),
            metadata=metadata,
            id_=f"{source_file}_chunk_{chunk_data.get('chunk_index', i)}"
        )
        
        # Set embedding if available
        vector = chunk_data.get('vector', [])
        if vector and len(vector) == 768:
            node.embedding = vector
        else:
            print(f"    WARNING: Chunk {i} missing or invalid embedding")
            continue
        
        nodes.append(node)
    
    print(f"  Created {len(nodes)} TextNodes with embeddings")
    return nodes

def process_vectors_file(vectors_file_path, vector_store):
    """Process a single vectors file and insert into LlamaIndex vector store."""
    print(f"\nProcessing: {vectors_file_path.name}")
    
    # Load vectors data
    vectors_data = load_vectors_file(vectors_file_path)
    if not vectors_data:
        return False
    
    # Extract source file name from vectors data or filename
    source_file = vectors_data.get('source_markdown', vectors_file_path.stem.replace('_vectors', ''))
    print(f"  Source file: {source_file}")
    
    # Create TextNode objects
    nodes = create_text_nodes(vectors_data, source_file)
    if not nodes:
        print(f"  No valid nodes created")
        return False
    
    # Insert nodes into vector store
    try:
        print(f"  Inserting {len(nodes)} nodes into vector store...")
        vector_store.add(nodes)
        print(f"  ✅ Successfully inserted {len(nodes)} nodes")
        return True
        
    except Exception as e:
        print(f"  ERROR: Failed to insert nodes - {e}")
        return False

def check_existing_data(vector_store):
    """Check if vectors exist in the store."""
    try:
        # Create a test query to check if the store is accessible
        test_query = VectorStoreQuery(
            query_embedding=[0.0] * 768,  # Dummy embedding
            similarity_top_k=1,
            mode="default"
        )
        
        # Try to execute a minimal query to check if table exists and has data
        result = vector_store.query(test_query)
        
        # Check if the query returned any results
        if hasattr(result, 'nodes') and result.nodes:
            print("  Existing data found in vector store")
            return 1  # Data exists
        else:
            print("  No existing data in vector store")
            return 0
            
    except Exception as e:
        # Query failed, store is empty or not initialized
        print(f"  Vector store appears empty or not initialized")
        return 0

def main():
    print("LlamaIndex Vector Database Insertion")
    print("=" * 50)
    
    # Load config
    config = load_config()
    
    # Create vector store
    print("Creating LlamaIndex PGVectorStore...")
    vector_store = create_vector_store(config)
    
    # Check existing data
    existing_count = check_existing_data(vector_store)
    if existing_count > 0:
        print(f"Found existing vectors in database")
    
    # Setup paths
    vectors_dir = Path("../vectors")
    if not vectors_dir.exists():
        vectors_dir = Path("vectors")
    
    if not vectors_dir.exists():
        print("ERROR: vectors folder not found")
        print("Run: python src/4-vectorization.py first")
        return 1
    
    print(f"Vectors folder: {vectors_dir}")
    
    # Find vector files
    vector_files = list(vectors_dir.glob("*_vectors.json"))
    
    if not vector_files:
        print("No vector files found in vectors folder")
        return 0
    
    print(f"Found {len(vector_files)} vector files")
    
    # Process each vector file
    processed_files = 0
    failed_files = 0
    
    try:
        for vector_file in vector_files:
            try:
                success = process_vectors_file(vector_file, vector_store)
                if success:
                    processed_files += 1
                    print(f"  File processed successfully")
                else:
                    failed_files += 1
                    
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break
            except Exception as e:
                print(f"  ERROR: Unexpected error - {e}")
                failed_files += 1
    
    except Exception as e:
        print(f"ERROR: {e}")
        return 1
    
    # Summary
    print("\n" + "=" * 50)
    print("Results:")
    print(f"Files processed:     {processed_files}")
    print(f"Files failed:        {failed_files}")
    print(f"Total files:         {len(vector_files)}")
    
    # Check final state
    final_state = check_existing_data(vector_store)
    if final_state > 0:
        print("Vector database populated successfully")
    
    if failed_files > 0:
        print(f"\n{failed_files} files had errors")
        return 1
    else:
        print("\nAll files processed successfully!")
        print("Ready to run: python src/6-test.py")
        return 0

if __name__ == "__main__":
    sys.exit(main())