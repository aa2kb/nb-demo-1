"""
Agent controller - Pure business logic for agent operations.
Contains no FastAPI dependencies, only business logic.
"""

from typing import Dict, Any
from services.crewai_service import CrewAIService


class AgentController:
    def __init__(self):
        self.crewai_service = CrewAIService()
    
    def get_agent_info(self) -> Dict[str, Any]:
        """
        Get information about the agent.
        Returns standardized response format.
        """
        try:
            agent_info = self.crewai_service.get_agent_info()
            return {
                "success": True,
                "data": {
                    "role": agent_info.get("role", ""),
                    "goal": agent_info.get("goal", ""),
                    "backstory": agent_info.get("backstory", ""),
                    "tools": []  # Add tools list when available
                }
            }
        except Exception as e:
            return {
                "success": False,
                "error": {
                    "type": "internal_error",
                    "message": f"Error getting agent info: {str(e)}"
                }
            }
    
    def chat_with_agent(self, topic: str) -> Dict[str, Any]:
        """
        Chat with the agent on a specific topic.
        Returns standardized response format.
        """
        try:
            if not topic or len(topic.strip()) == 0:
                return {
                    "success": False,
                    "error": {
                        "type": "invalid_input",
                        "message": "Topic cannot be empty"
                    }
                }
            
            result = self.crewai_service.chat(topic)
            
            if result["status"] == "error":
                return {
                    "success": False,
                    "error": {
                        "type": "crewai_error",
                        "message": result["error"]
                    }
                }
            
            return {
                "success": True,
                "data": {
                    "status": "success",
                    "topic": topic,
                    "result": result["response"]
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": {
                    "type": "internal_error",
                    "message": f"Error processing chat request: {str(e)}"
                }
            }
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check agent health status.
        Returns standardized response format.
        """
        try:
            # Test if we can get agent info
            agent_info_result = self.get_agent_info()
            
            if agent_info_result["success"]:
                return {
                    "success": True,
                    "data": {
                        "status": "healthy",
                        "service": "crewai-agent-api",
                        "agent_available": True
                    }
                }
            else:
                return {
                    "success": False,
                    "error": {
                        "type": "service_unavailable",
                        "message": "Agent service is not available"
                    }
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": {
                    "type": "internal_error",
                    "message": f"Health check failed: {str(e)}"
                }
            }