"""
CrewAI service for handling agent-based conversations.
"""

import os
from crewai import Agent, LLM
from typing import Dict, Any, List, Union
from phoenix.client import Client
from .rag_service import government_document_tool

phoenix_client = Client()
agent_role_prompt = phoenix_client.prompts.get(prompt_identifier="agent_role")
agent_role_goal = phoenix_client.prompts.get(prompt_identifier="agent_goal")
agent_role_backstory = phoenix_client.prompts.get(prompt_identifier="agent_backstory")
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
    
    # Fallback to Ollama or explicit Ollama configuration
    ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    return LLM(
        model=f"ollama/{llm_model}",
        base_url=ollama_base_url
    )

llm = get_configured_llm()


class CrewAIService:
    def __init__(self):
        self.chat_agent = Agent(
            role=agent_role_prompt.format().messages[0].get("content").strip(),
            goal=agent_role_goal.format().messages[0].get("content").strip(),
            backstory=agent_role_backstory.format().messages[0].get("content").strip(),
            verbose=True,
            allow_delegation=False,
            llm=llm,
            tools=[government_document_tool],  # Add government document search tool to agent
            max_iter=1,  # Limit to 1 iteration to prevent multiple tool calls
            memory=True  # Enable memory to use previous tool results
        )
    
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