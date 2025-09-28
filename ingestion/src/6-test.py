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

# Required imports
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.core.vector_stores import VectorStoreQuery



# Global query variable
query = "What are the procurement procedures for government entities?"
def main():
    """Semantic search using LlamaIndex PGVectorStore with exact same config as setup/insertion."""
    print("Semantic Search with LlamaIndex PGVectorStore")
    print("=" * 60)
    
    # Load config
    config = load_config()
    
    # Setup embedding model
    print("Setting up embedding model...")
    embedding_model = setup_embedding_model(config)
    
    # Setup LlamaIndex PGVectorStore with EXACT same configuration
    print("Creating LlamaIndex PGVectorStore...")
    vector_store = create_vector_store(config)
    
    # Check database stats
    vector_count = check_vector_count(config)
    print(f"Vector database: {vector_count} vectors available")
    
    print(f"\nSearching for: '{query}'")
    
    try:
        # Generate query embedding
        print(f"\nGenerating embedding for query...")
        query_embedding = generate_query_embedding(embedding_model, query)
        if not query_embedding:
            print("Failed to generate query embedding")
            return
        
        # Search using LlamaIndex PGVectorStore
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
            print("You may need to run the insertion script first.")
    
    except KeyboardInterrupt:
        print("\nSearch interrupted by user")
    except Exception as e:
        print(f"ERROR: Search failed - {e}")
    
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

def setup_embedding_model(config):
    """Setup embedding model for query vectorization."""
    try:
        embedding_model = OllamaEmbedding(
            model_name=config['EMBEDDING_MODEL'],
            base_url=config['OLLAMA_HOST']
        )
        print(f"✅ Connected to Ollama embedding model: {config['EMBEDDING_MODEL']}")
        return embedding_model
    except Exception as e:
        print(f"ERROR: Failed to setup embedding model - {e}")
        sys.exit(1)

def create_vector_store(config):
    """Create LlamaIndex PGVectorStore using the EXACT same configuration as setup and insertion."""
    try:
        from llama_index.vector_stores.postgres import PGVectorStore
    except ImportError:
        print("ERROR: llama-index-vector-stores-postgres not installed")
        print("Run: pip install llama-index-vector-stores-postgres")
        sys.exit(1)
    
    try:
        # Use EXACT same configuration as 0-setup.py and 5-insertion.py
        vector_store = PGVectorStore.from_params(
            database=config['DB_NAME'],
            host=config['DB_HOST'],
            password=config['DB_PASSWORD'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            table_name="vectors",  # This creates data_vectors table
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

def check_vector_count(config):
    """Check how many vectors are in the database."""
    try:
        import psycopg2
        
        conn = psycopg2.connect(
            host=config['DB_HOST'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
            database=config['DB_NAME']
        )
        cursor = conn.cursor()
        
        # Check if table exists and get count
        cursor.execute("""
            SELECT COUNT(*) FROM information_schema.tables 
            WHERE table_name = 'data_vectors'
        """)
        
        if cursor.fetchone()[0] == 0:
            cursor.close()
            conn.close()
            return 0
        
        cursor.execute("SELECT COUNT(*) FROM data_vectors")
        count = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
        
        return count
        
    except Exception as e:
        print(f"Could not check vector count - {e}")
        return 0



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
    try:
        # Create a VectorStoreQuery
        query_obj = VectorStoreQuery(
            query_embedding=query_embedding,
            similarity_top_k=top_k,
            mode="default"
        )
        
        # Execute the query
        print(f"  Executing similarity search for top {top_k} results...")
        query_result = vector_store.query(query_obj)
        
        search_results = []
        
        # Handle case where no results are returned
        if not query_result.nodes:
            print("  No nodes returned from vector store")
            return []
        
        print(f"  Found {len(query_result.nodes)} matching nodes")
        
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
                'source_file': parsed_metadata.get('source_file', parsed_metadata.get('source_file_name', 'Unknown')),
                'source_path': parsed_metadata.get('source_file_path', ''),
                'similarity_score': float(similarity) if similarity is not None else 0.0,
                'metadata': parsed_metadata
            })
        
        return search_results
        
    except Exception as e:
        print(f"ERROR: Failed to search with LlamaIndex PGVectorStore - {e}")
        return []







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