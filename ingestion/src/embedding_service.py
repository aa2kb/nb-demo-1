"""Embedding service using Ollama."""

import logging
from typing import List, Optional
import ollama
from llama_index.embeddings.ollama import OllamaEmbedding

from .config import settings

logger = logging.getLogger(__name__)


class EmbeddingService:
    """Handles text embedding using Ollama."""
    
    def __init__(self):
        self.client = ollama.Client(host=settings.ollama_host)
        self.embedding_model = OllamaEmbedding(
            model_name=settings.embedding_model,
            base_url=settings.ollama_host,
        )
        self._verify_model()
    
    def _verify_model(self) -> bool:
        """Verify that the embedding model is available."""
        try:
            models = self.client.list()
            available_models = [model['name'] for model in models['models']]
            
            if settings.embedding_model not in available_models:
                logger.warning(
                    f"Model {settings.embedding_model} not found. "
                    f"Available models: {available_models}"
                )
                return False
            
            logger.info(f"Embedding model {settings.embedding_model} is available")
            return True
            
        except Exception as e:
            logger.error(f"Failed to verify Ollama model: {e}")
            return False
    
    def embed_text(self, text: str) -> Optional[List[float]]:
        """Generate embedding for a single text."""
        try:
            embedding = self.embedding_model.get_text_embedding(text)
            return embedding
        except Exception as e:
            logger.error(f"Failed to generate embedding: {e}")
            return None
    
    def embed_texts(self, texts: List[str]) -> List[Optional[List[float]]]:
        """Generate embeddings for multiple texts."""
        embeddings = []
        
        for i, text in enumerate(texts):
            if i % 10 == 0:
                logger.info(f"Processing embedding {i+1}/{len(texts)}")
            
            embedding = self.embed_text(text)
            embeddings.append(embedding)
        
        logger.info(f"Generated {sum(1 for e in embeddings if e is not None)} embeddings out of {len(texts)}")
        return embeddings
    
    def test_embedding(self) -> bool:
        """Test the embedding service with a simple text."""
        try:
            test_text = "This is a test document for embedding."
            embedding = self.embed_text(test_text)
            
            if embedding and len(embedding) > 0:
                logger.info(f"Embedding test successful. Vector dimension: {len(embedding)}")
                return True
            else:
                logger.error("Embedding test failed: No embedding generated")
                return False
                
        except Exception as e:
            logger.error(f"Embedding test failed: {e}")
            return False