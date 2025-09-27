"""
Chat-related data models for OpenAI-compatible API.
These models match the OpenAI API specification to ensure compatibility.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union, Literal
import time


class ChatMessage(BaseModel):
    """A single message in a chat conversation."""
    role: Literal["system", "user", "assistant"]
    content: str


class ChatCompletionRequest(BaseModel):
    """Request model for chat completions endpoint."""
    model: str
    messages: List[ChatMessage]
    max_tokens: Optional[int] = Field(default=None, ge=1)
    temperature: Optional[float] = Field(default=1.0, ge=0.0, le=2.0)
    top_p: Optional[float] = Field(default=1.0, ge=0.0, le=1.0)
    stream: Optional[bool] = Field(default=False)
    stop: Optional[Union[str, List[str]]] = None


class Usage(BaseModel):
    """Token usage information."""
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionChoice(BaseModel):
    """A single choice in a chat completion response."""
    index: int
    message: ChatMessage
    finish_reason: Optional[Literal["stop", "length", "content_filter"]]


class ChatCompletionResponse(BaseModel):
    """Response model for chat completions endpoint."""
    id: str
    object: Literal["chat.completion"] = "chat.completion"
    created: int
    model: str
    choices: List[ChatCompletionChoice]
    usage: Usage


class ChatCompletionStreamChoice(BaseModel):
    """A single choice in a streaming chat completion response."""
    index: int
    delta: Dict[str, Any]
    finish_reason: Optional[Literal["stop", "length", "content_filter"]] = None


class ChatCompletionStreamResponse(BaseModel):
    """Response model for streaming chat completions."""
    id: str
    object: Literal["chat.completion.chunk"] = "chat.completion.chunk"
    created: int
    model: str
    choices: List[ChatCompletionStreamChoice]


def generate_completion_id() -> str:
    """Generate a unique completion ID."""
    return f"chatcmpl-{int(time.time())}"


def get_current_timestamp() -> int:
    """Get current Unix timestamp."""
    return int(time.time())