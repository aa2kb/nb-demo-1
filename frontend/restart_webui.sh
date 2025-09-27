#!/bin/bash
# Kill existing Open WebUI process and restart with proper config

echo "Stopping any existing Open WebUI processes..."
pkill -f "open-webui"

echo "Waiting for process to stop..."
sleep 2

echo "Starting Open WebUI with local API configuration..."
cd "$(dirname "$0")"

# Load environment variables from .env
if [ -f .env ]; then
    echo "Loading .env configuration..."
    export $(grep -v '^#' .env | xargs)
fi

# Activate virtual environment
source .venv/bin/activate

# Start Open WebUI with environment variables
echo "Configuration:"
echo "- API Base URL: $OPENAI_API_BASE_URL"
echo "- Host: $HOST"
echo "- Port: $PORT"

open-webui serve