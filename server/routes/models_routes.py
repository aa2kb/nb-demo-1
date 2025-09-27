"""
Models routes - Clean route definitions for model endpoints.
Uses handlers to process requests and responses.
"""

from fastapi import APIRouter
from models.requests import ModelsResponse
from handlers.models_handler import ModelsHandler

# Create router for models endpoints
router = APIRouter(prefix="/v1", tags=["Models"])

# Initialize handler
models_handler = ModelsHandler()


@router.get("/models", response_model=ModelsResponse)
async def list_models():
    """
    List all available models (agents) in OpenAI format.
    Returns the abu-dhabi-gov model powered by CrewAI.
    """
    return await models_handler.list_models()


@router.get("/models/{model_id}")
async def retrieve_model(model_id: str):
    """
    Retrieve information about a specific model.
    """
    return await models_handler.retrieve_model(model_id)