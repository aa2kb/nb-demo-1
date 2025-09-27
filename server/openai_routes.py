"""
OpenAI-compatible API routes for the server.
These routes implement the OpenAI API specification for compatibility with OpenAI clients.
"""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from typing import Union
import logging

from openai_models import (
    ChatCompletionRequest, ChatCompletionResponse, ModelsResponse, ErrorResponse,
    Model, Usage, ChatCompletionChoice, ChatMessage, generate_completion_id, get_current_timestamp
)
from crewai_agent import AgentCrew

logger = logging.getLogger(__name__)

# Create router for OpenAI-compatible endpoints
openai_router = APIRouter(prefix="/v1", tags=["OpenAI Compatible"])

# Initialize AgentCrew
agent_crew = AgentCrew()


@openai_router.get("/models", response_model=ModelsResponse)
async def list_models():
    """
    List all available models (agents) in OpenAI format.
    Returns the abu-dhabi-gov model powered by CrewAI.
    """
    try:
        # Return the abu-dhabi-gov model
        abu_dhabi_model = Model(
            id="abu-dhabi-gov",
            created=get_current_timestamp(),
            owned_by="abu-dhabi-government"
        )
        
        return ModelsResponse(
            data=[abu_dhabi_model]
        )
        
    except Exception as e:
        logger.error(f"Error listing models: {e}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "message": f"Internal server error: {str(e)}",
                    "type": "internal_error",
                    "code": "server_error"
                }
            }
        )


@openai_router.post("/chat/completions", response_model=None)
async def create_chat_completion(
    request: ChatCompletionRequest,
    http_request: Request
):
    """
    Create a chat completion using CrewAI agents.
    Currently supports non-streaming responses only.
    """
    try:
        print('received chat completion request:', request)
        # Validate that the model is abu-dhabi-gov
        if request.model != "abu-dhabi-gov":
            raise HTTPException(
                status_code=404,
                detail={
                    "error": {
                        "message": f"Model '{request.model}' not found. Available models: abu-dhabi-gov",
                        "type": "invalid_request_error",
                        "code": "model_not_found"
                    }
                }
            )
        
        # Validate messages
        if not request.messages:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": {
                        "message": "Messages cannot be empty",
                        "type": "invalid_request_error", 
                        "code": "invalid_messages"
                    }
                }
            )
        
        # Handle streaming response (not yet implemented for CrewAI)
        if request.stream:
            raise HTTPException(
                status_code=501,
                detail={
                    "error": {
                        "message": "Streaming is not yet supported with CrewAI agents",
                        "type": "not_implemented_error",
                        "code": "streaming_not_supported"
                    }
                }
            )
        
        # Extract the user's question from the last message
        user_message = None
        for msg in reversed(request.messages):
            if msg.role == "user":
                user_message = msg.content
                break
        
        if not user_message:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": {
                        "message": "No user message found in conversation",
                        "type": "invalid_request_error",
                        "code": "no_user_message"
                    }
                }
            )
        
        # Use AgentCrew to chat
        print('sending message to agentcrew:')
        chat_result = agent_crew.chat(user_message)
        
        if chat_result["status"] == "error":
            raise HTTPException(
                status_code=500,
                detail={
                    "error": {
                        "message": f"AgentCrew error: {chat_result['error']}",
                        "type": "internal_error",
                        "code": "agentcrew_error"
                    }
                }
            )
        
        # Create OpenAI-compatible response
        assistant_message = ChatMessage(
            role="assistant",
            content=chat_result["response"]
        )
        
        choice = ChatCompletionChoice(
            index=0,
            message=assistant_message,
            finish_reason="stop"
        )
        
        # Estimate token usage (simplified)
        prompt_tokens = sum(len(msg.content.split()) for msg in request.messages)
        completion_tokens = len(chat_result["response"].split())
        
        usage = Usage(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens
        )
        
        response = ChatCompletionResponse(
            id=generate_completion_id(),
            created=get_current_timestamp(),
            model=request.model,
            choices=[choice],
            usage=usage
        )
        
        return response
            
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        logger.error(f"Error in chat completion: {e}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "message": f"Internal server error: {str(e)}",
                    "type": "internal_error",
                    "code": "server_error"
                }
            }
        )


@openai_router.get("/models/{model_id}")
async def retrieve_model(model_id: str):
    """
    Retrieve information about a specific model.
    """
    try:
        if model_id == "abu-dhabi-gov":
            return Model(
                id="abu-dhabi-gov",
                created=get_current_timestamp(),
                owned_by="abu-dhabi-government"
            )
        
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "message": f"Model '{model_id}' not found",
                    "type": "invalid_request_error",
                    "code": "model_not_found"
                }
            }
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving model {model_id}: {e}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "message": f"Internal server error: {str(e)}",
                    "type": "internal_error", 
                    "code": "server_error"
                }
            }
        )


# Health check endpoint for OpenAI API
@openai_router.get("/health")
async def openai_health_check():
    """
    Health check for the OpenAI-compatible API.
    """
    try:
        # Check if AgentCrew is available
        agent_info = agent_crew.get_agent_info()
        
        if agent_info:
            return {
                "status": "healthy",
                "service": "openai-compatible-api",
                "agentcrew_status": "connected",
                "agent_role": agent_info.get("role", "unknown")
            }
        else:
            raise HTTPException(
                status_code=503,
                detail={
                    "status": "unhealthy", 
                    "service": "openai-compatible-api",
                    "agentcrew_status": "disconnected",
                    "error": "Cannot access AgentCrew service"
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