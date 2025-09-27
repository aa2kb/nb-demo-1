"""
Health handlers - Handle HTTP requests/responses for health check endpoints.
Bridge between FastAPI and business logic controllers.
"""

from fastapi import HTTPException
from controllers.agent_controller import AgentController


class HealthHandler:
    def __init__(self):
        self.agent_controller = AgentController()
    
    async def openai_health_check(self):
        """Handle OpenAI-compatible API health check."""
        try:
            # Check if CrewAI service is available
            result = self.agent_controller.get_agent_info()
            
            if result["success"]:
                agent_data = result["data"]
                return {
                    "status": "healthy",
                    "service": "openai-compatible-api",
                    "crewai_status": "connected",
                    "agent_role": agent_data.get("role", "unknown")
                }
            else:
                raise HTTPException(
                    status_code=503,
                    detail={
                        "status": "unhealthy", 
                        "service": "openai-compatible-api",
                        "crewai_status": "disconnected",
                        "error": "Cannot access CrewAI service"
                    }
                )
                
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=503,
                detail={
                    "status": "unhealthy",
                    "service": "openai-compatible-api", 
                    "error": str(e)
                }
            )