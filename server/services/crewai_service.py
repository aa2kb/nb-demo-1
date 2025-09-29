"""
CrewAI service for handling agent-based conversations.
"""

import os
from crewai import Agent, LLM
from typing import Dict, Any, List, Union
from phoenix.client import Client
from .rag_service import hr_rag_tool

phoenix_client = Client()
agent_role_prompt = phoenix_client.prompts.get(prompt_identifier="agent_role")
agent_role_goal = phoenix_client.prompts.get(prompt_identifier="agent_goal")
agent_role_backstory = phoenix_client.prompts.get(prompt_identifier="agent_backstory")
# TODO: RAG using PGSearchTool
# from crewai_tools import PGSearchTool

# Configure Ollama Mistral 7B LLM
llm = LLM(
    model="ollama/mistral:7b",
    base_url="http://localhost:11434"
)


class CrewAIService:
    def __init__(self):
        self.chat_agent = Agent(
            role=agent_role_prompt.format().messages[0].get("content").strip(),
            goal=agent_role_goal.format().messages[0].get("content").strip(),
            backstory=agent_role_backstory.format().messages[0].get("content").strip(),
            verbose=True,
            allow_delegation=False,
            llm=llm,
            tools=[hr_rag_tool],  # Add HR RAG tool to agent
            max_iter=3,  # Limit iterations to prevent tool hallucination
            step_callback=self._tool_callback
        )
    
    def _tool_callback(self, step):
        """Callback to monitor tool usage and prevent hallucination."""
        if hasattr(step, 'tool_input') and step.tool_input:
            print(f"🔧 Tool being used: {step.tool_input}")
        return step
    
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