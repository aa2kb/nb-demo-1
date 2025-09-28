#!/usr/bin/env python3
"""
Test semantic search functionality.
Takes a query, generates embedding, and finds top 25 similar chunks from the database.
"""

import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
from typing import List, Dict, Any, Tuple

# Third-party imports that might not be available
try:
    import psycopg2
except ImportError:
    psycopg2 = None

try:
    from llama_index.embeddings.ollama import OllamaEmbedding
except ImportError:
    OllamaEmbedding = None

try:
    from llama_index.vector_stores.postgres import PGVectorStore
    from llama_index.core import VectorStoreIndex, StorageContext
    from llama_index.core.vector_stores import VectorStoreQuery
except ImportError:
    PGVectorStore = None
    VectorStoreIndex = None
    StorageContext = None
    VectorStoreQuery = None



# Global query variable
query = "What are the procurement procedures for government entities?"
def main():
    """Semantic search using ONLY LlamaIndex PGVectorStore."""
    print("Semantic Search with LlamaIndex PGVectorStore ONLY")
    print("=" * 60)
    
    # Load config
    config = load_config()
    
    # Setup database connection (for stats only)
    print("Connecting to database for stats...")
    conn = connect_database(config)
    cursor = conn.cursor()
    
    # Check pgvector support
    check_pgvector_support(cursor)
    
    # Setup embedding model
    print("Setting up embedding model...")
    embedding_model = setup_embedding_model(config)
    
    # Setup LlamaIndex PGVectorStore
    print("Setting up LlamaIndex PGVectorStore...")
    vector_store = setup_pgvector_store(config)
    
    # Check database stats (from original tables)
    try:
        cursor.execute("SELECT COUNT(*) FROM documents_sources WHERE processing_status = 'completed';")
        doc_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM document_chunks;")
        chunk_count = cursor.fetchone()[0]
        
        print(f"Original database: {doc_count} documents, {chunk_count} chunks")
    except Exception:
        print("Original database tables not accessible")
    
    print(f"\nSearching for: '{query}'")
    
    try:
        # Generate query embedding
        print(f"\nGenerating embedding for query...")
        query_embedding = generate_query_embedding(embedding_model, query)
        if not query_embedding:
            print("Failed to generate query embedding")
            return
        
        # Search using ONLY LlamaIndex PGVectorStore
        print("Searching with LlamaIndex PGVectorStore...")
        results = search_similar_chunks_llamaindex(vector_store, query_embedding, top_k=25)
        
        # Print results
        print_search_results(results, query)
        
        if results:
            print(f"\n✅ Found {len(results)} results using LlamaIndex PGVectorStore")
            print(f"Best match: {results[0]['similarity_score']*100:.1f}% similarity")
        else:
            print("❌ No results found")
            print("Note: LlamaIndex PGVectorStore table might be empty.")
            print("You may need to insert data into the LlamaIndex table first.")
    
    except KeyboardInterrupt:
        print("\nSearch interrupted by user")
    
    finally:
        cursor.close()
        conn.close()
    
    print("\nSearch completed!")

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
        'OLLAMA_HOST': os.getenv('OLLAMA_HOST', 'http://localhost:11434'),
        'EMBEDDING_MODEL': os.getenv('EMBEDDING_MODEL', 'embeddinggemma:300m'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO')
    }

