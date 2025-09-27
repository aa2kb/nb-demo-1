"""
Chat completion controller - Pure business logic for chat completions.
Contains no FastAPI dependencies, only business logic.
"""

import time
from typing import Dict, Any, List, Optional
from services.crewai_service import CrewAIService
from models.chat import (
    ChatMessage, generate_completion_id, get_current_timestamp
)


class ChatController:
    def __init__(self):
        self.crewai_service = CrewAIService()
    
    def validate_model(self, model: str) -> bool:
        """Validate if the model is supported."""
        return model == "abu-dhabi-gov"
    
    def validate_messages(self, messages: List[Dict[str, str]]) -> Optional[str]:
        """
        Validate messages and return user message if valid.
        Returns None if validation fails.
        """
        if not messages:
            return None
            
        # Extract the user's question from the last message
        for msg in reversed(messages):
            if msg.get("role") == "user":
                return msg.get("content")
        
        return None
    
    def create_chat_completion(
        self, 
        model: str, 
        messages: List[Dict[str, str]], 
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        stop: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Create a chat completion using CrewAI service.
        Returns a standardized response format.
        """
        # Validate model
        if not self.validate_model(model):
            return {
                "success": False,
                "error": {
                    "type": "model_not_found",
                    "message": f"Model '{model}' not found. Available models: abu-dhabi-gov"
                }
            }
        
        # Validate and extract user message
        user_message = self.validate_messages(messages)
        if not user_message:
            return {
                "success": False,
                "error": {
                    "type": "invalid_messages",
                    "message": "No valid user message found in conversation"
                }
            }
        
        # Get response from CrewAI service
        try:
            chat_result = self.crewai_service.chat(user_message)
            
            if chat_result["status"] == "error":
                return {
                    "success": False,
                    "error": {
                        "type": "crewai_error",
                        "message": f"CrewAI service error: {chat_result['error']}"
                    }
                }
            
            # Calculate token usage (simplified)
            prompt_tokens = sum(len(msg.get("content", "").split()) for msg in messages)
            completion_tokens = len(chat_result["response"].split())
            
            return {
                "success": True,
                "data": {
                    "id": generate_completion_id(),
                    "created": get_current_timestamp(),
                    "model": model,
                    "response": chat_result["response"],
                    "usage": {
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "total_tokens": prompt_tokens + completion_tokens
                    }
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": {
                    "type": "internal_error",
                    "message": f"Internal processing error: {str(e)}"
                }
            }
    
    def create_streaming_completion(
        self, 
        model: str, 
        messages: List[Dict[str, str]], 
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        stop: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Create a streaming chat completion.
        Returns the full content to be streamed and metadata.
        """
        # Use the same logic as non-streaming but return content for streaming
        result = self.create_chat_completion(model, messages, max_tokens, temperature, top_p, stop)
        
        if not result["success"]:
            return result
        
        # Return streaming-specific format
        return {
            "success": True,
            "data": {
                "id": result["data"]["id"],
                "created": result["data"]["created"],
                "model": model,
                "content": result["data"]["response"]
            }
        }
    
    def prepare_streaming_content(self, content: str) -> str:
        """
        Clean and prepare content for streaming.
        Remove CrewAI-specific formatting.
        """
        content = content.strip()
        
        # Remove any potential CrewAI-specific formatting or metadata
        lines = content.split('\n')
        cleaned_lines = []
        for line in lines:
            line = line.strip()
            # Skip lines that look like CrewAI metadata
            if line and not line.startswith(('Thought:', 'Action:', 'Observation:', 'Final Answer:')):
                cleaned_lines.append(line)
        
        return ' '.join(cleaned_lines).strip()