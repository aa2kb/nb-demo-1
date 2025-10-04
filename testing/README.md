# Testing Service - Ragas Evaluation Framework

This directory contains the comprehensive testing and evaluation framework for the NB-2 project, utilizing the Ragas framework to assess the quality, accuracy, and performance of the RAG (Retrieval-Augmented Generation) system and Abu Dhabi government AI services.

## 🏗️ Overview

The testing service provides automated evaluation of the AI system using multiple metrics to ensure high-quality responses for Abu Dhabi government services. It evaluates both RAG approaches (vector-based and full-document) across various government document domains.

### Key Features

- 📊 **Multi-Metric Evaluation**: Faithfulness, factual correctness, and response quality assessment
- 🤖 **Dual LLM Support**: Gemini and Ollama evaluation models
- 📈 **Performance Benchmarking**: Response time and resource usage analysis
- 📋 **Comprehensive Dataset**: Abu Dhabi government service test cases
- 📁 **Multiple Export Formats**: JSON and CSV result exports
- 🔄 **Automated Testing**: Docker-based evaluation pipeline

## 📁 Contents

```
testing/
├── Dockerfile              # Container setup for testing environment
├── README.md               # This documentation
├── requirements.txt        # Python dependencies for Ragas framework
├── test.py                 # Main evaluation script
├── dataset.py              # Test dataset with Q&A pairs
└── results/                # Evaluation results and exports
    ├── evaluation_results.json
    ├── evaluation_results.csv
    └── performance_metrics.json
```

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Run evaluation tests
docker-compose run --rm testing

# Or use the interactive startup script
./start.sh
# Choose option 5: "Run evaluation tests"

# View results
cat testing/results/evaluation_results.json
```

### Manual Setup

```bash
# Navigate to testing directory
cd testing

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run evaluation
python test.py
```

## 📊 Evaluation Metrics

The testing framework uses Ragas metrics specifically designed for RAG system evaluation:

### 1. Faithfulness
- **Purpose**: Measures factual consistency between generated answers and retrieved contexts
- **Range**: 0.0 to 1.0 (higher is better)
- **Interpretation**: How well the AI sticks to factual information from source documents

### 2. Factual Correctness
- **Purpose**: Evaluates the accuracy of factual statements in responses
- **Range**: 0.0 to 1.0 (higher is better)
- **Interpretation**: Whether the AI provides correct information about government procedures

### 3. Simple Criteria Score
- **Purpose**: Assesses overall response quality against custom criteria
- **Range**: 0.0 to 1.0 (higher is better)
- **Interpretation**: General quality and usefulness of responses

### 4. Aspect Critic
- **Purpose**: Evaluates specific aspects of government service responses
- **Range**: 0.0 to 1.0 (higher is better)
- **Interpretation**: Domain-specific quality for Abu Dhabi government services

## 🎯 Test Dataset

### Abu Dhabi Government Services Coverage

The test dataset covers comprehensive government service domains:

| Domain | Questions | Example Topics |
|--------|-----------|----------------|
| **Procurement Standards** | 5 | Objectives, transparency, purchase orders |
| **Information Security** | 5 | NESA standards, risk assessment, lifecycle |
| **Procurement (Ariba)** | 5 | SAP alignment, exemptions, benefits |
| **Business Processes** | 5 | R2P process, category classification |
| **HR Bylaws** | 5 | Employment regulations, policies |

### Sample Test Cases

```python
test_examples = {
    "procurement": {
        "question": "What is the objective of the Abu Dhabi Procurement Standards?",
        "expected_context": "Clear rules for procurement across government entities ensuring fairness, transparency, and efficiency",
        "evaluation_criteria": ["accuracy", "completeness", "policy_compliance"]
    },
    "security": {
        "question": "What is the purpose of the UAE Information Assurance Standards?",
        "expected_context": "Raise minimum protection level of information assets and systems across implementing entities",
        "evaluation_criteria": ["technical_accuracy", "regulatory_compliance"]
    }
}
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DEFAULT_LLM_PROVIDER` | `gemini` | Evaluation LLM provider |
| `DEFAULT_LLM_MODEL` | `gemini-flash-lite-latest` | Evaluation model name |
| `GEMINI_API_KEY` | Required | Google Gemini API key |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama service endpoint |
| `SERVER_BASE_URL` | `http://localhost:8000` | NB-2 server API endpoint |

