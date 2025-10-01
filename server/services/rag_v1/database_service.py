import os
import psycopg2
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
            'EMBEDDING_MODEL': os.getenv('EMBEDDING_MODEL', 'nomic-embed-text:v1.5'),
            'EMBEDDING_DIM': int(os.getenv('EMBEDDING_DIM', 768)),  # Ensure this is int
            'EMBEDDING_TABLE_NAME': os.getenv('EMBEDDING_TABLE_NAME', 'vectors_docling_nomic_embed'),  # Match actual table name
        }
        self.vector_store = None
        self.connection = None
    
    def _connect(self):
        """Create direct database connection for diagnostics."""
        import psycopg2
        try:
            self.connection = psycopg2.connect(
                host=self.config['DB_HOST'],
                port=self.config['DB_PORT'],
                database=self.config['DB_NAME'],
                user=self.config['DB_USER'],
                password=self.config['DB_PASSWORD']
            )
            return self.connection
        except Exception as e:
            print(f"❌ Direct connection failed: {e}")
            raise
    
    def get_vector_store(self) -> PGVectorStore:
        """Get PGVectorStore instance with configuration."""
        print(f"🗄️ Connecting to database: {self.config['DB_HOST']}:{self.config['DB_PORT']}/{self.config['DB_NAME']}")
        print(f"📊 Table: {self.config['EMBEDDING_TABLE_NAME']}, Dimensions: {self.config['EMBEDDING_DIM']}")
        
        try:
            self.vector_store = PGVectorStore.from_params(
                database=self.config['DB_NAME'],
                host=self.config['DB_HOST'],
                password=self.config['DB_PASSWORD'],
                port=self.config['DB_PORT'],
                user=self.config['DB_USER'],
                table_name=self.config['EMBEDDING_TABLE_NAME'],
                embed_dim=int(self.config['EMBEDDING_DIM']),  # Force int conversion
                hybrid_search=True,
                text_search_config="english"
            )
            print("✅ Database connection successful")
            return self.vector_store
        except Exception as e:
            print(f"❌ Database connection failed: {type(e).__name__}: {str(e)}")
            raise
    
    def setup_embedding_model(self) -> OllamaEmbedding:
        """Setup embedding model for vector operations."""
        embed_model = OllamaEmbedding(
            model_name=self.config['EMBEDDING_MODEL'],
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