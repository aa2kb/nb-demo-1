"""
Database Service for Government Document Search.
Handles vector store and database connection management.
"""

import os
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding


class DatabaseService:
    """Service for database and vector store operations."""
    
    def __init__(self):
        """Initialize database service with configuration."""
        self.config = {
            'DB_HOST': os.getenv('DB_HOST', 'localhost'),
            'DB_PORT': int(os.getenv('DB_PORT', 5432)),
            'DB_USER': os.getenv('DB_USER', 'admin'),
            'DB_PASSWORD': os.getenv('DB_PASSWORD', 'admin'),
            'DB_NAME': os.getenv('DB_NAME', 'postgres'),
        }
    
    def get_vector_store(self) -> PGVectorStore:
        """Get PGVectorStore instance with configuration."""
        print(f"🗄️ Connecting to database: {self.config['DB_HOST']}:{self.config['DB_PORT']}/{self.config['DB_NAME']}")
        
        try:
            vector_store = PGVectorStore.from_params(
                database=self.config['DB_NAME'],
                host=self.config['DB_HOST'],
                password=self.config['DB_PASSWORD'],
                port=self.config['DB_PORT'],
                user=self.config['DB_USER'],
                table_name="vectors_v2",
                embed_dim=1024,
                hybrid_search=True,
                text_search_config="english"
            )
            print("✅ Database connection successful")
            return vector_store
        except Exception as e:
            print(f"❌ Database connection failed: {type(e).__name__}: {str(e)}")
            raise
    
    def setup_embedding_model(self) -> OllamaEmbedding:
        """Setup embedding model for vector operations."""
        embed_model = OllamaEmbedding(
            model_name="bge-m3:latest",
            base_url="http://localhost:11434"
        )
        return embed_model
    
    def create_index(self, vector_store: PGVectorStore, embed_model: OllamaEmbedding) -> VectorStoreIndex:
        """Create vector store index."""
        index = VectorStoreIndex.from_vector_store(
            vector_store, 
            embed_model=embed_model
        )
        return index
    
    def setup_components(self) -> tuple:
        """
        Setup all database components.
        
        Returns:
            Tuple of (vector_store, embed_model, index)
        """
        vector_store = self.get_vector_store()
        embed_model = self.setup_embedding_model()
        index = self.create_index(vector_store, embed_model)
        
        return vector_store, embed_model, index