### LLM Provider Setup

#### Using Gemini (Recommended)
```bash
# Set API key
export GEMINI_API_KEY=your-gemini-api-key

# Configure provider
export DEFAULT_LLM_PROVIDER=gemini
export DEFAULT_LLM_MODEL=gemini-flash-lite-latest
```

#### Using Ollama (Local)
```bash
# Ensure Ollama is running
ollama pull llama2  # or your preferred model

# Configure provider
export DEFAULT_LLM_PROVIDER=ollama
export DEFAULT_LLM_MODEL=llama2
export OLLAMA_BASE_URL=http://localhost:11434
```

## 📈 Performance Testing

### Response Time Analysis

The testing framework measures:

```python
performance_metrics = {
    "avg_response_time": 2.45,        # seconds
    "p95_response_time": 4.12,        # 95th percentile
    "p99_response_time": 7.89,        # 99th percentile
    "timeout_rate": 0.02,             # 2% timeout rate
    "success_rate": 0.95              # 95% success rate
}
```

### Resource Utilization

```python
resource_metrics = {
    "avg_tokens_per_query": 3200,     # Token consumption
    "avg_cost_per_query": 0.0045,     # USD cost estimate
    "memory_usage_mb": 150,           # Peak memory usage
    "cpu_utilization": 0.35           # CPU usage fraction
}
```

## 📋 Evaluation Results

### Sample Output

```json
{
  "timestamp": "2024-10-04T15:30:00Z",
  "evaluation_summary": {
    "Faithfulness": 0.847,
    "FactualCorrectness": 0.892,
    "SimpleCriteriaScore": 0.923,
    "AspectCritic": 0.889
  },
  "performance_metrics": {
    "avg_response_time": 2.45,
    "total_questions": 20,
    "successful_responses": 19,
    "timeout_responses": 1
  },
  "detailed_results": [
    {
      "question": "What is the objective of Abu Dhabi Procurement Standards?",
      "response": "The Abu Dhabi Procurement Standards aim to...",
      "faithfulness": 0.89,
      "factual_correctness": 0.92,
      "response_time": 2.1
    }
  ]
}
```

### CSV Export Format

```csv
Question,Response,Faithfulness,FactualCorrectness,SimpleCriteriaScore,AspectCritic,ResponseTime
"What is the objective...",0.89,0.92,0.95,0.88,2.1
"Who issues the standards...",0.85,0.88,0.91,0.86,1.9
```

## 🔍 Quality Analysis

### Benchmarking Targets

| Metric | Minimum Target | Good Performance | Excellent |
|--------|----------------|------------------|-----------|
| **Faithfulness** | > 0.70 | > 0.85 | > 0.90 |
| **Factual Correctness** | > 0.75 | > 0.88 | > 0.93 |
| **Response Quality** | > 0.80 | > 0.90 | > 0.95 |
| **Response Time** | < 5s | < 3s | < 2s |

### Domain-Specific Analysis

```python
domain_performance = {
    "procurement_standards": {
        "avg_faithfulness": 0.89,
        "avg_factual_correctness": 0.92,
        "complexity_score": "medium"
    },
    "information_security": {
        "avg_faithfulness": 0.82,
        "avg_factual_correctness": 0.87,
        "complexity_score": "high"
    },
    "hr_bylaws": {
        "avg_faithfulness": 0.91,
        "avg_factual_correctness": 0.94,
        "complexity_score": "low"
    }
}
```

## 🚨 Troubleshooting

### Common Issues

1. **Server Connection Failed**
   ```bash
   # Verify server is running
   curl http://localhost:8000/v1/health
   
   # Check server logs
   docker-compose logs server
   
   # Restart server if needed
   docker-compose restart server
   ```

