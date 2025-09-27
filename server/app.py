"""
FastAPI application setup and configuration.
"""

from fastapi import FastAPI
from routes import chat_routes, models_routes, agent_routes, health_routes

# Initialize FastAPI app
app = FastAPI(
    title="AgentCrew API with OpenAI Compatibility",
    description="A hybrid API that provides both AgentCrew chat functionality and OpenAI-compatible endpoints using the abu-dhabi-gov model",
    version="2.0.0"
)

# Include routers
app.include_router(chat_routes.router)
app.include_router(models_routes.router)
app.include_router(agent_routes.router)
app.include_router(health_routes.router)


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


