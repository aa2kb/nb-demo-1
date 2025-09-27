"""
Agent handlers - Handle HTTP requests/responses for agent endpoints.
Bridge between FastAPI and business logic controllers.
"""

from fastapi import HTTPException
from models.requests import ResearchRequest, ResearchResponse, AgentInfoResponse
from controllers.agent_controller import AgentController


class AgentHandler:
    def __init__(self):
        self.controller = AgentController()
    
    def _handle_error(self, error: dict) -> HTTPException:
        """Convert controller error to HTTPException."""
        error_type = error.get("type", "internal_error")
        message = error.get("message", "Unknown error")
        
        status_codes = {
            "invalid_input": 400,
            "crewai_error": 500,
            "service_unavailable": 503,
            "internal_error": 500
        }
        
        status_code = status_codes.get(error_type, 500)
        
        return HTTPException(
            status_code=status_code,
            detail=message
        )
    
    async def get_agent_info(self):
        """Handle get agent info request."""
        try:
            result = self.controller.get_agent_info()
            
            if not result["success"]:
                raise self._handle_error(result["error"])
            
            data = result["data"]
            
            return AgentInfoResponse(**data)
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error getting agent info: {str(e)}"
            )
    
    async def chat_with_agent(self, request: ResearchRequest):
        """Handle chat with agent request."""
        try:
            result = self.controller.chat_with_agent(request.topic)
            
            if not result["success"]:
                error = result["error"]
                if error["type"] == "invalid_input":
                    raise HTTPException(status_code=400, detail=error["message"])
                else:
                    raise self._handle_error(error)
            
            data = result["data"]
            
            return ResearchResponse(
                status=data["status"],
                topic=data["topic"],
                result=data["result"]
            )
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error processing chat request: {str(e)}"
            )
    
    async def health_check(self):
        """Handle basic health check request."""
        try:
            result = self.controller.health_check()
            
            if not result["success"]:
                return {"status": "unhealthy", "service": "crewai-agent-api"}
            
            data = result["data"]
            return data
            
        except Exception as e:
            return {"status": "unhealthy", "service": "crewai-agent-api", "error": str(e)}