2. **Evaluation LLM Issues**
   ```bash
   # For Gemini
   echo $GEMINI_API_KEY  # Verify API key
   
   # For Ollama
   curl http://localhost:11434/api/tags  # Check models
   ollama pull llama2  # Pull required model
   ```

3. **Timeout Errors**
   ```bash
   # Increase timeout in test.py
   # timeout=180  # 3 minutes
   
   # Or test with smaller dataset
   python test.py --limit 5
   ```

4. **Memory Issues**
   ```bash
   # Monitor resource usage
   docker stats testing
   
   # Reduce batch size
   # Process questions individually
   ```

### Debug Mode

```bash
# Run with debug logging
DEBUG=1 docker-compose run testing

# Manual debugging
docker-compose run --rm testing python test.py --debug
```

## 📊 Continuous Integration

### Automated Testing Pipeline

```bash
# Daily evaluation run
cron: "0 2 * * *"  # 2 AM daily
command: docker-compose run --rm testing

# Weekly comprehensive report
cron: "0 1 * * 0"  # Sunday 1 AM
command: docker-compose run --rm testing python test.py --full-report
```

### Quality Gates

```python
quality_gates = {
    "faithfulness_threshold": 0.75,
    "factual_correctness_threshold": 0.80,
    "response_time_threshold": 5.0,  # seconds
    "success_rate_threshold": 0.90
}

# Fail CI if any threshold not met
def check_quality_gates(results):
    return all([
        results["Faithfulness"] >= quality_gates["faithfulness_threshold"],
        results["FactualCorrectness"] >= quality_gates["factual_correctness_threshold"],
        results["avg_response_time"] <= quality_gates["response_time_threshold"],
        results["success_rate"] >= quality_gates["success_rate_threshold"]
    ])
```

## 🔧 Advanced Configuration

### Custom Evaluation Metrics

```python
# Add domain-specific evaluation
def evaluate_government_service_quality(query, response, context):
    """Custom metric for government service evaluation"""
    criteria = {
        "policy_compliance": check_policy_alignment(response),
        "procedural_accuracy": verify_procedures(response),
        "citation_quality": validate_sources(response),
        "language_clarity": assess_readability(response)
    }
    return sum(criteria.values()) / len(criteria)

# Register custom metric
from ragas.metrics import BaseMetric
class GovernmentServiceQuality(BaseMetric):
    name = "government_service_quality"
    # Implementation...
```

### Test Dataset Expansion

```python
# Add new test categories
new_test_categories = {
    "visa_services": [
        "How do I apply for a tourist visa to Abu Dhabi?",
        "What documents are required for visa application?"
    ],
    "business_licensing": [
        "What are the steps to register a business in Abu Dhabi?",
        "How long does business registration take?"
    ]
}
```

## 🔗 Integration

This testing service integrates with:

- **[Server Service](../server/README.md)**: Tests API endpoints and RAG system performance
- **[Database Service](../database/README.md)**: Validates vector search and retrieval quality
- **[Telemetry Service](../telemetry/README.md)**: Monitors evaluation metrics in Phoenix
- **[Frontend Service](../frontend/README.md)**: Tests end-to-end user interaction flows

## 📚 Additional Resources

- [Ragas Documentation](https://docs.ragas.io/)
- [Ragas GitHub Repository](https://github.com/explodinggradients/ragas)
- [RAG Evaluation Best Practices](https://docs.ragas.io/en/stable/concepts/metrics/)
- [LLM Evaluation Metrics](https://docs.ragas.io/en/stable/concepts/metrics/faithfulness/)

---

**Comprehensive evaluation framework for Abu Dhabi government AI services** 🧪

## 👨‍💻 Author

**Amin Ahmed Khan**
- 🔗 LinkedIn: [aa2kb](https://www.linkedin.com/in/aa2kb/)
- 💻 GitHub: [aa2kb](https://github.com/aa2kb)