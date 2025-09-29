"""
LLM Configuration Service for Government Document Search.
Handles setup and configuration of LLMs (Gemini and Ollama).
"""

import os
from typing import Tuple
from llama_index.llms.ollama import Ollama
from llama_index.llms.gemini import Gemini


class LLMConfigurationService:
    """Service for LLM setup and configuration."""
    
    def __init__(self):
        """Initialize LLM configuration service."""
        self.llm_provider = os.getenv("DEFAULT_LLM_PROVIDER", "ollama").lower()
        self.llm_model = os.getenv("DEFAULT_LLM_MODEL", "mistral:7b")
    
    def setup_llms(self) -> Tuple[object, object]:
        """
        Setup and configure LLMs based on environment settings.
        
        Returns:
            Tuple of (primary_llm, secondary_llm)
        """
        print(f"🤖 Using LLM Provider: {self.llm_provider}, Model: {self.llm_model}")
        
        # Setup LLMs based on provider
        if self.llm_provider == "gemini":
            return self._setup_gemini_llms()
        else:
            return self._setup_ollama_llms()
    
    def _setup_gemini_llms(self) -> Tuple[object, object]:
        """Setup Gemini LLMs."""
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            print("❌ GEMINI_API_KEY not found but Gemini provider selected. Falling back to Ollama.")
            return self._setup_ollama_llms()
        
        print("✅ Configuring Gemini Flash for both reranking and generation")
        try:
            primary_llm = Gemini(
                model=self.llm_model,
                api_key=gemini_api_key,
                temperature=0.1,
                max_tokens=8192
            )
            secondary_llm = primary_llm  # Use same LLM for both operations
            print("✅ Gemini LLMs initialized successfully")
            return primary_llm, secondary_llm
        except Exception as e:
            print(f"⚠️ Gemini initialization failed: {str(e)}")
            print("🔄 Falling back to Ollama")
            return self._setup_ollama_llms()
    
    def _setup_ollama_llms(self) -> Tuple[object, object]:
        """Setup Ollama LLMs."""
        print("✅ Configuring Ollama for both reranking and generation")
        primary_llm = Ollama(
            model=self.llm_model if self.llm_provider == "ollama" else "mistral:7b",
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            request_timeout=60.0
        )
        secondary_llm = primary_llm  # Use same LLM for both operations
        return primary_llm, secondary_llm
    
    def get_fallback_llm(self) -> object:
        """Get fallback Ollama LLM for error scenarios."""
        try:
            fallback_llm = Ollama(
                model="mistral:7b",
                base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                request_timeout=60.0
            )
            return fallback_llm
        except Exception as e:
            print(f"❌ Fallback LLM creation failed: {str(e)}")
            raise