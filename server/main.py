"""Main entry point for the CrewAI FastAPI application.

This module serves as the main entry point for running the CrewAI agent API server.
It imports the FastAPI app from server.py and runs it using uvicorn.

Usage:
    python main.py

The server will start on http://0.0.0.0:8000 with auto-reload enabled.
"""

import uvicorn
from app import app

def main():
    """Start the FastAPI server with uvicorn."""
    print("Starting CrewAI Agent API Server...")
    print("Server will be available at: http://localhost:8000")
    print("API Documentation: http://localhost:8000/docs")
    print("Press CTRL+C to stop the server")
    print("-" * 50)
    
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()