from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from crewai_agent import AgentCrew
from openai_routes import openai_router

# Pydantic models for request/response
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    status: str
    message: str
    result: str = None
    error: str = None

# Keep ResearchRequest/Response for backward compatibility
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
    title="AgentCrew API with OpenAI Compatibility",
    description="A hybrid API that provides both AgentCrew chat functionality and OpenAI-compatible endpoints using the abu-dhabi-gov model",
    version="2.0.0"
)

# Include OpenAI-compatible routes
app.include_router(openai_router)

# Initialize AgentCrew
agent_crew = AgentCrew()

@app.get("/")
async def root():
    """Root endpoint with basic information"""
    return {
        "message": "CrewAI Agent API with OpenAI Compatibility",
        "version": "2.0.0",
        "endpoints": {
            "agentcrew": [
                "/chat - POST: Chat with the AgentCrew",
                "/agent-info - GET: Get AgentCrew information",
                "/health - GET: Health check for AgentCrew service"
            ],
            "openai_compatible": [
                "/v1/models - GET: List available abu-dhabi-gov model",
                "/v1/chat/completions - POST: Create chat completions using AgentCrew",
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
    """Get information about the chat agent"""
    try:
        agent_info = agent_crew.get_agent_info()
        return AgentInfoResponse(**agent_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting agent info: {str(e)}")

@app.post("/chat", response_model=ResearchResponse)
async def chat_with_agent(request: ResearchRequest):
    """Chat with the AgentCrew"""
    try:
        if not request.topic or len(request.topic.strip()) == 0:
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        result = agent_crew.chat(request.topic)
        
        if result["status"] == "error":
            return ResearchResponse(
                status="error",
                topic=request.topic,
                error=result["error"]
            )
        
        return ResearchResponse(
            status="success",
            topic=request.topic,
            result=result["response"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")