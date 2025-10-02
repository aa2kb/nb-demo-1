# Frontend Dockerfile for Open WebUI
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

# Create data directory
RUN mkdir -p /app/data

# Expose port
EXPOSE 3000

# Set environment variables
ENV HOST=0.0.0.0
ENV PORT=3000
ENV DATA_DIR=/app/data

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/ || exit 1

# Start Open WebUI
CMD ["open-webui", "serve", "--host", "0.0.0.0", "--port", "3000"]