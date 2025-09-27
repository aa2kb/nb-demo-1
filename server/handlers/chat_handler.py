"""
Chat handlers - Handle HTTP requests/responses for chat endpoints.
Bridge between FastAPI and business logic controllers.
"""

import asyncio
import json
from fastapi import HTTPException, Request
from fastapi.responses import StreamingResponse
from pprint import pprint

from models.chat import (
    ChatCompletionRequest, ChatCompletionResponse, ChatCompletionChoice,
    ChatMessage, Usage, ChatCompletionStreamResponse, ChatCompletionStreamChoice,
    get_current_timestamp
)
from controllers.chat import ChatController


class ChatHandler:
    def __init__(self):
        self.controller = ChatController()
    
    def _log_request(self, request: ChatCompletionRequest):
        """Log the incoming request for debugging."""
        print("\n" + "="*80)
        print("📨 INCOMING CHAT COMPLETION REQUEST")
        print("="*80)
        
        print(f"🤖 Model: {request.model}")
        print(f"🔄 Stream: {request.stream}")
        print(f"🌡️  Temperature: {request.temperature}")
        print(f"📏 Max Tokens: {request.max_tokens}")
        print(f"🎯 Top P: {request.top_p}")
        print(f"🛑 Stop: {request.stop}")
        
        print("\n💬 MESSAGE THREAD:")
        print("-" * 50)
        for i, msg in enumerate(request.messages, 1):
            role_emoji = {"system": "⚙️", "user": "👤", "assistant": "🤖"}.get(msg.role, "❓")
            print(f"{i}. {role_emoji} {msg.role.upper()}:")
            print(f"   Content: {msg.content}")
            print()
        
        print("📋 FULL REQUEST OBJECT:")
        print("-" * 50)
        pprint(request.model_dump(), width=120, depth=3)
        print("="*80 + "\n")
    
    def _convert_messages_to_dict(self, messages):
        """Convert Pydantic models to dict format for controller."""
        return [{"role": msg.role, "content": msg.content} for msg in messages]
    
    def _handle_error(self, error: dict) -> HTTPException:
        """Convert controller error to HTTPException."""
        error_type = error.get("type", "internal_error")
        message = error.get("message", "Unknown error")
        
        status_codes = {
            "model_not_found": 404,
            "invalid_messages": 400,
            "invalid_input": 400,
            "crewai_error": 500,
            "internal_error": 500
        }
        
        status_code = status_codes.get(error_type, 500)
        
        return HTTPException(
            status_code=status_code,
            detail={
                "error": {
                    "message": message,
                    "type": error_type.replace("_", "_"),
                    "code": error_type
                }
            }
        )
    
    async def create_chat_completion(self, request: ChatCompletionRequest, http_request: Request):
        """Handle chat completion request."""
        try:
            # Log the request
            self._log_request(request)
            
            # Convert messages to dict format
            messages = self._convert_messages_to_dict(request.messages)
            
            print('sending message to crewai service:')
            
            # Handle streaming request
            if request.stream:
                return await self._handle_streaming_request(request, messages)
            
            # Handle non-streaming request
            result = self.controller.create_chat_completion(
                model=request.model,
                messages=messages,
                max_tokens=request.max_tokens,
                temperature=request.temperature,
                top_p=request.top_p,
                stop=request.stop
            )
            
            if not result["success"]:
                raise self._handle_error(result["error"])
            
            data = result["data"]
            
            # Create OpenAI-compatible response
            assistant_message = ChatMessage(
                role="assistant",
                content=data["response"]
            )
            
            choice = ChatCompletionChoice(
                index=0,
                message=assistant_message,
                finish_reason="stop"
            )
            
            usage = Usage(
                prompt_tokens=data["usage"]["prompt_tokens"],
                completion_tokens=data["usage"]["completion_tokens"],
                total_tokens=data["usage"]["total_tokens"]
            )
            
            response = ChatCompletionResponse(
                id=data["id"],
                created=data["created"],
                model=data["model"],
                choices=[choice],
                usage=usage
            )
            
            return response
            
        except HTTPException:
            raise
        except Exception as e:
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
    
    async def _handle_streaming_request(self, request: ChatCompletionRequest, messages: list):
        """Handle streaming chat completion request."""
        result = self.controller.create_streaming_completion(
            model=request.model,
            messages=messages,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            stop=request.stop
        )
        
        if not result["success"]:
            raise self._handle_error(result["error"])
        
        data = result["data"]
        
        return StreamingResponse(
            self._simulate_streaming_response(
                content=data["content"], 
                model=data["model"], 
                completion_id=data["id"]
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
    
    async def _simulate_streaming_response(self, content: str, model: str, completion_id: str, chunk_delay: float = 0.05):
        """Simulate streaming response."""
        # Clean the content using streaming controller
        content = self.controller.streaming_controller.prepare_streaming_content(content)
        
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
        chunk_size = 3
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