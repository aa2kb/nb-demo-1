"""
Chat controller - Main orchestrator for chat completion functionality.
Coordinates validation, completion, and streaming controllers.
"""

from typing import Dict, Any, List, Optional
from .validation_controller import ChatValidationController
from .completion_controller import ChatCompletionController
from .streaming_controller import ChatStreamingController


class ChatController:
    """
    Main chat controller that orchestrates all chat-related functionality.
    Delegates to specialized controllers for validation, completion, and streaming.
    """
    
    def __init__(self):
        self.validation_controller = ChatValidationController()
        self.completion_controller = ChatCompletionController()
        self.streaming_controller = ChatStreamingController()
    
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
        Create a chat completion.
        Validates input and delegates to completion controller.
        """
        # Validate all parameters
        validation_result = self.validation_controller.validate_chat_parameters(
            model, messages, max_tokens, temperature, top_p, stop
        )
        
        if not validation_result["success"]:
            return validation_result
        
        # Delegate to completion controller
        return self.completion_controller.create_completion(
            model, 
            validation_result["user_message"], 
            messages, 
            max_tokens, 
            temperature, 
            top_p, 
            stop
        )
    
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
        Validates input and delegates to completion and streaming controllers.
        """
        # Validate all parameters
        validation_result = self.validation_controller.validate_chat_parameters(
            model, messages, max_tokens, temperature, top_p, stop
        )
        
        if not validation_result["success"]:
            return validation_result
        
        # Get completion result
        completion_result = self.completion_controller.create_completion(
            model,
            validation_result["user_message"],
            messages,
            max_tokens,
            temperature,
            top_p,
            stop
        )
        
        if not completion_result["success"]:
            return completion_result
        
        # Format for streaming using streaming controller
        return self.streaming_controller.format_streaming_response(
            completion_result["data"]["id"],
            model,
            completion_result["data"]["response"]
        )