# Frontend Service - Open WebUI

This directory contains the frontend service for the NB-2 project using [Open WebUI](https://github.com/open-webui/open-webui), providing a modern, intuitive chat interface for interacting with Abu Dhabi government AI services.

## 🏗️ Overview

Open WebUI is a feature-rich, self-hosted web interface designed for Large Language Models (LLMs). It provides:

- **Clean Chat Interface**: Modern, responsive UI similar to ChatGPT
- **Multi-Model Support**: Works with Gemini, Ollama, and custom endpoints
- **Offline Capability**: Runs entirely offline with local models
- **Rich Features**: Chat history, file uploads, model switching, and more

### Key Features

- 🎨 **Intuitive Design**: Clean, responsive interface optimized for conversations
- 🔗 **API Compatibility**: Standard API integration
- 💬 **Chat Management**: Conversation history and organization
- 🛠️ **Customization**: Themes, plugins, and extensive configuration
- 📱 **Mobile Friendly**: Responsive design for all devices
- 🔒 **Privacy First**: All data stays local

## 📁 Contents

```
frontend/
├── Dockerfile              # Open WebUI container setup
├── README.md               # This documentation  
├── INTEGRATION_GUIDE.md    # Detailed API integration guide
├── requirements.txt        # Python dependencies
├── start.sh               # Service startup script
└── .venv/                 # Python virtual environment (created on setup)
```

## 🐳 Docker Configuration

### Container Setup
- **Base Image**: Open WebUI official image
- **Python Version**: 3.11 (required for compatibility)
- **Port**: 3000 (mapped to host)

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `API_BASE_URL` | `http://server:8000/v1` | Backend API endpoint |
| `API_KEY` | `local-api` | API authentication (dummy value) |
| `WEBUI_SECRET_KEY` | Set in `.env` | Session security key |

## Prerequisites

- Python 3.11 (required for Open WebUI compatibility)
- Your backend server running (see `../server/` directory)

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Start the frontend service
docker-compose up -d frontend

# Or start the full stack
docker-compose up -d

# Access the interface
open http://localhost:3000
```

### Manual Setup

```bash
# Navigate to frontend directory
cd frontend

# Create virtual environment with Python 3.11
python3.11 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Open WebUI
open-webui serve
```

## 🔧 Configuration

### Backend Integration

The frontend automatically connects to the backend API server:

- **API Endpoint**: `http://server:8000/v1` (Docker) or `http://localhost:8000/v1` (manual)
- **Available Model**: `abu-dhabi-gov` - Abu Dhabi government services AI
- **Authentication**: No API key required for local development

### Custom Configuration

```bash
# Set custom host and port
export HOST=0.0.0.0
export PORT=3000

# Set data directory (optional)
export DATA_DIR=./data

# Start with custom settings
open-webui serve
```

## Setup Instructions

### 1. Virtual Environment Setup

The frontend uses a separate Python 3.11 virtual environment to ensure compatibility:

```bash
# Navigate to frontend directory
cd frontend

# Create virtual environment with Python 3.11
python3.11 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Verify Python version
python --version  # Should show Python 3.11.x
```

### 2. Install Dependencies

```bash
# Install Open WebUI and dependencies
pip install -r requirements.txt
```

### 3. Start Open WebUI

```bash
# Start the Open WebUI server
open-webui serve
```

By default, Open WebUI will be available at: `http://localhost:3000`

## 💬 Usage

### Abu Dhabi Government Services

The frontend provides access to Abu Dhabi government AI services through an intuitive chat interface:

**Available Services:**
- 📋 Entry permits and visa services
- 🚗 Driver's license services  
- 🏥 Health services and information
- ⚡ Utilities (water/electricity) services
- 🏢 Business registration and licensing
- 🎓 Education services and schools
- 📞 General government services and contacts

### Example Conversations

```
User: "How do I apply for a driver's license in Abu Dhabi?"
AI: Provides step-by-step guidance with required documents and procedures

User: "What are the business registration requirements?"
AI: Details the complete business setup process with relevant forms and fees

User: "Help me find information about school enrollment"
AI: Guides through education system options and enrollment procedures
```

### Advanced Features

- **Chat History**: All conversations are saved and searchable
- **File Uploads**: Share documents for analysis (when supported)
- **Model Selection**: Switch between available AI models
- **Export Chats**: Download conversation history
- **Dark/Light Mode**: Toggle interface themes

## 🔧 Advanced Configuration

### Connecting to Your Backend API

If you have a custom chat API running (like the one in `../server/`), you can configure Open WebUI to use it:

1. Open Open WebUI in your browser
2. Go to Settings → Connections
3. Add your API endpoint (e.g., `http://localhost:8000/v1`)
4. Configure any required API keys if needed

### Environment Variables

You can customize Open WebUI behavior using environment variables:

```bash
# Set custom host and port
export HOST=0.0.0.0
export PORT=3000

# Set data directory (optional)
export DATA_DIR=./data

# Start with custom settings
open-webui serve
```

## Features

Open WebUI provides:

- 🎨 **Intuitive Interface**: Clean, responsive web interface
- 🔗 **Multiple Model Support**: Works with Ollama, Gemini, and custom endpoints
- 💬 **Chat Management**: Organize conversations and chat history
- 🛠️ **Customization**: Themes, plugins, and extensive configuration options
- 📱 **Mobile Friendly**: Responsive design for all devices
- 🔒 **Privacy First**: Runs entirely offline with your data

## Integration with Backend

This frontend is designed to work seamlessly with the backend server located in `../server/`. The backend provides:

- Standard chat API endpoints (`/v1/chat/completions`, `/v1/models`)
- Integration with Ollama for local model inference
- Custom model management and routing

### API Connection Setup

For detailed API integration instructions, see [INTEGRATION_GUIDE.md](./INTEGRATION_GUIDE.md).

#### Quick Setup:
1. Open Open WebUI at `http://localhost:3000`
2. Go to Settings → Connections
3. Add API endpoint: `http://localhost:8000/v1`
4. Select the `abu-dhabi-gov` model
5. Start chatting with the AI assistant

### Environment Configuration

```bash
# Frontend service configuration
API_BASE_URL=http://server:8000/v1
API_KEY=local-api
WEBUI_SECRET_KEY=your-secret-key

# Optional customization
HOST=0.0.0.0
PORT=3000
DATA_DIR=./data
```

## 🔍 Monitoring & Health

### Health Checks

```bash
# Check frontend status
curl http://localhost:3000/health

# Verify API connection
curl http://localhost:3000/api/v1/models

# Check container status
docker-compose ps frontend
```

### Performance Monitoring

```bash
# View frontend logs
docker-compose logs -f frontend

# Monitor resource usage
docker stats frontend

# Check active connections
netstat -an | grep :3000
```

## 🚨 Troubleshooting

### Common Issues

1. **Python Version Error**: 
   - Ensure you're using Python 3.11: `python --version`
   - Recreate virtual environment if needed

2. **Port Conflicts**:
   - Change the port: `PORT=3001 open-webui serve`
   - Check what's running on port 3000: `lsof -i :3000`

3. **API Connection Issues**:
   - Ensure your backend server is running
   - Check the API endpoint URL in Open WebUI settings
   - Verify CORS settings if accessing from different origins

### Common Issues

1. **Service Won't Start**:
   ```bash
   # Check port availability
   lsof -i :3000
   
   # Restart container
   docker-compose restart frontend
   
   # Check logs for errors
   docker-compose logs frontend
   ```

2. **API Connection Failed**:
   ```bash
   # Verify backend is running
   curl http://localhost:8000/v1/models
   
   # Check network connectivity
   docker-compose exec frontend curl http://server:8000/v1/models
   
   # Restart both services
   docker-compose restart server frontend
   ```

3. **Model Not Available**:
   - Ensure backend server is running and healthy
   - Check API endpoint configuration in Open WebUI settings
   - Verify the `abu-dhabi-gov` model is listed at `/v1/models`

4. **Performance Issues**:
   ```bash
   # Check container resources
   docker stats frontend
   
   # Monitor response times
   curl -w "@curl-format.txt" -o /dev/null -s http://localhost:3000
   ```

### Debug Mode

```bash
# Run with debug logging
DEBUG=1 docker-compose up frontend

# Or for manual setup
DEBUG=1 open-webui serve
```

## 🔧 Development

### Local Development

```bash
# Start only backend services
docker-compose up -d server database

# Run frontend locally for development
cd frontend
source .venv/bin/activate
open-webui serve --host 0.0.0.0 --port 3000
```

### Updating Open WebUI

```bash
# Activate virtual environment
source .venv/bin/activate

# Update to latest version
pip install --upgrade open-webui

# Update requirements.txt
pip freeze > requirements.txt

# Rebuild Docker image
docker-compose build frontend
```

### Custom Themes & Plugins

```bash
# Open WebUI data directory structure
frontend/data/
├── config.json          # Main configuration
├── chats/              # Chat history storage
├── models/             # Model configurations
├── uploads/            # File upload storage
└── themes/             # Custom themes (if any)
```

## 📊 Data & Storage

### Data Persistence

Open WebUI stores data in the container's `/app/backend/data` directory:

- **Chat History**: All conversations and metadata
- **User Settings**: Preferences and configurations
- **Uploaded Files**: Documents and attachments
- **Model Configs**: Custom model settings

### Data Export

```bash
# Export chat data
docker-compose exec frontend cat /app/backend/data/chats.db > chats_backup.db

# Backup entire data directory
docker run --rm \
  -v nb2-frontend-data:/data \
  -v $(pwd):/backup \
  ubuntu tar czf /backup/frontend-data-$(date +%Y%m%d_%H%M%S).tar.gz /data
```

## 🔗 Integration

This frontend service integrates with:

- **[Server Service](../server/README.md)**: Backend API providing AI models and RAG functionality
- **[Database Service](../database/README.md)**: Stores conversation history and user data
- **[Telemetry Service](../telemetry/README.md)**: Monitors frontend performance and usage

## 📚 Additional Resources

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [API Integration Guide](./INTEGRATION_GUIDE.md)
- [Backend API Documentation](../server/README.md)

---

**Modern AI chat interface for Abu Dhabi government services** 💬

## 👨‍💻 Author

**Amin Ahmed Khan**
- 🔗 LinkedIn: [aa2kb](https://www.linkedin.com/in/aa2kb/)
- 💻 GitHub: [aa2kb](https://github.com/aa2kb)