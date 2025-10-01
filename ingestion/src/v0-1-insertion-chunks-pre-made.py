"""
Document insertion script for pre-made chunks from JSON files.
Processes JSON files containing pre-chunked documents and inserts into PostgreSQL vector store.
"""

import sys
import json
from pathlib import Path
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.schema import TextNode
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.postgres import PGVectorStore
from base.common import get_config


def main():
    print("🚀 Pre-made Chunks Insertion Pipeline")
    print("=" * 40)
    
    # Load config
    try:
        config = get_config()
        print(f"Loaded config: embedding_model={config['EMBEDDING_MODEL']}")
        print(f"Using embedding dimension: {config['EMBEDDING_DIM']}")
        print(f"Using embedding table: {config['EMBEDDING_TABLE_NAME']}")
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
    except Exception as e:
        print(f"Failed to initialize embedding model: {e}")
        return 1
    
    # Find JSON files with pre-made chunks
    chunks_dir = Path("../chunks")
    if not chunks_dir.exists():
        chunks_dir = Path("chunks")
    
    if not chunks_dir.exists():
        print(f"Chunks folder not found: {chunks_dir}")
        print("Creating chunks folder...")
        chunks_dir.mkdir(exist_ok=True)
        print("Please place your JSON chunk files in the chunks folder")
        return 1
    
    json_files = list(chunks_dir.glob("*.json"))
    if not json_files:
        print("No JSON chunk files found")
        return 1
    
    print(f"Found {len(json_files)} JSON chunk files")
    
    # Process each JSON file
    success_count = 0
    error_count = 0
    total_chunks_processed = 0
    
    for json_file in json_files:
        print(f"\n📄 Processing: {json_file.name}")
        
        # Load and validate JSON
        chunk_data = load_chunk_json(json_file)
        if not chunk_data:
            print(f"   ❌ Failed to load JSON file")
            error_count += 1
            continue
        
        # Check if already processed (idempotency)
        source_markdown = chunk_data.get('source_markdown', json_file.stem)
        if check_document_exists(vector_store, source_markdown):
            print(f"   ⏭️  Already processed, skipping")
            continue
        
        # Convert chunks to nodes
        nodes = convert_chunks_to_nodes(chunk_data)
        if not nodes:
            print(f"   ❌ Failed to create nodes from chunks")
            error_count += 1
            continue
        
        print(f"   📊 Created {len(nodes)} nodes from {chunk_data.get('total_chunks', len(nodes))} chunks")
        
        # Insert into vector store
        if insert_nodes(nodes, vector_store, embedding_model):
            print(f"   ✅ Successfully inserted {len(nodes)} chunks")
            success_count += 1
            total_chunks_processed += len(nodes)
        else:
            print(f"   ❌ Failed to insert chunks")
            error_count += 1
    
    # Summary
    print("\n" + "=" * 40)
    print("Insertion Results:")
    print(f"Successfully processed files: {success_count}")
    print(f"Total chunks inserted: {total_chunks_processed}")
    print(f"Errors: {error_count}")
    print(f"Total JSON files: {len(json_files)}")
    
    if error_count == 0:
        print("\n🎉 All chunk files inserted successfully!")
        return 0
    else:
        print(f"\n⚠️  Completed with {error_count} errors")
        return 1


def load_chunk_json(file_path):
    """Load and validate JSON chunk file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Validate required fields
        required_fields = ['chunks']
        for field in required_fields:
            if field not in data:
                print(f"   ❌ Missing required field: {field}")
                return None
        
        if not isinstance(data['chunks'], list):
            print(f"   ❌ 'chunks' must be a list")
            return None
        
        if len(data['chunks']) == 0:
            print(f"   ❌ No chunks found in file")
            return None
        
        print(f"   📊 Loaded {len(data['chunks'])} chunks")
        print(f"   📋 Source: {data.get('source_markdown', 'unknown')}")
        print(f"   🔧 Method: {data.get('chunking_method', 'unknown')}")
        
        return data
    
    except json.JSONDecodeError as e:
        print(f"   ❌ Invalid JSON format: {e}")
        return None
    except Exception as e:
        print(f"   ❌ Error loading file: {e}")
        return None


def convert_chunks_to_nodes(chunk_data):
    """Convert chunk data to LlamaIndex TextNode objects."""
    try:
        nodes = []
        chunks = chunk_data['chunks']
        
        # Extract common metadata
        common_metadata = {
            'source_markdown': chunk_data.get('source_markdown', 'unknown'),
            'total_chunks': chunk_data.get('total_chunks', len(chunks)),
            'chunking_method': chunk_data.get('chunking_method', 'unknown'),
            'created_at': chunk_data.get('created_at', None)
        }
        
        for i, chunk in enumerate(chunks):
            try:
                # Get chunk content
                content = chunk.get('content', '')
                if not content.strip():
                    print(f"   ⚠️  Skipping empty chunk at index {i}")
                    continue
                
                # Combine metadata
                node_metadata = common_metadata.copy()
                
                # Add chunk-specific metadata
                node_metadata.update({
                    'chunk_index': chunk.get('chunk_index', i),
                    'chunk_id': f"{common_metadata['source_markdown']}_{chunk.get('chunk_index', i)}"
                })
                
                # Add any additional metadata from the chunk
                if 'metadata' in chunk and isinstance(chunk['metadata'], dict):
                    node_metadata.update(chunk['metadata'])
                
                # Create TextNode
                node = TextNode(
                    text=content,
                    metadata=node_metadata,
                    id_=node_metadata['chunk_id']
                )
                
                nodes.append(node)
                
            except Exception as e:
                print(f"   ⚠️  Error processing chunk {i}: {e}")
                continue
        
        print(f"   ✅ Successfully converted {len(nodes)} chunks to nodes")
        return nodes
    
    except Exception as e:
        print(f"   ❌ Error converting chunks to nodes: {e}")
        return []


def check_document_exists(vector_store, source_markdown):
    """Check if document chunks are already in the vector store."""
    # For now, always process (can be enhanced with metadata queries)
    # This avoids complex vector store queries for idempotency
    return False


def insert_nodes(nodes, vector_store, embedding_model):
    """Insert nodes into vector store using VectorStoreIndex."""
    if not nodes:
        return False
    
    try:
        # Create storage context with vector store
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        # Create index - this will automatically generate embeddings and insert
        # Process in smaller batches for better memory management
        batch_size = 50
        total_inserted = 0
        
        for i in range(0, len(nodes), batch_size):
            batch = nodes[i:i + batch_size]
            
            try:
                index = VectorStoreIndex(batch, storage_context=storage_context, embed_model=embedding_model)
                total_inserted += len(batch)
                print(f"   📦 Inserted batch {i//batch_size + 1}: {len(batch)} nodes")
                
            except Exception as e:
                print(f"   ⚠️  Error inserting batch {i//batch_size + 1}: {e}")
                continue
        
        print(f"   ✅ Total inserted: {total_inserted}/{len(nodes)} nodes")
        return total_inserted > 0
    
    except Exception as e:
        print(f"   ❌ Error inserting nodes: {e}")
        return False


if __name__ == "__main__":
    sys.exit(main())