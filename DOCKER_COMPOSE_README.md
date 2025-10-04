# Docker Compose Setup - NB-2 Project

This directory contains a complete Docker Compose setup for the NB-2 project, providing a containerized environment for all services.

## 🏗️ Architecture Overview

The Docker Compose setup includes the following services:

### Core Services (Always Running)
- **Database** (`database`): PostgreSQL 16 with pgvector extension
- **Server** (`server`): FastAPI backend with standard chat API
- **Frontend** (`frontend`): Open WebUI for chat interface
- **Telemetry** (`telemetry`): Arize Phoenix for observability

### Optional Services (Profile-based)
- **Ollama** (`ollama`): Local LLM inference server
- **Testing** (`testing`): Ragas evaluation framework
- **Ingestion** (`ingestion`): Document processing pipeline

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Copy environment template
cp .env.template .env

# Edit the .env file with your API keys and settings
nano .env
```

### 2. Start Core Services

```bash
# Start all core services (database, server, frontend, telemetry)
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f
```

### 3. Access Services

- **Frontend (Open WebUI)**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Telemetry (Phoenix)**: http://localhost:6006
- **Database**: localhost:5432

## 📋 Service Management

### Core Services

```bash
# Start core services
docker-compose up -d

# Stop all services
docker-compose down

# Restart a specific service
docker-compose restart server

# View service logs
docker-compose logs -f server
```

### Optional Services (Profiles)

```bash
# Start with Ollama for local LLM inference
docker-compose --profile ollama up -d

# Run testing/evaluation
docker-compose --profile testing run --rm testing

# Run document ingestion
docker-compose --profile ingestion run --rm ingestion python src/ingest_documents.py

# Start all services including optional ones
docker-compose --profile ollama --profile testing --profile ingestion up -d
```

## 🔧 Configuration

### Environment Variables

Key environment variables in `.env`:

```bash
# Required API Keys
GEMINI_API_KEY=your-gemini-key
GEMINI_API_KEY=your-gemini-key

# Database Configuration
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=nb2

# Frontend Security
WEBUI_SECRET_KEY=your-secret-key

# Ollama Configuration
OLLAMA_BASE_URL=http://ollama:11434
```

### Service Ports

| Service | Port | Description |
|---------|------|-------------|
| Frontend | 3000 | Open WebUI Interface |
| Server | 8000 | Backend API |
| Database | 5432 | PostgreSQL Database |
| Telemetry | 6006 | Phoenix Observability |
| Ollama | 11434 | Local LLM Server |

### Volumes

Persistent data is stored in named Docker volumes:

- `nb2-postgres-data`: Database data
- `nb2-webui-data`: Frontend configuration and chat history
- `nb2-phoenix-data`: Telemetry data and traces
- `nb2-ollama-data`: Downloaded LLM models
- `nb2-testing-results`: Evaluation results
- `nb2-server-cache`: Backend cache data

## 🧪 Development Workflow

### Development Mode

```bash
# Start core services for development
docker-compose up -d database telemetry

# The server and frontend can be run locally for development
# while using containerized database and telemetry services
```

### Testing

```bash
# Run Ragas evaluation tests
docker-compose --profile testing run --rm testing

# Run specific test script
docker-compose --profile testing run --rm testing python custom_test.py

# View test results
docker-compose exec testing ls -la /app/results/
```

### Database Management

```bash
# Access database shell
docker-compose exec database psql -U admin -d nb2

# Create database backup
docker-compose exec database pg_dump -U admin nb2 > backup.sql

# Restore database from backup
docker-compose exec -T database psql -U admin nb2 < backup.sql
```

## 🔍 Troubleshooting

### Common Issues

1. **Port Conflicts**
   ```bash
   # Check what's using a port
   lsof -i :8000
   
   # Change port in docker-compose.yml or stop conflicting service
   ```

2. **Database Connection Issues**
   ```bash
   # Check database health
   docker-compose exec database pg_isready -U admin -d nb2
   
   # View database logs
   docker-compose logs database
   ```

3. **Service Dependencies**
   ```bash
   # Restart services in correct order
   docker-compose down
   docker-compose up -d database
   docker-compose up -d server
   docker-compose up -d frontend telemetry
   ```

### Health Checks

All services include health checks. Monitor them with:

```bash
# Check service health status
docker-compose ps

# View detailed health information
docker inspect $(docker-compose ps -q server) | grep -A 10 Health
```

### Logs and Debugging

```bash
# View all service logs
docker-compose logs

# Follow logs for specific service
docker-compose logs -f server

# View last 100 lines
docker-compose logs --tail=100 server

# Debug service startup issues
docker-compose up server  # (without -d flag)
```

## 🔐 Security Considerations

### Production Deployment

1. **Change Default Passwords**
   ```bash
   # Update .env file with strong passwords
   POSTGRES_PASSWORD=strong-random-password
   WEBUI_SECRET_KEY=strong-random-secret
   ```

2. **Network Security**
   ```yaml
   # Expose only necessary ports
   # Consider using a reverse proxy (nginx/traefik)
   ```

3. **API Key Security**
   ```bash
   # Use Docker secrets or external secret management
   # Never commit API keys to version control
   ```

### Backup Strategy

```bash
# Regular database backups
docker-compose exec database pg_dump -U admin nb2 | gzip > "backup_$(date +%Y%m%d_%H%M%S).sql.gz"

# Backup persistent volumes
docker run --rm -v nb2-postgres-data:/data -v $(pwd):/backup ubuntu tar czf /backup/postgres-data.tar.gz /data
```

## 🚀 Scaling and Performance

### Resource Allocation

```yaml
# Add resource limits to docker-compose.yml
services:
  server:
    deploy:
      resources:
        limits:
          memory: 2G
          cpus: '1.0'
```

### GPU Support for Ollama

```yaml
# Ollama service with GPU support
ollama:
  deploy:
    resources:
      reservations:
        devices:
          - driver: nvidia
            count: all
            capabilities: [gpu]
```

## 📚 Service Details

### Database Service
- **Image**: PostgreSQL 16 with pgvector
- **Purpose**: Store application data and vector embeddings
- **Health Check**: `pg_isready` command

### Server Service
- **Build**: Custom FastAPI application
- **Purpose**: API backend with standard chat endpoints
- **Health Check**: HTTP GET to `/health`

### Frontend Service
- **Build**: Open WebUI interface
- **Purpose**: Chat interface for LLM interaction
- **Health Check**: HTTP GET to root path

### Telemetry Service
- **Build**: Arize Phoenix observability
- **Purpose**: Monitor LLM application performance
- **Health Check**: HTTP GET to Phoenix UI

## 🔄 Updates and Maintenance

### Updating Services

```bash
# Pull latest images
docker-compose pull

# Rebuild custom services
docker-compose build --no-cache

# Restart with new images
docker-compose up -d
```

### Cleaning Up

```bash
# Remove stopped containers
docker-compose down

# Remove volumes (WARNING: deletes all data)
docker-compose down -v

# Clean up unused Docker resources
docker system prune -a
```

## 📖 Related Documentation

- [Server API Documentation](./server/README.md)
- [Frontend Setup Guide](./frontend/README.md)
- [Telemetry Configuration](./telemetry/README.md)
- [Testing Framework](./testing/README.md)

## 🆘 Support

For issues with the Docker Compose setup:

1. Check service logs: `docker-compose logs [service-name]`
2. Verify environment configuration: `cat .env`
3. Check service health: `docker-compose ps`
4. Review port conflicts: `docker-compose port [service-name]`

## 📝 License

This Docker Compose configuration is part of the NB-2 project. Refer to individual service documentation for specific licensing information.