import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai.tools import BaseTool
from typing import Dict, Any

# Load environment variables
load_dotenv()

# Configure Ollama Mistral 7B LLM
llm = LLM(
    model="ollama/mistral:7b",
    base_url="http://localhost:11434"
)

class SimpleResearchTool(BaseTool):
    name: str = "Simple Research Tool"
    description: str = "A basic tool that provides information on simple topics"

    def _run(self, topic: str) -> str:
        """Simple research simulation"""
        research_data = {
            "python": "Python is a high-level programming language known for its simplicity and readability.",
            "ai": "Artificial Intelligence involves creating systems that can perform tasks typically requiring human intelligence.",
            "crewai": "CrewAI is a framework for building AI agent teams that work together on complex tasks.",
            "default": f"Research topic: {topic}. This is a basic research result for demonstration purposes."
        }
        return research_data.get(topic.lower(), research_data["default"])

class CrewAIService:
    def __init__(self):
        self.research_tool = SimpleResearchTool()
        
        # Define the research agent
        self.research_agent = Agent(
            role='Research Analyst',
            goal='Provide comprehensive research on given topics',
            backstory='You are an experienced research analyst with expertise in various fields.',
            tools=[self.research_tool],
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    
    def research_topic(self, topic: str) -> Dict[str, Any]:
        """Execute a research task on a given topic"""
        task = Task(
            description=f'Research and provide information about: {topic}',
            agent=self.research_agent,
            expected_output='A comprehensive report with key findings and insights'
        )
        
        crew = Crew(
            agents=[self.research_agent],
            tasks=[task],
            verbose=True,
            planning_llm=llm
        )
        
        try:
            result = crew.kickoff()
            return {
                "status": "success",
                "topic": topic,
                "result": str(result)
            }
        except Exception as e:
            return {
                "status": "error",
                "topic": topic,
                "error": str(e)
            }
    
    def get_agent_info(self) -> Dict[str, str]:
        """Get information about the agent"""
        return {
            "role": self.research_agent.role,
            "goal": self.research_agent.goal,
            "backstory": self.research_agent.backstory,
            "tools": [tool.name for tool in self.research_agent.tools]
        }