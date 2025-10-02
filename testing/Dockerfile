# Testing Dockerfile for Ragas Evaluation
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy test scripts
COPY test.py .
COPY dataset.py .

# Create results directory
RUN mkdir -p /app/results

# Set environment variables
ENV PYTHONPATH=/app
ENV RESULTS_DIR=/app/results

# Default command (can be overridden)
CMD ["python", "test.py"]