"""
Chat completion controller - Handles core completion logic.
Orchestrates CrewAI service interactions and response formatting.
"""

from typing import Dict, Any, List, Optional
from services.crewai_service import CrewAIService
from models.chat import generate_completion_id, get_current_timestamp


class ChatCompletionController:
    """
    Controller responsible for creating chat completions.
    Handles CrewAI service interactions and response formatting.
    """
    
    def __init__(self):
        self.crewai_service = CrewAIService()
    
    def create_completion(
        self, 
        model: str,
        user_message: str,
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
        try:
            # Pass the full messages array to CrewAI service for context-aware responses
            chat_result = self.crewai_service.chat(messages=messages)
            
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
    
    def calculate_token_usage(self, messages: List[Dict[str, str]], response: str) -> Dict[str, int]:
        """
        Calculate token usage for the completion.
        Simplified token counting based on word splitting.
        """
        prompt_tokens = sum(len(msg.get("content", "").split()) for msg in messages)
        completion_tokens = len(response.split())
        
        return {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens
        }
    
    def format_completion_response(
        self,
        completion_id: str,
        model: str,
        response: str,
        usage: Dict[str, int]
    ) -> Dict[str, Any]:
        """
        Format a successful completion response.
        """
        return {
            "success": True,
            "data": {
                "id": completion_id,
                "created": get_current_timestamp(),
                "model": model,
                "response": response,
                "usage": usage
            }
        }