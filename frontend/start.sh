#!/bin/bash
# Start script with explicit environment variables

cd "$(dirname "$0")"

# Activate virtual environment
source .venv/bin/activate

# Export environment variables for Open WebUI
export OPENAI_API_BASE_URL="http://localhost:8000/v1"
export OPENAI_API_KEY="local-api"
export HOST="0.0.0.0"
export PORT="8080"

echo "Starting Open WebUI with configuration:"
echo "- API Base URL: $OPENAI_API_BASE_URL"
echo "- API Key: $OPENAI_API_KEY"
echo "- Host: $HOST"
echo "- Port: $PORT"

# Start Open WebUI
open-webui serve