"""
Request and response models for the API.
"""

from pydantic import BaseModel
from typing import Dict, Any, List, Literal


class Model(BaseModel):
    """Model information."""
    id: str
    object: Literal["model"] = "model"
    created: int
    owned_by: str = "ollama"


class ModelsResponse(BaseModel):
    """Response model for models endpoint."""
    object: Literal["list"] = "list"
    data: List[Model]


class ErrorResponse(BaseModel):
    """Error response model."""
    error: Dict[str, Any]


# Legacy models for backward compatibility
class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    status: str
    message: str
    result: str = None
    error: str = None


class ResearchRequest(BaseModel):
    topic: str


class ResearchResponse(BaseModel):
    status: str
    topic: str
    result: str = None
    error: str = None


class AgentInfoResponse(BaseModel):
    role: str
    goal: str
    backstory: str
    tools: list