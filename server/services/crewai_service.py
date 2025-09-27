"""
CrewAI service for handling agent-based conversations.
"""

import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from typing import Dict, Any, List, Union

# Load environment variables
load_dotenv()

# Configure Ollama Mistral 7B LLM
llm = LLM(
    model="ollama/mistral:7b",
    base_url="http://localhost:11434"
)


class CrewAIService:
    def __init__(self):
        self.chat_agent = Agent(
            role="AI Assistant",
            goal="Provide helpful and informative responses to user queries",
            backstory="You are a knowledgeable AI assistant that helps users with various questions and tasks.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    
    def chat(self, messages: Union[str, List[Dict[str, str]]]) -> Dict[str, Any]:
        """Chat with Agent using messages array or single string"""
        try:
            result = self.chat_agent.kickoff(messages)
    
            return {
                "status": "success",
                "messages": messages,
                "response": str(result)
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
    
    def get_agent_info(self) -> Dict[str, str]:
        """Get information about the agent"""
        return {
            "role": self.chat_agent.role,
            "goal": self.chat_agent.goal,
            "backstory": self.chat_agent.backstory
        }