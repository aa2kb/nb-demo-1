# Using Your Local OpenAI-Compatible API with Open WebUI

## Quick Setup Guide

Your local server is running an OpenAI-compatible API at `http://localhost:8000/v1` with the `abu-dhabi-gov` model available. Here's how to connect it to Open WebUI:

## Method 1: Configure Through Open WebUI Interface (Recommended)

1. **Access Open WebUI**: Go to http://localhost:8080
2. **Open Settings**: Click the settings/gear icon (usually top-right corner)
3. **Navigate to Connections**: Look for "Admin Panel" → "Connections" or "Settings" → "External Connections"
4. **Add New Connection**:
   - **API Base URL**: `http://localhost:8000/v1`
   - **API Key**: Use any value (e.g., "local-api") - your server doesn't require authentication
   - **Model**: The system will detect `abu-dhabi-gov` automatically

## Method 2: Use Environment File (.env) - Recommended

The easiest way is to use the `.env` file that's already configured:

```bash
cd frontend
./start.sh
```

Or manually:
```bash
cd frontend
source .venv/bin/activate
open-webui serve  # Will automatically load .env file
```

## Method 3: Use the Configuration Script

Run the provided script that handles both `.env` and fallback configuration:

```bash
cd frontend
./configure_local_api.sh
```

## Method 4: Manual Environment Setup

If you prefer manual control:

```bash
cd frontend
source .venv/bin/activate

# Set environment variables
export OPENAI_API_BASE_URL="http://localhost:8000/v1"
export OPENAI_API_KEY="local-api"

# Start Open WebUI
open-webui serve --host 0.0.0.0 --port 8080
```

## Available Services

Your local API provides:
- **Model**: `abu-dhabi-gov` - Specialized AI agent for Abu Dhabi government services
- **Endpoint**: `/v1/chat/completions` (OpenAI-compatible)
- **Models List**: `/v1/models`
- **Health Check**: `/v1/health`

## Usage Examples

Once connected, you can chat with the Abu Dhabi government assistant through Open WebUI. The AI agent can help with:

- Entry permits and visa services
- Driver's license services  
- Health services
- Utilities (water/electricity)
- Business registration
- Education services
- General government services

## Verification

To verify the connection is working:

1. **Check Model Availability**: In Open WebUI, look for "abu-dhabi-gov" in the model selector
2. **Test Chat**: Send a message like "Help me with Abu Dhabi government services"
3. **API Health**: Visit http://localhost:8000/v1/health to check server status

## Troubleshooting

### Common Issues:

1. **Model Not Appearing**: 
   - Ensure the API base URL ends with `/v1` (not `/v1/`)
   - Refresh the Open WebUI page
   - Check that both servers are running

2. **Connection Failed**:
   - Verify server is running: `curl http://localhost:8000/v1/models`
   - Check Open WebUI logs for error messages
   - Ensure no firewall blocking local connections

3. **API Key Errors**:
   - Use any dummy value for API key
   - Don't leave the API key field completely empty in some Open WebUI versions

### Testing Your Setup:

```bash
# Test server directly
curl http://localhost:8000/v1/models

# Test chat completion
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "abu-dhabi-gov", "messages": [{"role": "user", "content": "Hello"}]}'
```

## Architecture

```
┌─────────────────┐    HTTP/OpenAI API    ┌──────────────────┐
│   Open WebUI    │ ─────────────────────► │   Your Server    │
│  (Frontend)     │                        │  (Backend API)   │
│ localhost:8080  │                        │ localhost:8000   │
└─────────────────┘                        └──────────────────┘
                                                     │
                                                     ▼
                                           ┌──────────────────┐
                                           │   CrewAI Agent   │
                                           │ "abu-dhabi-gov"  │
                                           └──────────────────┘
```

## Next Steps

1. Start both servers if not already running
2. Configure Open WebUI using one of the methods above  
3. Begin chatting with the Abu Dhabi government assistant
4. Explore the various government services and information available

Your setup is now complete! The Abu Dhabi government AI agent is ready to assist users through the Open WebUI interface.