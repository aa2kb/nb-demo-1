"""Configuration settings for the ingestion service."""

from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # Database configuration
    db_host: str = Field(default="localhost", env="DB_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")
    db_user: str = Field(default="admin", env="DB_USER")
    db_password: str = Field(default="admin", env="DB_PASSWORD")
    db_name: str = Field(default="postgres", env="DB_NAME")
    
    # Ollama configuration
    ollama_host: str = Field(default="http://localhost:11434", env="OLLAMA_HOST")
    embedding_model: str = Field(default="embeddinggemma:300m", env="EMBEDDING_MODEL")
    
    # Document processing
    chunk_size: int = Field(default=1024, env="CHUNK_SIZE")
    chunk_overlap: int = Field(default=200, env="CHUNK_OVERLAP")
    
    # Logging
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    
    @property
    def database_url(self) -> str:
        """Get the database URL."""
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()