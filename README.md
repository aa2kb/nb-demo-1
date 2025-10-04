# Abu Dhabi Gov Agent - Complete AI Stack

A comprehensive, containerized AI application stack featuring RAG (Retrieval-Augmented Generation), LLM evaluation, and observability. Built with modern tools including FastAPI, Open WebUI, Ragas evaluation framework, and Arize Phoenix telemetry.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                Abu Dhabi Gov Agent Stack                    │
├─────────────────────────────────────────────────────────────┤
│  Frontend (Port 3000)     │  Telemetry (Port 6006)          │
│  ┌─────────────────┐      │  ┌─────────────────────────┐    │
│  │   Open WebUI    │      │  │    Arize Phoenix        │    │
│  │   Chat Interface│◄─────┤  │    Observability        │    │
│  └─────────────────┘      │  └─────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│  Backend API (Port 8000)  │  Testing (On-demand)            │
│  ┌─────────────────┐      │  ┌─────────────────────────┐    │
│  │   FastAPI       │      │  │    Ragas Framework      │    │
│  │   RAG Endpoints │      │  │    Evaluation Suite     │    │
│  └─────────────────┘      │  └─────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│  Database (Port 5432)     │  Ingestion Pipeline             │
│  ┌─────────────────┐      │  ┌─────────────────────────┐    │
│  │  PostgreSQL     │      │  │  Document Processing    │    │
│  │  + pgvector     │◄─────┤  │  PDF → Chunks → Vectors │    │
│  └─────────────────┘      │  └─────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│  Ollama (Port 11434)                                        │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Local LLM Server (Optional)              │  │
│  │         Provides local inference capabilities         │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- (Optional) API key for Google Gemini

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd abu-dhabi-gov-agent

# Copy environment template
cp .env.template .env

# Edit with your API keys (optional for basic setup)
nano .env
```

### 2. Start the Stack

```bash
# Option 1: Use the interactive startup script
./start.sh

# Option 2: Direct Docker Compose commands
docker-compose up -d

# Option 3: Include Ollama for local LLM inference
docker-compose --profile ollama up -d
```

### 3. Access Services

- **Chat Interface**: http://localhost:3000 (Open WebUI)
- **API Documentation**: http://localhost:8000/docs
- **Observability**: http://localhost:6006 (Phoenix)
- **Backend API**: http://localhost:8000

## 📁 Project Structure

```
abu-dhabi-gov-agent/
├── 🐳 docker-compose.yml              # Main orchestration file
├── 🔧 .env.template                   # Environment variables template
├── 🚀 start.sh                        # Interactive startup script
├── 📚 DOCKER_COMPOSE_README.md        # Detailed Docker setup guide
│
├── 📊 database/                       # PostgreSQL + pgvector
│   └── Dockerfile
│
├── 🖥️ server/                         # FastAPI backend
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── ... (API implementation)
│
├── 🌐 frontend/                       # Open WebUI interface
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
│
├── 📈 telemetry/                      # Arize Phoenix observability
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
│
├── 🧪 testing/                        # Ragas evaluation framework
│   ├── Dockerfile
│   ├── test.py                        # Main evaluation script
│   ├── dataset.py                     # Test dataset
│   └── requirements.txt
│
└── 📝 ingestion/                      # Document processing
    ├── Dockerfile
    ├── src/
    └── docs/
```

## 🔧 Configuration

### Environment Variables

Key settings in `.env` file:

```bash
# API Keys (optional but recommended)
GEMINI_API_KEY=your-gemini-key

# Database Configuration
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=abu_dhabi_gov_agent

# Security
WEBUI_SECRET_KEY=your-secret-key

# Ollama Configuration
OLLAMA_BASE_URL=http://ollama:11434
```

### Service Ports

| Service | Port | Purpose |
|---------|------|---------|
| Frontend | 3000 | Chat interface (Open WebUI) |
| Backend | 8000 | API server |
| Database | 5432 | PostgreSQL |
| Telemetry | 6006 | Phoenix observability |
| Ollama | 11434 | Local LLM server |

## 🧪 Evaluation & Testing

### Ragas Evaluation Framework

The project includes a comprehensive evaluation setup using Ragas:

```bash
# Run evaluation tests
./start.sh
# Choose option 5: "Run evaluation tests"

