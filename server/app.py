"""
FastAPI application setup and configuration.
"""
from dotenv import load_dotenv
from phoenix.otel import register
from fastapi import FastAPI
from routes import chat_routes, models_routes, health_routes

load_dotenv()

tracer_provider = register(
  project_name="abu-dhabi-gov", # Default is 'default'
  auto_instrument=True # Auto-instrument your app based on installed OI dependencies
)

# Initialize FastAPI app
app = FastAPI(
    title="AgentCrew API with OpenAI Compatibility",
    description="A hybrid API that provides both AgentCrew chat functionality and OpenAI-compatible endpoints using the abu-dhabi-gov model",
    version="2.0.0"
)

# Include routers
app.include_router(chat_routes.router)
app.include_router(models_routes.router)
app.include_router(health_routes.router)


@app.get("/")
async def root():
    """Root endpoint with basic information"""
    return {
        "message": "CrewAI Agent API with OpenAI Compatibility",
        "version": "2.0.0",
        "endpoints": {
            "openai_compatible": [
                "/v1/models - GET: List available abu-dhabi-gov model",
                "/v1/chat/completions - POST: Create chat completions using AgentCrew",
                "/v1/models/{model_id} - GET: Get specific model information",
                "/v1/health - GET: Health check for OpenAI-compatible API"
            ]
        },
        "documentation": "/docs"
    }


