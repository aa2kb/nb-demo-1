#!/bin/bash
# Start script for Arize Phoenix telemetry server

cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies if requirements.txt has been updated
echo "Installing dependencies..."
pip install -r requirements.txt

# Set environment variables for Phoenix
export API_BASE_URL="http://localhost:8000/v1"
export API_KEY="local-api"
export PHOENIX_HOST="0.0.0.0"
export PHOENIX_PORT="6006"

echo "Starting Arize Phoenix with configuration:"
echo "- Host: $PHOENIX_HOST"
echo "- Port: $PHOENIX_PORT"
echo "- Phoenix UI will be available at: http://localhost:6006"

# Start Phoenix server
phoenix serve