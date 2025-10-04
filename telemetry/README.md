# Telemetry Service - Arize Phoenix Observability

This directory contains the telemetry and observability setup for the NB-2 project using [Arize Phoenix](https://phoenix.arize.com/), an open-source observability platform designed specifically for LLM and ML applications.

## 🏗️ Overview

Arize Phoenix provides comprehensive observability for the NB-2 AI stack, offering real-time monitoring, tracing, and debugging capabilities for the RAG system and AI agent interactions.

### Key Features

- 🔍 **LLM Tracing**: Complete visibility into AI agent conversations and RAG operations
- 📊 **Performance Monitoring**: Real-time metrics for latency, token usage, and costs
- 🎯 **Quality Evaluation**: Model output analysis and quality scoring
- 🔗 **Multi-Framework Support**: Integrated with CrewAI, LlamaIndex, and Gemini
- 📈 **Interactive Dashboard**: Real-time visualization of system performance
- 🛠️ **Debugging Tools**: Identify bottlenecks and optimize RAG performance

## 📁 Contents

```
telemetry/
├── Dockerfile              # Phoenix container configuration
├── README.md               # This documentation
├── requirements.txt        # Python dependencies
├── start.sh               # Service startup script
└── phoenix_data/          # Phoenix data storage (created at runtime)
    ├── traces/            # LLM interaction traces
    ├── evaluations/       # Quality evaluation data
    └── projects/          # Project-specific data
```

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Start telemetry service
docker-compose up -d telemetry

# Or start with the full stack
docker-compose up -d

# Access Phoenix dashboard
open http://localhost:6006
```

### Manual Setup

```bash
# Navigate to telemetry directory
cd telemetry

# Run the startup script
./start.sh

# Or manual setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
phoenix serve
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PHOENIX_HOST` | `0.0.0.0` | Phoenix server host |
| `PHOENIX_PORT` | `6006` | Phoenix server port |
| `PHOENIX_WORKING_DIR` | `./phoenix_data` | Data storage directory |
| `PHOENIX_PROJECT_NAME` | `abu-dhabi-gov` | Project identifier |

### Docker Configuration

The Phoenix service is configured for the NB-2 stack:

```yaml
# docker-compose.yml snippet
telemetry:
  build: ./telemetry
  ports:
    - "6006:6006"
  volumes:
    - phoenix-data:/app/phoenix_data
  environment:
    - PHOENIX_PROJECT_NAME=abu-dhabi-gov
```

## 📊 Monitoring Capabilities

### RAG System Tracing

Phoenix provides detailed visibility into the dual RAG system:

#### RAG v1 (Vector-Based) Tracing
- **Document Detection**: LLM reasoning for document selection
- **Vector Retrieval**: Similarity search performance and results
- **Reranking Process**: LLM-based relevance scoring
- **Response Generation**: Final answer synthesis with citations

#### RAG v2 (Full Document) Tracing  
- **Document Loading**: File access and content processing
- **Context Assembly**: Large context preparation
- **LLM Processing**: Token usage and generation metrics
- **Response Quality**: Comprehensive answer evaluation

### CrewAI Agent Monitoring

Complete visibility into the Abu Dhabi Government AI agent:

```
Phoenix Dashboard View:
├── Agent Conversations
│   ├── User Queries
│   ├── Tool Selections (RAG v1 vs v2)
│   ├── Document Retrievals
│   └── Final Responses
├── Performance Metrics  
│   ├── Response Times
│   ├── Token Consumption
│   ├── Success/Failure Rates
│   └── Cost Analysis
└── Quality Metrics
    ├── Response Relevance
    ├── Citation Accuracy
    ├── User Satisfaction
    └── Error Analysis
```

## 🔍 Dashboard Features

### Real-time Monitoring

Access Phoenix at `http://localhost:6006` to view:

1. **Live Traces**: Real-time LLM interactions and RAG operations
2. **Performance Dashboard**: Latency, throughput, and resource usage
3. **Error Analysis**: Failed requests and debugging information
4. **Token Analytics**: Usage patterns and cost optimization insights

### Key Metrics Tracked

| Metric Category | Specific Metrics | Use Case |
|-----------------|------------------|----------|
| **Performance** | Response time, token/sec, requests/min | System optimization |
| **Quality** | Response relevance, citation accuracy | Model improvement |
| **Usage** | Token consumption, API costs | Resource planning |
| **Reliability** | Success rates, error patterns | System stability |

## 🔧 Integration with NB-2 Services

### Server Integration

The telemetry service is deeply integrated with the server's RAG system:

```python
# In server/app.py
from phoenix.otel import register

tracer_provider = register(
    project_name="abu-dhabi-gov",
    auto_instrument=True
)

# Automatic instrumentation of:
# - CrewAI agent interactions
# - RAG pipeline operations  
# - LLM API calls (Gemini)
# - Database queries (PostgreSQL)
```

### RAG Pipeline Tracing

```python
# In server/services/rag_v1/rag_pipeline_service.py
class RAGPipelineService:
    def __init__(self):
        self.phoenix_client = Client()
        
    def _generate_with_phoenix(self, context, question, doc_name, doc_filename, llm):
        """Phoenix manages prompts and traces all operations"""
        prompt = self.phoenix_client.prompts.get(prompt_identifier="document_processing")
        # All LLM calls automatically traced
```

### Prompt Management

Phoenix manages versioned prompts for consistent RAG operations:

- **Document Processing Prompts**: For individual document responses
- **Answer Combination Prompts**: For multi-document synthesis
- **Quality Evaluation Prompts**: For response assessment

## 📈 Performance Analysis

### RAG Performance Comparison

Phoenix enables detailed comparison between RAG approaches:

```
Performance Dashboard:
┌─────────────────────────────────────────────┐
│ RAG v1 (Vector)    │ RAG v2 (Full Doc)      │
├─────────────────────────────────────────────┤
│ Avg Response: 2.3s │ Avg Response: 18.7s    │
│ Token Usage: 3.2K  │ Token Usage: 127K      │
│ Success Rate: 87%  │ Success Rate: 94%      │
│ Cost/Query: $0.002 │ Cost/Query: $0.031     │
└─────────────────────────────────────────────┘
```

### Quality Metrics

Phoenix tracks response quality through:

- **Faithfulness**: Accuracy of information retrieval
- **Relevance**: Query-response alignment
- **Completeness**: Coverage of user questions
- **Citation Quality**: Source attribution accuracy

## 🚨 Alerting & Monitoring

### Performance Alerts

Configure alerts for:

```python
alert_thresholds = {
    "response_time_p95": 10.0,      # 95th percentile > 10s
    "error_rate": 0.05,             # Error rate > 5%
    "token_usage_spike": 2.0,       # 2x normal usage
    "database_latency": 1.0         # DB queries > 1s
}
```

### Health Monitoring

```bash
# Check Phoenix health
curl http://localhost:6006/health

# Monitor service status
docker-compose ps telemetry

# View real-time metrics
curl http://localhost:6006/api/v1/projects/abu-dhabi-gov/metrics
```

## 🔧 Advanced Configuration

### Custom Evaluations

Create domain-specific evaluations for government services:

```python
import phoenix as px

def evaluate_government_response(query, response):
    """Custom evaluation for Abu Dhabi government responses"""
    return {
        "policy_accuracy": check_policy_compliance(response),
        "procedural_completeness": verify_procedures(response),
        "citation_validity": validate_sources(response),
        "language_clarity": assess_clarity(response)
    }

# Register evaluation
px.register_evaluation("government_service_quality", evaluate_government_response)
```

### Data Retention

Configure data retention policies:

```python
# Phoenix data retention configuration
phoenix_config = {
    "trace_retention_days": 30,      # Keep traces for 30 days
    "evaluation_retention_days": 90, # Keep evaluations for 90 days
    "aggregation_intervals": ["1h", "1d", "1w"]
}
```

## 🚨 Troubleshooting

### Common Issues

1. **Phoenix Not Starting**
   ```bash
   # Check port availability
   lsof -i :6006
   
   # Use different port
   PHOENIX_PORT=6007 docker-compose up telemetry
   
   # Check container logs
   docker-compose logs telemetry
   ```

2. **No Traces Appearing**
   ```bash
   # Verify server instrumentation
   curl http://localhost:8000/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{"model": "abu-dhabi-gov", "messages": [{"role": "user", "content": "test"}]}'
   
   # Check Phoenix connection
   docker-compose exec telemetry phoenix --version
   ```

3. **Performance Issues**
   ```bash
   # Monitor resource usage
   docker stats telemetry
   
   # Clear old data
   docker volume rm nb2-phoenix-data
   docker-compose up -d telemetry
   ```

4. **Data Persistence Problems**
   ```bash
   # Verify volume mounting
   docker volume inspect nb2-phoenix-data
   
   # Check data directory permissions
   docker-compose exec telemetry ls -la /app/phoenix_data
   ```

### Debug Mode

```bash
# Enable debug logging
DEBUG=1 docker-compose up telemetry

# Manual debugging
docker-compose exec telemetry phoenix serve --log-level DEBUG
```

## 📊 Data Export & Backup

### Export Traces

```bash
# Export trace data
docker-compose exec telemetry phoenix export \
  --project abu-dhabi-gov \
  --format json \
  --output /app/phoenix_data/exports/traces_$(date +%Y%m%d).json

# Copy to host
docker cp $(docker-compose ps -q telemetry):/app/phoenix_data/exports/ ./exports/
```

### Backup Data

```bash
# Backup Phoenix data volume
docker run --rm \
  -v nb2-phoenix-data:/data \
  -v $(pwd):/backup \
  ubuntu tar czf /backup/phoenix-data-$(date +%Y%m%d_%H%M%S).tar.gz /data
```

## 🔗 Integration

This telemetry service integrates with:

- **[Server Service](../server/README.md)**: Monitors RAG operations and API responses
- **[Frontend Service](../frontend/README.md)**: Tracks user interactions and response quality
- **[Testing Service](../testing/README.md)**: Evaluates model performance and accuracy
- **[Database Service](../database/README.md)**: Monitors query performance and vector operations

## 📚 Additional Resources

- [Arize Phoenix Documentation](https://docs.arize.com/phoenix/)
- [Phoenix GitHub Repository](https://github.com/Arize-ai/phoenix)
- [LLM Observability Best Practices](https://docs.arize.com/phoenix/concepts/llm-observability)
- [RAG System Monitoring](https://docs.arize.com/phoenix/how-to/evals/retrieval-augmented-generation-rag)

---

**Comprehensive observability for Abu Dhabi government AI services** 📊