"""
RAG v2 Services Module

This module contains the second version of RAG (Retrieval-Augmented Generation) services
that uses full document loading instead of vector search.

Key differences from RAG v1:
- Uses document detection to find relevant documents
- Loads entire markdown files into LLM context
- Uses Gemini Flash Lite for processing large contexts
- No vector search or chunking required
"""

from .full_document_service import FullDocumentRAGService, FullDocumentTool, full_document_tool

__all__ = [
    "FullDocumentRAGService",
    "FullDocumentTool", 
    "full_document_tool"
]