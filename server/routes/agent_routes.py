"""
Agent routes - Clean route definitions for agent endpoints.
Uses handlers to process requests and responses.
"""

from fastapi import APIRouter
from models.requests import AgentInfoResponse
from handlers.agent_handler import AgentHandler

# Create router for agent endpoints
router = APIRouter(tags=["Agent"])

# Initialize handler
agent_handler = AgentHandler()


@router.get("/agent-info", response_model=AgentInfoResponse)
async def get_agent_info():
    """Get information about the chat agent"""
    return await agent_handler.get_agent_info()


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return await agent_handler.health_check()