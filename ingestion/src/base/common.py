"""
Super simple common utilities - just config and vector store.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from llama_index.vector_stores.postgres import PGVectorStore

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
        'EMBEDDING_DIM': int(os.getenv('EMBEDDING_DIM', 1024)),
    }

def get_vector_store_v1():
    """Get PGVectorStore instance. v1"""
    config = get_config()
    
    return PGVectorStore.from_params(
        database=config['DB_NAME'],
        host=config['DB_HOST'],
        password=config['DB_PASSWORD'],
        port=config['DB_PORT'],
        user=config['DB_USER'],
        table_name="vectors",
        embed_dim=1024,
        hybrid_search=True,
        text_search_config="english"
    )

def get_vector_store_v2():
    """Get PGVectorStore instance. v2"""
    config = get_config()
    
    return PGVectorStore.from_params(
        database=config['DB_NAME'],
        host=config['DB_HOST'],
        password=config['DB_PASSWORD'],
        port=config['DB_PORT'],
        user=config['DB_USER'],
        table_name="vectors_v2",
        embed_dim=1024,
        hybrid_search=True,
        text_search_config="english"
    )