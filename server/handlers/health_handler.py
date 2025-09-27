"""
Health handlers - Handle HTTP requests/responses for health check endpoints.
Bridge between FastAPI and business logic controllers.
"""

from fastapi import HTTPException
from services.crewai_service import CrewAIService


class HealthHandler:
    def __init__(self):
        self.crewai_service = CrewAIService()
    
    async def openai_health_check(self):
        """Handle OpenAI-compatible API health check."""
        try:
            # Check if CrewAI service is available
            agent_info = self.crewai_service.get_agent_info()
            
            if agent_info:
                return {
                    "status": "healthy",
                    "service": "openai-compatible-api",
                    "crewai_status": "connected",
                    "agent_role": agent_info.get("role", "unknown")
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