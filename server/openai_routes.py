"""
OpenAI-compatible API routes for the server.
These routes implement the OpenAI API specification for compatibility with OpenAI clients.
"""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from typing import Union
import logging
import asyncio
import json
import time

from openai_models import (
    ChatCompletionRequest, ChatCompletionResponse, ModelsResponse, ErrorResponse,
    Model, Usage, ChatCompletionChoice, ChatMessage, generate_completion_id, get_current_timestamp,
    ChatCompletionStreamResponse, ChatCompletionStreamChoice
)
from crewai_agent import AgentCrew

logger = logging.getLogger(__name__)

# Create router for OpenAI-compatible endpoints
openai_router = APIRouter(prefix="/v1", tags=["OpenAI Compatible"])

# Initialize AgentCrew
agent_crew = AgentCrew()


async def simulate_streaming_response(content: str, model: str, completion_id: str, chunk_delay: float = 0.05):
    """
    Simulate streaming by breaking the full response into chunks and yielding them.
    Compatible with OpenWebUI and other OpenAI clients.
    
    Args:
        content: The complete response text to stream
        model: The model name 
        completion_id: The completion ID
        chunk_delay: Delay between chunks in seconds
    """
    # Clean the content to remove any formatting issues that might interfere with OpenWebUI
    content = content.strip()
    
    # Remove any potential CrewAI-specific formatting or metadata
    # Look for common patterns that CrewAI might add
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        # Skip lines that look like CrewAI metadata (e.g., "Thought:", "Action:", etc.)
        if line and not line.startswith(('Thought:', 'Action:', 'Observation:', 'Final Answer:')):
            cleaned_lines.append(line)
    
    # Rejoin the cleaned content
    content = ' '.join(cleaned_lines).strip()
    
    # Split content into words for chunk-by-chunk streaming
    words = content.split()
    
    # Send the first chunk with role information
    first_chunk = ChatCompletionStreamResponse(
        id=completion_id,
        created=get_current_timestamp(),
        model=model,
        choices=[
            ChatCompletionStreamChoice(
                index=0,
                delta={"role": "assistant", "content": ""}
            )
        ]
    )
    yield f"data: {first_chunk.model_dump_json(exclude_none=True)}\n\n"
    
    # Stream content in chunks (multiple words per chunk for better flow)
    chunk_size = 3  # Number of words per chunk
    for i in range(0, len(words), chunk_size):
        chunk_words = words[i:i + chunk_size]
        chunk_content = " ".join(chunk_words)
        
        # Add space before chunk if it's not the first content chunk
        if i > 0:
            chunk_content = " " + chunk_content
            
        stream_chunk = ChatCompletionStreamResponse(
            id=completion_id,
            created=get_current_timestamp(),
            model=model,
            choices=[
                ChatCompletionStreamChoice(
                    index=0,
                    delta={"content": chunk_content}
                )
            ]
        )
        
        yield f"data: {stream_chunk.model_dump_json(exclude_none=True)}\n\n"
        
        # Small delay to simulate real streaming
        await asyncio.sleep(chunk_delay)
    
    # Send final chunk with finish_reason
    final_chunk = ChatCompletionStreamResponse(
        id=completion_id,
        created=get_current_timestamp(),
        model=model,
        choices=[
            ChatCompletionStreamChoice(
                index=0,
                delta={},
                finish_reason="stop"
            )
        ]
    )
    yield f"data: {final_chunk.model_dump_json(exclude_none=True)}\n\n"
    
    # Send the final [DONE] marker
    yield "data: [DONE]\n\n"


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
    Supports both streaming and non-streaming responses.
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
        
        # Use AgentCrew to chat and get the full response first
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
        
        # Handle streaming response by simulating streaming of the full response
        if request.stream:
            completion_id = generate_completion_id()
            return StreamingResponse(
                simulate_streaming_response(
                    content=chat_result["response"], 
                    model=request.model, 
                    completion_id=completion_id
                ),
                media_type="text/event-stream",
                headers={
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "text/event-stream; charset=utf-8",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                    "Access-Control-Allow-Headers": "*"
                }
            )
        
        # Create OpenAI-compatible response (non-streaming)
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