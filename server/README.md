# CrewAI Agent with FastAPI

A simple project that combines CrewAI agents with FastAPI to create a research agent accessible through REST endpoints.

## Project Structure

```
nb-2/
├── main.py              # Application entry point (runs uvicorn server)
├── server.py            # FastAPI application and routes
├── crewai_agent.py      # CrewAI agent implementation (using Ollama)
├── test_ollama.py       # Test script for Ollama connectivity
├── pyproject.toml       # Project configuration and dependencies
├── requirements.txt     # Python dependencies (alternative)
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Features

- **Simple Research Agent**: A CrewAI agent that can research basic topics
- **FastAPI Integration**: RESTful API endpoints to interact with the agent
- **Health Checks**: Basic monitoring endpoints
- **Error Handling**: Comprehensive error handling and validation
- **Environment Configuration**: Easy setup with environment variables

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

**Option 1: Using pyproject.toml (Recommended)**
```bash
pip install -e .
```

**Option 2: Using requirements.txt**
```bash
pip install -r requirements.txt
```

**For development (includes testing and linting tools):**
```bash
pip install -e ".[dev]"
```

### 4. Environment Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. **Install and Setup Ollama** (if not already done):
```bash
# Install Ollama (macOS)
curl -fsSL https://ollama.com/install.sh | sh

# Pull Mistral 7B model
ollama pull mistral:7b

# Start Ollama service (if not running)
ollama serve
```

3. **Verify Ollama is running**:
```bash
curl http://localhost:11434/api/tags
```

**Note**: This project uses Ollama with Mistral 7B model running locally. No external API keys required!

## Running the Application

### Start the FastAPI Server

```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

### Interactive API Documentation

FastAPI automatically generates interactive documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### 1. Root Endpoint
- **GET** `/`
- Returns basic API information

### 2. Health Check
- **GET** `/health`
- Returns service health status

### 3. Agent Information
- **GET** `/agent-info`
- Returns information about the research agent

### 4. Research Topic
- **POST** `/research`
- Researches a given topic using the CrewAI agent

**Request Body:**
```json
{
  "topic": "python programming"
}
```

**Response:**
```json
{
  "status": "success",
  "topic": "python programming",
  "result": "Research results here..."
}
```

## Usage Examples

### Using curl

```bash
# Health check
curl http://localhost:8000/health

# Get agent info
curl http://localhost:8000/agent-info

# Research a topic
curl -X POST http://localhost:8000/research \
  -H "Content-Type: application/json" \
  -d '{"topic": "artificial intelligence"}'
```

### Using Python requests

```python
import requests

# Research a topic
response = requests.post(
    "http://localhost:8000/research",
    json={"topic": "crewai"}
)
print(response.json())
```

## Development

### Project Dependencies

- **FastAPI**: Web framework for building APIs
- **CrewAI**: Framework for AI agent teams
- **Uvicorn**: ASGI server for FastAPI
- **Pydantic**: Data validation and serialization
- **python-dotenv**: Environment variable management
- **Ollama**: Local LLM inference server (external dependency)

### Development Tools (Optional)

- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Code linting
- **mypy**: Type checking

Install development dependencies with: `pip install -e ".[dev]"`

### Extending the Agent

To add more capabilities to the agent:

1. Create new tools in `crewai_agent.py`
2. Add them to the agent's tools list
3. Create new endpoints in `main.py`

### Adding More Agents

To add additional agents:

1. Define new agents in `crewai_agent.py`
2. Create tasks for collaboration
3. Add corresponding API endpoints

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure virtual environment is activated and dependencies are installed
2. **Ollama Connection**: Ensure Ollama is running on `http://localhost:11434`
3. **Model Not Found**: Make sure `mistral:7b` is pulled with `ollama pull mistral:7b`
4. **Port Conflicts**: Change the port in `main.py` if 8000 is already in use

### Ollama Specific Troubleshooting

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Check available models
ollama list

# Test Mistral model directly
curl http://localhost:11434/api/generate -d '{
  "model": "mistral:7b",
  "prompt": "Hello, how are you?",
  "stream": false
}'
```

### Logs

The application provides detailed logs. Check the console output for debugging information.

## License

This project is for educational purposes. Please check the licenses of individual dependencies.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Note**: This is a basic implementation for learning purposes. For production use, consider adding authentication, rate limiting, proper logging, and error monitoring.