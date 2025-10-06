"""
CrewAI service for handling agent-based conversations.
"""

import os
from crewai import Agent, LLM
from typing import Dict, Any, List, Union
from .rag_v1.rag_service import rag_document_tool
from .rag_v2 import full_document_tool
from phoenix.client import Client

phoenix_client = Client()
agent_role_prompt = phoenix_client.prompts.get(prompt_identifier=os.getenv("AGENT_ROLE_PROMPT_ID", "agent_role"))
agent_role_goal = phoenix_client.prompts.get(prompt_identifier=os.getenv("AGENT_GOAL_PROMPT_ID", "agent_goal"))
agent_role_backstory = phoenix_client.prompts.get(prompt_identifier=os.getenv("AGENT_BACKSTORY_PROMPT_ID", "agent_backstory"))
    
# TODO: RAG using PGSearchTool
# from crewai_tools import PGSearchTool

# Configure LLM based on environment settings
def get_configured_llm():
    """Get LLM configuration from environment variables."""
    llm_provider = os.getenv("DEFAULT_LLM_PROVIDER", "ollama").lower()
    llm_model = os.getenv("DEFAULT_LLM_MODEL", "mistral:7b")
    
    print(f"🤖 CrewAI using LLM Provider: {llm_provider}, Model: {llm_model}")
    
    if llm_provider == "gemini":
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            print("❌ GEMINI_API_KEY not found but Gemini provider selected. Falling back to Ollama.")
            llm_provider = "ollama"
            llm_model = "mistral:7b"
        else:
            return LLM(
                model=f"gemini/{llm_model}",
                api_key=gemini_api_key
            )
    
    elif llm_provider == "openrouter":
        openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
        openrouter_base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        if not openrouter_api_key:
            print("❌ OPENROUTER_API_KEY not found but OpenRouter provider selected. Falling back to Ollama.")
            llm_provider = "ollama"
            llm_model = "mistral:7b"
        else:
            return LLM(
                model=f"openrouter/{llm_model}",
                base_url=openrouter_base_url,
                api_key=openrouter_api_key
            )
    
    elif llm_provider == "groq":
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            print("❌ GROQ_API_KEY not found but Groq provider selected. Falling back to Ollama.")
            llm_provider = "ollama"
            llm_model = "mistral:7b"
        else:
            return LLM(
                model=f"groq/{llm_model}",
                api_key=groq_api_key,
                temperature=0.1,  # Lower temperature for more consistent responses
                max_tokens=131072   # Ensure adequate token limit
            )
    
    elif llm_provider == "fireworks":
        fireworks_api_key = os.getenv("FIREWORKS_API_KEY")
        if not fireworks_api_key:
            print("❌ FIREWORKS_API_KEY not found but Fireworks provider selected. Falling back to Ollama.")
            llm_provider = "ollama"
            llm_model = "mistral:7b"
        else:
            return LLM(
                model=f"fireworks_ai/{llm_model}",
                api_key=fireworks_api_key,
                temperature=0.7
            )
    
    # Fallback to Ollama or explicit Ollama configuration
    ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    return LLM(
        model=f"ollama/{llm_model}",
        base_url=ollama_base_url
    )

llm = get_configured_llm()


class CrewAIService:
    def __init__(self):
        # Get role, goal, and backstory with proper error handling
        role = agent_role_prompt.format().messages[0].get("content", "Abu Dhabi Government AI Assistant").strip()
        goal = agent_role_goal.format().messages[0].get("content", "Provide accurate government information").strip()
        backstory = agent_role_backstory.format().messages[0].get("content", "Expert Abu Dhabi government assistant").strip()
        
        print(f"🤖 Creating agent with role: {role[:50]}...")
        
        self.chat_agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            verbose=True,
            allow_delegation=False,
            llm=llm,
            tools=[rag_document_tool, full_document_tool],
            max_iter=2,
            memory=True
        )
        print("✅ CrewAI Agent initialized successfully")
            
    
    def chat(self, messages: Union[str, List[Dict[str, str]]]) -> Dict[str, Any]:
        """Chat with Agent using messages array or single string"""
        try:
            result = self.chat_agent.kickoff(messages)
            cleanResult = str(result).replace("### Assistant:", "").strip()
            if cleanResult != str(result):
                print("Stripped Assistant prefix from response")
            return {
                "status": "success",
                "messages": messages,
                "response": str(cleanResult)
            }
        except Exception as e:
            return {
                "status": "error",
                "messages": messages,
                "error": str(e)
            }
    
    def get_agent_info(self) -> Dict[str, str]:
        """Get information about the agent"""
        return {
            "role": self.chat_agent.role,
            "goal": self.chat_agent.goal,
            "backstory": self.chat_agent.backstory
        }