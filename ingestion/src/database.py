"""Database setup and connection utilities."""

import logging
from typing import Optional
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from .config import settings

logger = logging.getLogger(__name__)


class DatabaseManager:
    """Manages database connections and setup."""
    
    def __init__(self):
        self.engine: Optional[Engine] = None
    
    def get_engine(self) -> Engine:
        """Get or create database engine."""
        if self.engine is None:
            self.engine = create_engine(
                settings.database_url,
                pool_pre_ping=True,
                pool_recycle=300
            )
        return self.engine
    
    def ensure_database_setup(self) -> bool:
        """Ensure database is properly set up with pgvector extension."""
        try:
            # First, connect to check if the database exists
            engine = self.get_engine()
            
            with engine.connect() as conn:
                # Enable pgvector extension
                try:
                    conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
                    conn.commit()
                    logger.info("pgvector extension enabled successfully")
                except Exception as e:
                    logger.warning(f"Could not enable pgvector extension: {e}")
                    # Continue anyway - it might already be enabled
                
                # Create the documents table if it doesn't exist
                create_table_sql = """
                CREATE TABLE IF NOT EXISTS document_chunks (
                    id SERIAL PRIMARY KEY,
                    document_id VARCHAR(255) NOT NULL,
                    document_name VARCHAR(255) NOT NULL,
                    chunk_index INTEGER NOT NULL,
                    content TEXT NOT NULL,
                    embedding VECTOR(384),
                    metadata JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                
                CREATE INDEX IF NOT EXISTS idx_document_chunks_doc_id ON document_chunks(document_id);
                CREATE INDEX IF NOT EXISTS idx_document_chunks_embedding ON document_chunks USING ivfflat (embedding vector_cosine_ops);
                """
                
                conn.execute(text(create_table_sql))
                conn.commit()
                logger.info("Database tables created successfully")
                
            return True
            
        except Exception as e:
            logger.error(f"Database setup failed: {e}")
            return False
    
    def test_connection(self) -> bool:
        """Test database connection."""
        try:
            engine = self.get_engine()
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            logger.info("Database connection successful")
            return True
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            return False


# Global database manager instance
db_manager = DatabaseManager()