# Server Service - FastAPI Backend with RAG

This directory contains the backend server for the NB-2 project, providing an advanced AI-powered API for Abu Dhabi government services using FastAPI, CrewAI agents, and a sophisticated RAG (Retrieval-Augmented Generation) system.

## 🏗️ Overview

The server implements a comprehensive AI backend featuring:

### Key Features

- 🤖 **Agentic Government Assistant**: AI agent with tool-based decision making
- �️ **Intelligent Tool Selection**: Dynamic choice between vector search and document analysis
- 📊 **Context Optimization**: Minimal context injection preserves conversation flow
- 🔄 **Adaptive System**: Agent learns and improves tool selection over time
- � **Cost Efficient**: Smart resource usage through targeted information retrieval
- ⚡ **High Performance**: Optimized for government document retrieval

## 📁 Project Structure

```
server/
├── Dockerfile              # Container configuration
├── main.py                 # Application entry point
├── app.py                  # FastAPI application setup
├── requirements.txt        # Python dependencies
├── README.md              # This documentation
├── rag.md                 # Comprehensive RAG implementation guide
├── config/                # Configuration files
├── controllers/           # API request controllers
├── handlers/              # Request handlers
│   ├── chat_handler.py    # Chat completion logic
│   ├── health_handler.py  # Health check implementations
│   └── models_handler.py  # Model management
├── models/                # Pydantic data models
│   ├── chat.py           # Chat completion models
│   └── requests.py       # Request/response schemas
├── routes/                # API route definitions
│   ├── chat_routes.py    # Chat endpoints
│   ├── health_routes.py  # Health check routes
│   └── models_routes.py  # Model management routes
├── services/              # Core business logic
│   ├── crewai_service.py # CrewAI agent orchestration
│   ├── rag_v1/           # Vector-based RAG implementation
│   │   ├── __init__.py
│   │   ├── rag_service.py              # Main RAG service
│   │   ├── rag_pipeline_service.py     # Processing pipeline
│   │   ├── database_service.py         # Vector database operations
│   │   ├── document_detection_service.py # Smart document selection
│   │   └── llm_configuration_service.py  # LLM setup and config
│   └── rag_v2/           # Full document RAG implementation
│       ├── __init__.py
│       └── full_document_service.py    # Complete document processing
└── tests/                # Test suites
    └── ...
```

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Start the server with dependencies
docker-compose up -d server

# Or start the full stack
docker-compose up -d

# Check server health
curl http://localhost:8000/health
```

### Manual Setup

```bash
# Navigate to server directory
cd server

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python main.py
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `GEMINI_API_KEY` | Required | Google Gemini API key |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama service endpoint |
| `DB_HOST` | `localhost` | PostgreSQL host |
| `DB_PORT` | `5432` | PostgreSQL port |
| `DB_USER` | `admin` | Database username |
| `DB_PASSWORD` | `admin` | Database password |
| `DB_NAME` | `postgres` | Database name |
| `PHOENIX_PROJECT_NAME` | `abu-dhabi-gov` | Phoenix project identifier |

### Model Configuration

The server supports multiple LLM providers:

```python
# Primary models for RAG operations
primary_llm = "gemini-flash-lite-latest"    # Document detection & reranking
secondary_llm = "gemini-flash-lite-latest"  # Response generation

# Embedding model for vector operations  
embedding_model = "nomic-embed-text:v1.5"  # 768-dimensional embeddings
```

## 🔍 Agentic RAG Implementation

The server features a sophisticated **agentic RAG system** where CrewAI agents use specialized tools for intelligent decision-making. For detailed information, see **[rag.md](./rag.md)**.

### Agent Tool Architecture

#### Vector Search Tool (Primary)
- **Usage**: Fast semantic search for quick lookups
- **Performance**: 1-4 second responses
- **Strategy**: Vector similarity + LLM reranking + context control
- **Efficiency**: Low token usage, cost-effective
- **Accuracy**: ~85% success rate

#### Document Reader Tool (Fallback)
- **Usage**: Deep document analysis for complex queries
- **Performance**: 10-30 second responses
- **Strategy**: Complete document context processing
- **Comprehensive**: High accuracy for detailed information
- **Accuracy**: ~95% success rate

### Agentic Decision Flow

```
User Query → CrewAI Agent → Tool Selection Decision
                    ↓
           Agent Reasoning:
           "Do I need fast lookup or deep analysis?"
                    ↓
    🔍 Vector Tool    OR    📄 Document Tool
    (Most queries)          (Complex procedures)
                    ↓
           🎯 Minimal Context Response
           (No context bloating)
```

### Context Control Benefits

- **No Context Bloating**: Agent selectively retrieves only necessary information
- **Clean Conversations**: Preserves natural chat flow without information dumps
- **Cost Optimization**: Efficient token usage through smart tool selection
- **Faster Responses**: Targeted retrieval reduces processing overhead
- **Better UX**: Users get concise, relevant answers without overwhelming context

## 📚 API Documentation

### Core Endpoints

#### 1. Health Check
```bash
GET /health
GET /v1/health
```

#### 2. Available Models
```bash
GET /v1/models
```
Returns the `abu-dhabi-gov` model information.

#### 3. Chat Completions (Standard API)
```bash
POST /v1/chat/completions
```

**Request Example:**
```json
{
  "model": "abu-dhabi-gov",
  "messages": [
    {"role": "user", "content": "How do I apply for a business license in Abu Dhabi?"}
  ],
  "stream": false
}
```

**Response Example:**
```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1699553600,
  "model": "abu-dhabi-gov",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "To apply for a business license in Abu Dhabi, you need to follow these steps...\n\n**Sources:**\n- Abu Dhabi Procurement Standards (Section 4.2)\n- Business Process Manual (Page 15-20)"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 150,
    "total_tokens": 175
  }
}
```

