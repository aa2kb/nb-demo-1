"""
Health check endpoints for the API.
"""

from fastapi import APIRouter, HTTPException
import logging
from services.crewai_service import CrewAIService

logger = logging.getLogger(__name__)

# Create router for health check endpoints
router = APIRouter(prefix="/v1", tags=["Health"])

# Initialize CrewAI service
crewai_service = CrewAIService()


@router.get("/health")
async def health_check():
    """
    Health check for the OpenAI-compatible API.
    """
    try:
        # Check if CrewAI service is available
        agent_info = crewai_service.get_agent_info()
        
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
            
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "service": "openai-compatible-api", 
                "error": str(e)
            }
        )