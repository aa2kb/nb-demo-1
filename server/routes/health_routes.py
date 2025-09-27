"""
Health routes - Clean route definitions for health check endpoints.
Uses handlers to process requests and responses.
"""

from fastapi import APIRouter
from handlers.health_handler import HealthHandler

# Create router for health endpoints
router = APIRouter(prefix="/v1", tags=["Health"])

# Initialize handler
health_handler = HealthHandler()


@router.get("/health")
async def openai_health_check():
    """
    Health check for the OpenAI-compatible API.
    """
    return await health_handler.openai_health_check()