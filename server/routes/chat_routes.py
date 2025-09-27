"""
Chat routes - Clean route definitions for chat endpoints.
Uses handlers to process requests and responses.
"""

from fastapi import APIRouter, Request
from models.chat import ChatCompletionRequest
from handlers.chat_handler import ChatHandler

# Create router for chat endpoints
router = APIRouter(prefix="/v1", tags=["Chat"])

# Initialize handler
chat_handler = ChatHandler()


@router.post("/chat/completions", response_model=None)
async def create_chat_completion(request: ChatCompletionRequest, http_request: Request):
    """
    Create a chat completion using CrewAI agents.
    Supports both streaming and non-streaming responses.
    """
    return await chat_handler.create_chat_completion(request, http_request)