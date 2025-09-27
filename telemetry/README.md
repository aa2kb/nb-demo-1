# Telemetry - Arize Phoenix

This directory contains the telemetry setup for the project using [Arize Phoenix](https://phoenix.arize.com/), an open-source observability platform for machine learning and LLM applications.

## Overview

Arize Phoenix is a comprehensive observability tool that provides:
- Real-time monitoring and debugging for ML/LLM applications
- Trace visualization and analysis
- Performance metrics and anomaly detection
- Integration with popular ML frameworks and LLM providers

## Prerequisites

- Python 3.8+ (recommended: Python 3.11+)
- Your backend server running (see `../server/` directory)

## Setup Instructions

### 1. Quick Start

The easiest way to get started is using the provided start script:

```bash
# Navigate to telemetry directory
cd telemetry

# Run the start script (creates venv, installs dependencies, starts Phoenix)
./start.sh
```

### 2. Manual Setup

If you prefer to set up manually:

```bash
# Navigate to telemetry directory
cd telemetry

# Create virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Phoenix server
phoenix serve
```

### 3. Access Phoenix UI

Once started, Phoenix will be available at: `http://localhost:6006`

## Configuration

### Environment Variables

You can customize Phoenix behavior using environment variables:

```bash
# Set custom host and port
export PHOENIX_HOST=0.0.0.0
export PHOENIX_PORT=6006

# Set working directory (optional)
export PHOENIX_WORKING_DIR=./phoenix_data

# Start with custom settings
phoenix serve
```

### Integration with Your Application

To instrument your Python application with Phoenix:

```python
import phoenix as px

# Start a Phoenix session
session = px.launch_app()

# For OpenAI integration
from phoenix.trace.openai import OpenAIInstrumentor
OpenAIInstrumentor().instrument()

# For LangChain integration  
from phoenix.trace.langchain import LangChainInstrumentor
LangChainInstrumentor().instrument()

# Your application code here...
```

## Features

Phoenix provides:

- 🔍 **Trace Analysis**: Visualize and debug LLM application traces
- 📊 **Performance Monitoring**: Track latency, token usage, and costs  
- 🎯 **Evaluation Tools**: Compare model outputs and measure quality
- 🔗 **Multi-Framework Support**: Works with OpenAI, LangChain, LlamaIndex, and more
- 📈 **Real-time Dashboard**: Live monitoring of your application performance
- 🛠️ **Debugging Tools**: Identify issues and bottlenecks in your LLM pipeline

## Integration with Backend

This telemetry setup is designed to work with the backend server located in `../server/`. To instrument your backend:

1. Install Phoenix in your backend environment:
   ```bash
   pip install arize-phoenix
   ```

2. Add instrumentation to your backend code:
   ```python
   # In your main.py or app.py
   import phoenix as px
   from phoenix.trace.openai import OpenAIInstrumentor
   
   # Launch Phoenix (connects to running Phoenix server)
   px.launch_app(run_in_notebook=False)
   
   # Instrument OpenAI calls
   OpenAIInstrumentor().instrument()
   ```

3. Your API calls will automatically be traced and visible in the Phoenix UI

## Monitoring Different Components

### OpenAI API Calls
```python
from phoenix.trace.openai import OpenAIInstrumentor
OpenAIInstrumentor().instrument()
```

### LangChain Applications
```python
from phoenix.trace.langchain import LangChainInstrumentor
LangChainInstrumentor().instrument()
```

### Custom Traces
```python
import phoenix as px
from phoenix.trace import trace

@trace("custom_function")
def my_function():
    # Your code here
    pass
```

## Troubleshooting

### Common Issues

1. **Port Already in Use**:
   ```bash
   # Check what's using port 6006
   lsof -i :6006
   
   # Use a different port
   PHOENIX_PORT=6007 phoenix serve
   ```

2. **Virtual Environment Issues**:
   ```bash
   # Remove and recreate virtual environment
   rm -rf .venv
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Missing Dependencies**:
   ```bash
   # Update pip and reinstall
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Debugging Phoenix

```bash
# Run Phoenix with debug logging
PHOENIX_LOG_LEVEL=DEBUG phoenix serve

# Check Phoenix version
python -c "import phoenix; print(phoenix.__version__)"
```

## File Structure

```
telemetry/
├── .venv/                 # Python virtual environment
├── requirements.txt       # Python dependencies
├── start.sh              # Startup script
├── README.md             # This file
└── phoenix_data/         # Phoenix data directory (created on first run)
    ├── traces/
    └── evaluations/
```

## Usage Examples

### Basic Monitoring Setup

```python
# basic_monitoring.py
import phoenix as px
from phoenix.trace.openai import OpenAIInstrumentor

# Connect to Phoenix server
session = px.launch_app(run_in_notebook=False)

# Instrument OpenAI
OpenAIInstrumentor().instrument()

# Now all OpenAI calls will be traced
import openai
client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, world!"}]
)
```

### Custom Evaluation

```python
# evaluation.py
import phoenix as px

# Define evaluation criteria
def evaluate_response(input_text, output_text):
    # Your evaluation logic
    return {"accuracy": 0.95, "relevance": 0.88}

# Log evaluations to Phoenix
px.log_evaluations(
    dataframe=eval_df,
    evaluation_name="response_quality"
)
```

## Development

### Updating Dependencies

```bash
# Activate virtual environment
source .venv/bin/activate

# Update Phoenix to latest version
pip install --upgrade arize-phoenix

# Update requirements.txt
pip freeze > requirements.txt
```

### Adding Custom Metrics

You can extend Phoenix with custom metrics and evaluations:

```python
import phoenix as px

# Custom span attributes
px.trace.add_span_attribute("custom_metric", value)

# Custom evaluations
px.trace.add_evaluation("quality_score", score)
```

## Related Documentation

- [Arize Phoenix Documentation](https://docs.arize.com/phoenix/)
- [Phoenix GitHub Repository](https://github.com/Arize-ai/phoenix)
- [Backend API Documentation](../server/README.md)
- [Frontend Documentation](../frontend/README.md)

## License

Arize Phoenix is licensed under the Apache License 2.0. See the [original repository](https://github.com/Arize-ai/phoenix) for details.