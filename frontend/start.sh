#!/bin/bash
# Start script with explicit environment variables

cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Export environment variables for Open WebUI
export OPENAI_API_BASE_URL="http://localhost:8000/v1"
export OPENAI_API_KEY="local-api"
export HOST="0.0.0.0"
export PORT="8080"
export ENABLE_FOLLOW_UP_GENERATION=false
export ENABLE_TAGS_GENERATION=false

echo "Starting Open WebUI with configuration:"
echo "- API Base URL: $API_BASE_URL"
echo "- API Key: $API_KEY"
echo "- Host: $HOST"
echo "- Port: $PORT"
echo "- Follow-up Generation: $ENABLE_FOLLOW_UP_GENERATION"
echo "- Tags Generation: $ENABLE_TAGS_GENERATION"

# Start Open WebUI
open-webui serve