"""
CrewAI service for handling agent-based conversations.
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from typing import Dict, Any

# Load environment variables
load_dotenv()

# Configure Ollama Mistral 7B LLM
llm = LLM(
    model="ollama/mistral:7b",
    base_url="http://localhost:11434"
)


class CrewAIService:
    def __init__(self):
        # Define a simple chat agent
        self.chat_agent = Agent(
            role='AI Assistant',
            goal='Provide helpful and informative responses to user queries',
            backstory='You are a knowledgeable AI assistant that helps users with various questions and tasks.',
            verbose=False,
            allow_delegation=False,
            llm=llm
        )
        
        # Create a task with placeholder for user message input
        self.chat_task = Task(
            description="Respond to the user's message: {user_message}",
            agent=self.chat_agent,
            expected_output="A helpful and informative response to the user's query"
        )
        
        # Create a crew with the agent and task
        self.crew = Crew(
            agents=[self.chat_agent],
            tasks=[self.chat_task],
            verbose=True
        )
    
    def chat(self, message: str) -> Dict[str, Any]:
        """Chat method that uses CrewAI crew.kickoff() with inputs"""
        try:
            # Execute the crew with inputs and get the result
            result = self.crew.kickoff(inputs={"user_message": message})
            
            return {
                "status": "success",
                "message": message,
                "response": str(result)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": message,
                "error": str(e)
            }
    
    def get_agent_info(self) -> Dict[str, str]:
        """Get information about the agent"""
        return {
            "role": self.chat_agent.role,
            "goal": self.chat_agent.goal,
            "backstory": self.chat_agent.backstory
        }