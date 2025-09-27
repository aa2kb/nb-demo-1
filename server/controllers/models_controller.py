"""
Models controller - Pure business logic for model management.
Contains no FastAPI dependencies, only business logic.
"""

from typing import Dict, Any, List
from models.chat import get_current_timestamp


class ModelsController:
    def __init__(self):
        # Define available models
        self.available_models = [
            {
                "id": "abu-dhabi-gov",
                "object": "model",
                "created": get_current_timestamp(),
                "owned_by": "abu-dhabi-government"
            }
        ]
    
    def list_models(self) -> Dict[str, Any]:
        """
        Get list of available models.
        Returns standardized response format.
        """
        try:
            return {
                "success": True,
                "data": {
                    "object": "list",
                    "data": self.available_models
                }
            }
        except Exception as e:
            return {
                "success": False,
                "error": {
                    "type": "internal_error",
                    "message": f"Error listing models: {str(e)}"
                }
            }
    
    def get_model(self, model_id: str) -> Dict[str, Any]:
        """
        Get specific model information.
        Returns standardized response format.
        """
        try:
            # Find the model
            for model in self.available_models:
                if model["id"] == model_id:
                    return {
                        "success": True,
                        "data": model
                    }
            
            # Model not found
            return {
                "success": False,
                "error": {
                    "type": "model_not_found",
                    "message": f"Model '{model_id}' not found"
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": {
                    "type": "internal_error",
                    "message": f"Error retrieving model: {str(e)}"
                }
            }
    
    def is_model_available(self, model_id: str) -> bool:
        """Check if a model is available."""
        return any(model["id"] == model_id for model in self.available_models)