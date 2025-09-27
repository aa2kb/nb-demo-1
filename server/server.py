from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from crewai_agent import CrewAIService
from openai_routes import openai_router

# Pydantic models for request/response
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

# Initialize FastAPI app
app = FastAPI(
    title="CrewAI Agent API with OpenAI Compatibility",
    description="A hybrid API that provides both CrewAI research agent functionality and OpenAI-compatible endpoints for Ollama models",
    version="2.0.0"
)

# Include OpenAI-compatible routes
app.include_router(openai_router)

# Initialize CrewAI service
crew_service = CrewAIService()

@app.get("/")
async def root():
    """Root endpoint with basic information"""
    return {
        "message": "CrewAI Agent API with OpenAI Compatibility",
        "version": "2.0.0",
        "endpoints": {
            "crewai": [
                "/research - POST: Research a topic using CrewAI",
                "/agent-info - GET: Get CrewAI agent information",
                "/health - GET: Health check for CrewAI service"
            ],
            "openai_compatible": [
                "/v1/models - GET: List available Ollama models as agents",
                "/v1/chat/completions - POST: Create chat completions using Ollama",
                "/v1/models/{model_id} - GET: Get specific model information",
                "/v1/health - GET: Health check for OpenAI-compatible API"
            ]
        },
        "documentation": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "crewai-agent-api"}

@app.get("/agent-info", response_model=AgentInfoResponse)
async def get_agent_info():
    """Get information about the research agent"""
    try:
        agent_info = crew_service.get_agent_info()
        return AgentInfoResponse(**agent_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting agent info: {str(e)}")

@app.post("/research", response_model=ResearchResponse)
async def research_topic(request: ResearchRequest):
    """Research a given topic using the CrewAI agent"""
    try:
        if not request.topic or len(request.topic.strip()) == 0:
            raise HTTPException(status_code=400, detail="Topic cannot be empty")
        
        result = crew_service.research_topic(request.topic)
        
        if result["status"] == "error":
            return ResearchResponse(
                status="error",
                topic=request.topic,
                error=result["error"]
            )
        
        return ResearchResponse(
            status="success",
            topic=request.topic,
            result=result["result"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing research request: {str(e)}")