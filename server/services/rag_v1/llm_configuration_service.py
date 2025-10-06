import os
from typing import Tuple
from llama_index.llms.ollama import Ollama
from llama_index.llms.gemini import Gemini
from llama_index.llms.openrouter import OpenRouter
from llama_index.llms.groq import Groq
from llama_index.llms.openai_like import OpenAILike


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
        elif self.llm_provider == "openrouter":
            return self._setup_openrouter_llms()
        elif self.llm_provider == "groq":
            return self._setup_groq_llms()
        elif self.llm_provider == "fireworks":
            return self._setup_fireworks_llms()
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
    
    def _setup_openrouter_llms(self) -> Tuple[object, object]:
        """Setup OpenRouter LLMs."""
        openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
        
        if not openrouter_api_key:
            print("❌ OPENROUTER_API_KEY not found but OpenRouter provider selected. Falling back to Ollama.")
            return self._setup_ollama_llms()
        
        print("✅ Configuring OpenRouter for both reranking and generation")
        try:
            primary_llm = OpenRouter(
                model=self.llm_model,
                api_key=openrouter_api_key,
                temperature=0.1,
                max_tokens=8192
            )
            secondary_llm = primary_llm  # Use same LLM for both operations
            print("✅ OpenRouter LLMs initialized successfully")
            return primary_llm, secondary_llm
        except Exception as e:
            print(f"⚠️ OpenRouter initialization failed: {str(e)}")
            print("🔄 Falling back to Ollama")
            return self._setup_ollama_llms()
    
    def _setup_groq_llms(self) -> Tuple[object, object]:
        """Setup Groq LLMs."""
        groq_api_key = os.getenv("GROQ_API_KEY")
        
        if not groq_api_key:
            print("❌ GROQ_API_KEY not found but Groq provider selected. Falling back to Ollama.")
            return self._setup_ollama_llms()
        
        print("✅ Configuring Groq for both reranking and generation")
        try:
            primary_llm = Groq(
                model=self.llm_model,
                api_key=groq_api_key,
                temperature=0.1,
                max_tokens=8192
            )
            secondary_llm = primary_llm  # Use same LLM for both operations
            print("✅ Groq LLMs initialized successfully")
            return primary_llm, secondary_llm
        except Exception as e:
            print(f"⚠️ Groq initialization failed: {str(e)}")
            print("🔄 Falling back to Ollama")
            return self._setup_ollama_llms()
    
    def _setup_fireworks_llms(self) -> Tuple[object, object]:
        """Setup Fireworks LLMs using OpenAILike client to bypass model validation."""
        fireworks_api_key = os.getenv("FIREWORKS_API_KEY")
        
        if not fireworks_api_key:
            print("❌ FIREWORKS_API_KEY not found but Fireworks provider selected. Falling back to Ollama.")
            return self._setup_ollama_llms()
        
        print("✅ Configuring Fireworks for both reranking and generation")
        try:
            # Use OpenAILike client for Fireworks to bypass model validation
            primary_llm = OpenAILike(
                model=self.llm_model,
                api_key=fireworks_api_key,
                api_base="https://api.fireworks.ai/inference/v1",
                temperature=0.1,
                max_tokens=8192,
                is_chat_model=True
            )
            secondary_llm = primary_llm  # Use same LLM for both operations
            print("✅ Fireworks LLMs initialized successfully")
            return primary_llm, secondary_llm
        except Exception as e:
            print(f"⚠️ Fireworks initialization failed: {str(e)}")
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