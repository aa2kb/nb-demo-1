"""
Chat validation controller - Handles all chat-related input validation.
Pure validation logic with no business logic dependencies.
"""

from typing import Dict, List, Optional


class ChatValidationController:
    """
    Controller responsible for validating chat-related inputs.
    """
    
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
    
    def validate_chat_parameters(
        self,
        model: str,
        messages: List[Dict[str, str]],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        stop: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """
        Validate all chat completion parameters.
        Returns validation result with success/error information.
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
        
        # Validate optional parameters
        if max_tokens is not None and max_tokens <= 0:
            return {
                "success": False,
                "error": {
                    "type": "invalid_parameter",
                    "message": "max_tokens must be a positive integer"
                }
            }
        
        if temperature is not None and (temperature < 0 or temperature > 2):
            return {
                "success": False,
                "error": {
                    "type": "invalid_parameter",
                    "message": "temperature must be between 0 and 2"
                }
            }
        
        if top_p is not None and (top_p < 0 or top_p > 1):
            return {
                "success": False,
                "error": {
                    "type": "invalid_parameter",
                    "message": "top_p must be between 0 and 1"
                }
            }
        
        return {
            "success": True,
            "user_message": user_message
        }