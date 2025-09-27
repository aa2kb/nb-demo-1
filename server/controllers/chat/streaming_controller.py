"""
Chat streaming controller - Handles streaming-specific logic.
Manages content preparation and streaming response formatting.
"""

from typing import Dict, Any
from models.chat import get_current_timestamp


class ChatStreamingController:
    """
    Controller responsible for streaming chat completions.
    Handles content preparation and streaming response formatting.
    """
    
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
    
    def format_streaming_response(
        self,
        completion_id: str,
        model: str,
        content: str
    ) -> Dict[str, Any]:
        """
        Format a streaming completion response.
        Returns streaming-specific format with cleaned content.
        """
        cleaned_content = self.prepare_streaming_content(content)
        
        return {
            "success": True,
            "data": {
                "id": completion_id,
                "created": get_current_timestamp(),
                "model": model,
                "content": cleaned_content
            }
        }
    
    def create_streaming_chunk(
        self,
        completion_id: str,
        model: str,
        delta: str,
        finish_reason: str = None
    ) -> Dict[str, Any]:
        """
        Create a single streaming chunk in OpenAI format.
        """
        chunk = {
            "id": completion_id,
            "object": "chat.completion.chunk",
            "created": get_current_timestamp(),
            "model": model,
            "choices": [{
                "index": 0,
                "delta": {"content": delta} if delta else {},
                "finish_reason": finish_reason
            }]
        }
        
        return chunk
    
    def split_content_for_streaming(self, content: str, chunk_size: int = 20) -> list:
        """
        Split content into chunks suitable for streaming.
        Returns list of content chunks.
        """
        words = content.split()
        chunks = []
        
        for i in range(0, len(words), chunk_size):
            chunk = ' '.join(words[i:i + chunk_size])
            if i + chunk_size < len(words):
                chunk += ' '  # Add space between chunks
            chunks.append(chunk)
        
        return chunks