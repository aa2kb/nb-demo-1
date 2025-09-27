# Frontend - Open WebUI

This directory contains the frontend setup for the project using [Open WebUI](https://github.com/open-webui/open-webui), a user-friendly web interface for Large Language Models (LLMs).

## Overview

Open WebUI is a feature-rich, self-hosted WebUI designed to operate entirely offline. It supports various LLM runners, including Ollama and OpenAI-compatible APIs, making it perfect for interacting with your custom API server.

## Prerequisites

- Python 3.11 (required for Open WebUI compatibility)
- Your backend server running (see `../server/` directory)

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

## Configuration

### Connecting to Your Backend API

If you have a custom OpenAI-compatible API running (like the one in `../server/`), you can configure Open WebUI to use it:

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
- 🔗 **Multiple Model Support**: Works with Ollama, OpenAI API, and custom endpoints
- 💬 **Chat Management**: Organize conversations and chat history
- 🛠️ **Customization**: Themes, plugins, and extensive configuration options
- 📱 **Mobile Friendly**: Responsive design for all devices
- 🔒 **Privacy First**: Runs entirely offline with your data

## Integration with Backend

This frontend is designed to work seamlessly with the backend server located in `../server/`. The backend provides:

- OpenAI-compatible API endpoints (`/v1/chat/completions`, `/v1/models`)
- Integration with Ollama for local model inference
- Custom model management and routing

## Troubleshooting

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

### Logs and Debugging

```bash
# Run with debug logging
DEBUG=1 open-webui serve

# Check Open WebUI version
open-webui --version
```

## File Structure

```
frontend/
├── .venv/                 # Python virtual environment
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── data/                 # Open WebUI data (created on first run)
    ├── config.json
    ├── chats/
    └── models/
```

## Development

### Updating Open WebUI

```bash
# Activate virtual environment
source .venv/bin/activate

# Update to latest version
pip install --upgrade open-webui

# Update requirements.txt
pip freeze > requirements.txt
```

### Custom Configuration

Open WebUI stores its configuration in the `data/` directory. You can:

- Modify `data/config.json` for custom settings
- Add custom themes in `data/themes/`
- Configure model presets in `data/models/`

## Related Documentation

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Backend API Documentation](../server/README.md)

## License

Open WebUI is licensed under the MIT License. See the [original repository](https://github.com/open-webui/open-webui) for details.