### Service Coverage

The Abu Dhabi Government AI Agent provides assistance with:

| Service Category | Examples |
|------------------|----------|
| **Entry Permits & Visas** | Tourist visas, entry requirements, document processing |
| **Driver's License** | Application process, requirements, renewals |
| **Health Services** | Hospital information, health card applications |
| **Utilities** | Water/electricity services, billing, connections |
| **Business Registration** | License applications, permits, compliance |
| **Education** | School enrollment, university admissions |
| **General Services** | Contact information, office locations, procedures |

## 🔧 Advanced Features

### Phoenix Observability

All agentic RAG operations are traced through Phoenix for comprehensive monitoring:

- **Real-time Agent Tracing**: Every tool selection and decision-making process
- **Performance Metrics**: Tool usage patterns, latency, and success rates
- **Quality Monitoring**: Response quality and context control effectiveness
- **Debug Capabilities**: Detailed agent reasoning and tool execution traces

Access Phoenix dashboard at: `http://localhost:6006`

### CrewAI Agent Architecture

```python
# The server uses CrewAI for intelligent tool orchestration
class AbuDhabiGovernmentAgent:
    """
    Specialized government services agent with:
    - Intelligent tool selection capabilities
    - Context control and optimization
    - Dynamic decision-making for information retrieval
    - Conversation flow preservation
    """
    
    tools = [
        VectorSearchTool(),      # Fast semantic search
        DocumentReaderTool(),    # Deep document analysis  
        MemoryTool(),           # Conversation context
        CitationTool()          # Source attribution
    ]
```

### Smart Tool Selection

The agent intelligently selects tools based on query analysis:

```python
agent_decision_matrix = {
    "simple_facts": VectorSearchTool,
    "procedures": VectorSearchTool, 
    "complex_analysis": DocumentReaderTool,
    "multi_document": DocumentReaderTool,
    "follow_up": MemoryTool + VectorSearchTool
}
```

## 🔍 Monitoring & Health

### Health Endpoints

```bash
# Basic health check
curl http://localhost:8000/health

# Standard API health check
curl http://localhost:8000/v1/health

# Detailed service status
curl http://localhost:8000/v1/models
```

### Performance Monitoring

```bash
# Monitor container resources
docker stats server

# Check application logs
docker-compose logs -f server

# Phoenix observability
open http://localhost:6006
```

### Database Health

```bash
# Test vector database connection
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "abu-dhabi-gov", "messages": [{"role": "user", "content": "test database connection"}]}'
```

## 🚨 Troubleshooting

### Common Issues

1. **Server Won't Start**
   ```bash
   # Check dependencies
   docker-compose ps database
   
   # Verify environment variables
   docker-compose config
   
   # Check logs
   docker-compose logs server
   ```

2. **RAG System Errors**
   ```bash
   # Verify database connection
   docker-compose exec database psql -U admin -d postgres -c "SELECT COUNT(*) FROM vectors_docling_nomic_embed;"
   
   # Check embedding service
   curl http://localhost:11434/api/tags
   
   # Test model availability
   curl http://localhost:8000/v1/models
   ```

3. **API Response Issues**
   ```bash
   # Check API key configuration
   echo $GEMINI_API_KEY
   
   # Verify model access
   curl -X POST http://localhost:8000/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{"model": "abu-dhabi-gov", "messages": [{"role": "user", "content": "hello"}]}'
   ```

4. **Performance Problems**
   ```bash
   # Monitor resource usage
   docker stats server
   
   # Check Phoenix traces
   open http://localhost:6006
   
   # Analyze query patterns
   docker-compose logs server | grep "Government Document Query"
   ```

### Debug Mode

```bash
# Enable debug logging
DEBUG=1 docker-compose up server

# Or with environment variable
docker-compose run -e DEBUG=1 server
```

## 📈 Performance Benchmarks

### Response Time Targets

| Query Type | RAG v1 Target | RAG v2 Target | Success Rate |
|------------|---------------|---------------|--------------|
| **Simple Lookup** | < 2s | < 15s | 95% |
| **Complex Procedures** | < 4s | < 25s | 90% |
| **Multi-document** | < 5s | < 30s | 85% |

### Resource Usage

| Metric | Normal Load | Peak Load | Limit |
|--------|-------------|-----------|-------|
| **CPU** | 20-40% | 60-80% | 90% |
| **Memory** | 200-400MB | 600MB-1GB | 2GB |
| **DB Connections** | 5-10 | 20-30 | 50 |

## 🔗 Integration

This server service integrates with:

- **[Frontend Service](../frontend/README.md)**: Provides AI chat interface via standard chat API
- **[Database Service](../database/README.md)**: Vector storage and retrieval for RAG operations
- **[Ingestion Service](../ingestion/README.md)**: Processes documents for RAG system
- **[Telemetry Service](../telemetry/README.md)**: Observability and monitoring via Phoenix
- **[Testing Service](../testing/README.md)**: Quality evaluation and performance testing

## 📚 Additional Resources

- **[RAG Implementation Guide](./rag.md)**: Comprehensive RAG system documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [CrewAI Framework](https://docs.crewai.com/)
- [Phoenix Observability](https://docs.arize.com/phoenix)
- [Gemini API Documentation](https://ai.google.dev/docs)

---

**Intelligent backend service for Abu Dhabi government AI assistance** 🤖

## 👨‍💻 Author

**Amin Ahmed Khan**
- 🔗 LinkedIn: [aa2kb](https://www.linkedin.com/in/aa2kb/)
- 💻 GitHub: [aa2kb](https://github.com/aa2kb)