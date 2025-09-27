"""
Ollama service for communicating with the local Ollama instance.
Handles OpenAI-compatible API requests to Ollama models.
"""

import requests
import json
import logging
from typing import List, Dict, Any, Optional, Generator
from models.chat import (
    ChatMessage, ChatCompletionRequest, ChatCompletionResponse,
    ChatCompletionStreamResponse, ChatCompletionChoice, ChatCompletionStreamChoice,
    Usage, generate_completion_id, get_current_timestamp
)
from models.requests import Model, ModelsResponse

logger = logging.getLogger(__name__)


class OllamaService:
    """Service for communicating with Ollama API."""
    
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip("/")
        
    def _make_request(self, endpoint: str, method: str = "GET", data: Optional[Dict] = None) -> requests.Response:
        """Make a request to Ollama API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, timeout=30)
            elif method.upper() == "POST":
                response = requests.post(url, json=data, timeout=60)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            response.raise_for_status()
            return response
            
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Cannot connect to Ollama at {self.base_url}. Make sure Ollama is running.")
        except requests.exceptions.Timeout:
            raise TimeoutError("Request to Ollama timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error communicating with Ollama: {e}")
    
    def list_models(self) -> ModelsResponse:
        """List all available models from Ollama."""
        try:
            response = self._make_request("api/tags")
            ollama_data = response.json()
            
            models = []
            for model_info in ollama_data.get("models", []):
                model = Model(
                    id=model_info["name"],
                    created=get_current_timestamp(),
                    owned_by="ollama"
                )
                models.append(model)
            
            return ModelsResponse(data=models)
            
        except Exception as e:
            logger.error(f"Error listing models: {e}")
            raise RuntimeError(f"Failed to list models: {e}")
    
    def _messages_to_prompt(self, messages: List[ChatMessage]) -> str:
        """Convert OpenAI messages format to a single prompt for Ollama."""
        prompt_parts = []
        
        for message in messages:
            role = message.role
            content = message.content
            
            if role == "system":
                prompt_parts.append(f"System: {content}")
            elif role == "user":
                prompt_parts.append(f"User: {content}")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")
        
        # Add final prompt for assistant response
        prompt_parts.append("Assistant:")
        
        return "\n\n".join(prompt_parts)
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough estimation of token count (approximate)."""
        # Very rough approximation: 1 token ≈ 4 characters
        return max(1, len(text) // 4)
    
    def chat_completion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """Create a chat completion using Ollama."""
        try:
            # Convert messages to prompt
            prompt = self._messages_to_prompt(request.messages)
            
            # Prepare Ollama request
            ollama_request = {
                "model": request.model,
                "prompt": prompt,
                "stream": False,
                "options": {}
            }
            
            # Add optional parameters
            if request.max_tokens:
                ollama_request["options"]["num_predict"] = request.max_tokens
            if request.temperature is not None:
                ollama_request["options"]["temperature"] = request.temperature
            if request.top_p is not None:
                ollama_request["options"]["top_p"] = request.top_p
            if request.stop:
                if isinstance(request.stop, str):
                    ollama_request["options"]["stop"] = [request.stop]
                else:
                    ollama_request["options"]["stop"] = request.stop
            
            # Make request to Ollama
            response = self._make_request("api/generate", "POST", ollama_request)
            ollama_response = response.json()
            
            # Extract response text
            response_text = ollama_response.get("response", "")
            
            # Estimate token usage
            prompt_tokens = self._estimate_tokens(prompt)
            completion_tokens = self._estimate_tokens(response_text)
            total_tokens = prompt_tokens + completion_tokens
            
            # Create OpenAI-compatible response
            completion_id = generate_completion_id()
            
            choice = ChatCompletionChoice(
                index=0,
                message=ChatMessage(role="assistant", content=response_text),
                finish_reason="stop"
            )
            
            usage = Usage(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=total_tokens
            )
            
            return ChatCompletionResponse(
                id=completion_id,
                created=get_current_timestamp(),
                model=request.model,
                choices=[choice],
                usage=usage
            )
            
        except Exception as e:
            logger.error(f"Error in chat completion: {e}")
            raise RuntimeError(f"Chat completion failed: {e}")
    
    def chat_completion_stream(self, request: ChatCompletionRequest) -> Generator[str, None, None]:
        """Create a streaming chat completion using Ollama."""
        try:
            # Convert messages to prompt
            prompt = self._messages_to_prompt(request.messages)
            
            # Prepare Ollama request for streaming
            ollama_request = {
                "model": request.model,
                "prompt": prompt,
                "stream": True,
                "options": {}
            }
            
            # Add optional parameters
            if request.max_tokens:
                ollama_request["options"]["num_predict"] = request.max_tokens
            if request.temperature is not None:
                ollama_request["options"]["temperature"] = request.temperature
            if request.top_p is not None:
                ollama_request["options"]["top_p"] = request.top_p
            if request.stop:
                if isinstance(request.stop, str):
                    ollama_request["options"]["stop"] = [request.stop]
                else:
                    ollama_request["options"]["stop"] = request.stop
            
            # Make streaming request to Ollama
            url = f"{self.base_url}/api/generate"
            
            completion_id = generate_completion_id()
            created_timestamp = get_current_timestamp()
            
            with requests.post(url, json=ollama_request, stream=True, timeout=60) as response:
                response.raise_for_status()
                
                for line in response.iter_lines():
                    if line:
                        try:
                            chunk_data = json.loads(line)
                            
                            if "response" in chunk_data:
                                content = chunk_data["response"]
                                
                                # Create streaming response chunk
                                choice = ChatCompletionStreamChoice(
                                    index=0,
                                    delta={"content": content} if content else {},
                                    finish_reason=None
                                )
                                
                                stream_response = ChatCompletionStreamResponse(
                                    id=completion_id,
                                    created=created_timestamp,
                                    model=request.model,
                                    choices=[choice]
                                )
                                
                                yield f"data: {stream_response.model_dump_json()}\n\n"
                            
                            # Check if this is the final chunk
                            if chunk_data.get("done", False):
                                # Send final chunk with finish_reason
                                final_choice = ChatCompletionStreamChoice(
                                    index=0,
                                    delta={},
                                    finish_reason="stop"
                                )
                                
                                final_response = ChatCompletionStreamResponse(
                                    id=completion_id,
                                    created=created_timestamp,
                                    model=request.model,
                                    choices=[final_choice]
                                )
                                
                                yield f"data: {final_response.model_dump_json()}\n\n"
                                yield "data: [DONE]\n\n"
                                break
                                
                        except json.JSONDecodeError:
                            continue
                            
        except Exception as e:
            logger.error(f"Error in streaming chat completion: {e}")
            raise RuntimeError(f"Streaming chat completion failed: {e}")
    
    def health_check(self) -> bool:
        """Check if Ollama is healthy and reachable."""
        try:
            response = self._make_request("api/tags")
            return response.status_code == 200
        except Exception:
            return False