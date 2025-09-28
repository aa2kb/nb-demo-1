"""Document Ingestion Package - Vector-based document processing and storage."""

__version__ = "1.0.0"
__author__ = "Document Ingestion Team"

from .config import settings
from .document_processor import DocumentProcessor, ProcessedDocument
from .embedding_service import EmbeddingService
from .vector_store import VectorStoreManager
from .database import db_manager

__all__ = [
    "settings",
    "DocumentProcessor",
    "ProcessedDocument", 
    "EmbeddingService",
    "VectorStoreManager",
    "db_manager"
]