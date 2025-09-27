"""
Models handlers - Handle HTTP requests/responses for model endpoints.
Bridge between FastAPI and business logic controllers.
"""

from fastapi import HTTPException
from models.requests import ModelsResponse, Model
from controllers.models_controller import ModelsController


class ModelsHandler:
    def __init__(self):
        self.controller = ModelsController()
    
    def _handle_error(self, error: dict) -> HTTPException:
        """Convert controller error to HTTPException."""
        error_type = error.get("type", "internal_error")
        message = error.get("message", "Unknown error")
        
        status_codes = {
            "model_not_found": 404,
            "internal_error": 500
        }
        
        status_code = status_codes.get(error_type, 500)
        
        return HTTPException(
            status_code=status_code,
            detail={
                "error": {
                    "message": message,
                    "type": error_type,
                    "code": error_type
                }
            }
        )
    
    async def list_models(self):
        """Handle list models request."""
        try:
            result = self.controller.list_models()
            
            if not result["success"]:
                raise self._handle_error(result["error"])
            
            data = result["data"]
            
            # Convert to Pydantic models
            models = [Model(**model_data) for model_data in data["data"]]
            
            return ModelsResponse(
                object=data["object"],
                data=models
            )
            
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
    
    async def retrieve_model(self, model_id: str):
        """Handle retrieve specific model request."""
        try:
            result = self.controller.get_model(model_id)
            
            if not result["success"]:
                raise self._handle_error(result["error"])
            
            data = result["data"]
            
            return Model(**data)
            
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