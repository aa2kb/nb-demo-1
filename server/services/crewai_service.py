"""
CrewAI service for handling agent-based conversations.
"""

import os
from crewai import Agent, LLM
from typing import Dict, Any, List, Union
from phoenix.client import Client


# Configure Ollama Mistral 7B LLM
llm = LLM(
    model="ollama/mistral:7b",
    base_url="http://localhost:11434"
)


class CrewAIService:
    def __init__(self):
        self.chat_agent = Agent(
            role="You are a Abu Dhabi Government AI Assistant",
            goal="Provide helpful and informative responses to user queries regarding Abu Dhabi government services.",
            backstory="You are a knowledgeable AI assistant that helps users with various questions and tasks regarding Abu Dhabi government services and information.",
            verbose=True,
            allow_delegation=False,
            llm=llm
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
    
    def get_agent_info(self) -> Dict[str, str]:
        """Get information about the agent"""
        return {
            "role": self.chat_agent.role,
            "goal": self.chat_agent.goal,
            "backstory": self.chat_agent.backstory
        }