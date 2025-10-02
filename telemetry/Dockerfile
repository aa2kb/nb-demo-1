# Telemetry Dockerfile for Arize Phoenix
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

# Create Phoenix data directory
RUN mkdir -p /app/phoenix_data

# Expose port
EXPOSE 6006

# Set environment variables
ENV PHOENIX_HOST=0.0.0.0
ENV PHOENIX_PORT=6006
ENV PHOENIX_WORKING_DIR=/app/phoenix_data

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:6006/ || exit 1

# Start Phoenix server
CMD ["phoenix", "serve", "--host", "0.0.0.0", "--port", "6006"]