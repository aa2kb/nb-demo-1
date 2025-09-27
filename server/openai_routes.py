"""
OpenAI-compatible API routes for the server.
These routes implement the OpenAI API specification for compatibility with OpenAI clients.
"""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from typing import Union
import logging

from openai_models import (
    ChatCompletionRequest, ChatCompletionResponse, ModelsResponse, ErrorResponse
)
from ollama_client import OllamaClient

logger = logging.getLogger(__name__)

# Create router for OpenAI-compatible endpoints
openai_router = APIRouter(prefix="/v1", tags=["OpenAI Compatible"])

# Initialize Ollama client
ollama_client = OllamaClient()


@openai_router.get("/models", response_model=ModelsResponse)
async def list_models():
    """
    List all available models (agents) in OpenAI format.
    Maps Ollama models to OpenAI model format.
    """
    try:
        models_response = ollama_client.list_models()
        return models_response
        
    except ConnectionError:
        raise HTTPException(
            status_code=503, 
            detail={
                "error": {
                    "message": "Ollama service is not available. Please ensure Ollama is running.",
                    "type": "service_unavailable",
                    "code": "ollama_connection_error"
                }
            }
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
    Create a chat completion using Ollama models.
    Supports both streaming and non-streaming responses.
    """
    try:
        # Validate that the model exists
        models_response = ollama_client.list_models()
        available_models = [model.id for model in models_response.data]
        
        if request.model not in available_models:
            raise HTTPException(
                status_code=404,
                detail={
                    "error": {
                        "message": f"Model '{request.model}' not found. Available models: {', '.join(available_models)}",
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
        
        # Handle streaming response
        if request.stream:
            def generate_stream():
                try:
                    for chunk in ollama_client.chat_completion_stream(request):
                        yield chunk
                except Exception as e:
                    logger.error(f"Error in streaming: {e}")
                    error_chunk = f"data: {{'error': '{str(e)}'}}\n\n"
                    yield error_chunk
            
            return StreamingResponse(
                generate_stream(),
                media_type="text/plain",
                headers={
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "text/event-stream",
                }
            )
        
        # Handle non-streaming response
        else:
            completion_response = ollama_client.chat_completion(request)
            return completion_response
            
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except ConnectionError:
        raise HTTPException(
            status_code=503,
            detail={
                "error": {
                    "message": "Ollama service is not available. Please ensure Ollama is running.",
                    "type": "service_unavailable", 
                    "code": "ollama_connection_error"
                }
            }
        )
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
        models_response = ollama_client.list_models()
        
        for model in models_response.data:
            if model.id == model_id:
                return model
        
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
        is_healthy = ollama_client.health_check()
        
        if is_healthy:
            return {
                "status": "healthy",
                "service": "openai-compatible-api",
                "ollama_status": "connected"
            }
        else:
            raise HTTPException(
                status_code=503,
                detail={
                    "status": "unhealthy", 
                    "service": "openai-compatible-api",
                    "ollama_status": "disconnected",
                    "error": "Cannot connect to Ollama"
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