# Or directly with Docker Compose
docker-compose --profile testing run --rm testing
```

**Evaluation Metrics:**
- **Faithfulness**: Measures factual consistency
- **AspectCritic**: Custom quality evaluation
- **SimpleCriteriaScore**: Response quality scoring
- **FactualCorrectness**: Answer accuracy validation

**Results Export:**
- JSON format: `testing/results/evaluation_results.json`
- CSV format: `testing/results/evaluation_results.csv`

### Sample Evaluation Output

```json
{
  "Faithfulness": 0.178,
  "AspectCritic": 1.0,
  "SimpleCriteriaScore": 1.0,
  "FactualCorrectness": 0.317,
  "avg_response_time": 2.45
}
```

## 📊 Observability

### Arize Phoenix Integration

Monitor your LLM applications with comprehensive observability:

- **Real-time Traces**: See every API call and response
- **Performance Metrics**: Track latency and token usage
- **Quality Metrics**: Monitor response quality over time
- **Debug Tools**: Identify and fix issues quickly

Access Phoenix at: http://localhost:6006

## 🎯 Core Features

### 1. Chat Interface (Open WebUI)
- Clean, responsive web interface
- Multi-model support (Gemini, Ollama)
- Chat history and conversation management
- Mobile-friendly design
- Plugin and theme support

### 2. API Backend (FastAPI)
- Standard chat completion endpoints
- Async request processing
- Comprehensive error handling
- Interactive API documentation
- Health monitoring endpoints

### 3. Evaluation Framework (Ragas)
- Multi-metric evaluation suite
- Dual LLM provider support (Gemini/Ollama)
- Automated testing pipeline
- JSON and CSV result export
- Custom metric configuration

### 4. Observability (Phoenix)
- LLM application monitoring
- Trace visualization
- Performance analytics
- Quality tracking
- Debug capabilities

## 🚧 Development

### Local Development

```bash
# Start only database and telemetry for local dev
docker-compose up -d database telemetry

# Run server locally for development
cd server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py

# Run frontend locally
cd frontend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
open-webui serve
```

### Adding Custom Evaluation Metrics

Edit `testing/test.py` to add new Ragas metrics:

```python
# Add new metrics to the evaluator
metrics = [
    faithfulness,
    AspectCritic(
        name="custom_aspect",
        definition="Your custom evaluation criteria"
    ),
    # Add more metrics here
]
```

### Custom API Endpoints

Add new routes in `server/routes/`:

```python
# server/routes/custom_routes.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/custom-endpoint")
async def custom_function():
    return {"message": "Custom response"}
```

## 🔍 Troubleshooting

### Common Issues

1. **Port Conflicts**
   ```bash
   # Check what's using a port
   lsof -i :8000
   
   # Stop conflicting services or change ports in docker-compose.yml
   ```

2. **API Key Issues**
   ```bash
   # Verify API keys in .env file
   cat .env | grep API_KEY
   
   # Test Gemini API connectivity
   curl -H "Authorization: Bearer $GEMINI_API_KEY" https://generativelanguage.googleapis.com/v1/models
   ```

3. **Service Health**
   ```bash
   # Check service status
   docker-compose ps
   
   # View service logs
   docker-compose logs -f [service-name]
   ```

### Debugging Commands

```bash
# View all service logs
docker-compose logs

# Check service health
docker-compose exec server curl http://localhost:8000/health

# Access database
docker-compose exec database psql -U admin -d abu_dhabi_gov_agent

# Restart specific service
docker-compose restart server
```

## 📚 Documentation

- [Docker Compose Setup Guide](DOCKER_COMPOSE_README.md)
- [Backend API Documentation](server/README.md)
- [Frontend Setup Guide](frontend/README.md)
- [Telemetry Configuration](telemetry/README.md)
- [Testing Framework](testing/README.md)

## 🔐 Security

### Production Considerations

1. **Environment Variables**
   ```bash
   # Use strong passwords
   POSTGRES_PASSWORD=strong-random-password
   WEBUI_SECRET_KEY=strong-random-secret
   ```

2. **API Key Security**
   - Never commit API keys to version control
   - Use Docker secrets in production
   - Rotate keys regularly

3. **Network Security**
   - Use reverse proxy (nginx/traefik) in production
   - Configure CORS properly
   - Enable HTTPS

### Backup Strategy

```bash
# Database backup
docker-compose exec database pg_dump -U admin abu_dhabi_gov_agent > backup.sql

# Volume backup
docker run --rm -v abu-dhabi-gov-agent-postgres-data:/data -v $(pwd):/backup ubuntu tar czf /backup/postgres-data.tar.gz /data
```

## 🚀 Deployment

### Production Deployment

1. **Update Environment**
   ```bash
   # Set production values in .env
   PRODUCTION=true
   DEBUG=false
   ```

2. **Resource Limits**
   ```yaml
   # Add to docker-compose.yml
   deploy:
     resources:
       limits:
         memory: 2G
         cpus: '1.0'
   ```

3. **Reverse Proxy**
   ```nginx
   # nginx configuration
   server {
     listen 80;
     server_name your-domain.com;
     
     location / {
       proxy_pass http://localhost:3000;
     }
     
     location /api {
       proxy_pass http://localhost:8000;
     }
   }
   ```

## 📄 License

This project is open source. See individual component documentation for specific licensing information.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For issues and questions:

1. Check the [troubleshooting section](#-troubleshooting)
2. Review service logs: `docker-compose logs [service]`
3. Check the [documentation](#-documentation)
4. Open an issue on GitHub

---

**Built with ❤️ using modern AI and container technologies**

## 👨‍💻 Author

**Amin Ahmed Khan**
- 🔗 LinkedIn: [aa2kb](https://www.linkedin.com/in/aa2kb/)
- 💻 GitHub: [aa2kb](https://github.com/aa2kb)