def connect_database(config):
    """Connect to PostgreSQL database."""
    if psycopg2 is None:
        print("ERROR: psycopg2 not installed. Run: pip install psycopg2-binary")
        sys.exit(1)
    
    try:
        conn = psycopg2.connect(
            host=config['DB_HOST'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
            database=config['DB_NAME']
        )
        return conn
    except Exception as e:
        print(f"ERROR: Failed to connect to database - {e}")
        sys.exit(1)

def setup_embedding_model(config):
    """Setup embedding model for query vectorization."""
    if OllamaEmbedding is None:
        print("ERROR: llama-index-embeddings-ollama not installed")
        print("Run: pip install llama-index-embeddings-ollama")
        sys.exit(1)
    
    try:
        embedding_model = OllamaEmbedding(
            model_name=config['EMBEDDING_MODEL'],
            base_url=config['OLLAMA_HOST']
        )
        return embedding_model
    except Exception as e:
        print(f"ERROR: Failed to setup embedding model - {e}")
        sys.exit(1)

def setup_pgvector_store(config):
    """Setup PGVectorStore using LlamaIndex with existing document_chunks table."""
    if PGVectorStore is None:
        print("ERROR: llama-index-vector-stores-postgres not installed")
        print("Run: pip install llama-index-vector-stores-postgres")
        sys.exit(1)
    
    try:
        # Use the vectors table created by setup
        vector_store = PGVectorStore.from_params(
            database=config['DB_NAME'],
            host=config['DB_HOST'],
            password=config['DB_PASSWORD'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            table_name="vectors",  # This will become data_vectors
            embed_dim=768,
            hybrid_search=False,
            text_search_config="english"
        )
        
        print(f"✅ LlamaIndex PGVectorStore initialized with 'vectors' table")
        return vector_store
    except Exception as e:
        print(f"ERROR: Failed to setup PGVectorStore - {e}")
        print(f"Error details: {str(e)}")
        # Try without custom column mapping as fallback
        try:
            print("Trying with default column names...")
            vector_store = PGVectorStore.from_params(
                database=config['DB_NAME'],
                host=config['DB_HOST'],
                password=config['DB_PASSWORD'],
                port=config['DB_PORT'],
                user=config['DB_USER'],
                table_name="document_chunks",
                embed_dim=768,
                hybrid_search=False,
                text_search_config="english"
            )
            print(f"✅ LlamaIndex PGVectorStore initialized with default settings")
            return vector_store
        except Exception as e2:
            print(f"ERROR: Both attempts failed - {e2}")
            sys.exit(1)

def check_pgvector_support(cursor):
    """Check if pgvector is available."""
    try:
        cursor.execute("SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';")
        result = cursor.fetchone()
        if result:
            print(f"Using pgvector v{result[1]} for similarity search")
            return True
        else:
            print("pgvector not available, using JSON embeddings")
            return False
    except Exception as e:
        print(f"ERROR: Failed to check pgvector - {e}")
        return False

def generate_query_embedding(embedding_model, query: str) -> List[float]:
    """Generate embedding for the query string."""
    try:
        print(f"Generating embedding for query: '{query[:50]}{'...' if len(query) > 50 else ''}'")
        embedding = embedding_model.get_text_embedding(query)
        print(f"Generated {len(embedding)}-dimensional embedding")
        return embedding
    except Exception as e:
        print(f"ERROR: Failed to generate query embedding - {e}")
        return []

def search_similar_chunks_llamaindex(vector_store, query_embedding: List[float], top_k: int = 25) -> List[Dict]:
    """Search for similar chunks using LlamaIndex PGVectorStore."""
    if vector_store is None:
        print("ERROR: Vector store not available")
        sys.exit(1)
    
    try:
        # Create a VectorStoreQuery
        query_obj = VectorStoreQuery(
            query_embedding=query_embedding,
            similarity_top_k=top_k,
            mode="default"
        )
        
        # Execute the query
        query_result = vector_store.query(query_obj)
        
        search_results = []
        
        # Handle case where no results are returned
        if not query_result.nodes:
            print("No nodes returned from LlamaIndex PGVectorStore query")
            return []
        
        for i, node in enumerate(query_result.nodes):
            # Get similarity score if available
            similarity = query_result.similarities[i] if query_result.similarities and i < len(query_result.similarities) else 0.0
            
            # Extract metadata from the node
            metadata = node.metadata if hasattr(node, 'metadata') else {}
            
            # Parse metadata if it's a JSON string
            if isinstance(metadata, dict):
                parsed_metadata = metadata
            elif isinstance(metadata, str):
                try:
                    parsed_metadata = json.loads(metadata)
                except json.JSONDecodeError:
                    parsed_metadata = {}
            else:
                parsed_metadata = {}
            
            search_results.append({
                'id': getattr(node, 'node_id', f'node_{i}'),
                'chunk_index': parsed_metadata.get('chunk_index', i),
                'content': node.text if hasattr(node, 'text') else str(node),
                'content_contextualized': parsed_metadata.get('content_contextualized', ''),
                'source_file': parsed_metadata.get('source_file_name', 'Unknown'),
                'source_path': parsed_metadata.get('source_file_path', ''),
                'similarity_score': float(similarity) if similarity is not None else 0.0,
                'metadata': parsed_metadata
            })
        
        return search_results
        
    except Exception as e:
        print(f"ERROR: Failed to search with LlamaIndex PGVectorStore - {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)







def print_search_results(results: List[Dict], query: str):
    """Print search results in a readable format."""
    print("\n" + "=" * 80)
    print(f"SEARCH RESULTS FOR: '{query}'")
    print("=" * 80)
    
    if not results:
        print("No results found.")
        return
    
    print(f"Found {len(results)} results:")
    print()
    
    for i, result in enumerate(results, 1):
        similarity_percent = result['similarity_score'] * 100
        
        print(f"[{i:2d}] Similarity: {similarity_percent:.1f}% | Source: {result['source_file']}")
        print(f"     Chunk #{result['chunk_index']} (ID: {result['id']})")
        
        # Show context if available
        if result.get('content_contextualized'):
            print(f"     Context: {result['content_contextualized'][:100]}{'...' if len(result['content_contextualized']) > 100 else ''}")
        
        # Show content preview
        content_preview = result['content'][:200].replace('\n', ' ').strip()
        print(f"     Content: {content_preview}{'...' if len(result['content']) > 200 else ''}")
        print()




if __name__ == "__main__":
    main()