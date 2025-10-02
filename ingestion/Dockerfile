# Ingestion Dockerfile for Document Processing
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for PDF processing
RUN apt-get update && apt-get install -y \
    curl \
    poppler-utils \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Create basic requirements.txt for ingestion
RUN echo "pypdf2==3.0.1\npandas==2.3.3\nrequests==2.32.5\npsycopg2-binary==2.9.9" > requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY docs/ ./docs/

# Create data directory
RUN mkdir -p /app/data

# Set environment variables
ENV PYTHONPATH=/app

# Default command
CMD ["python", "-c", "print('Ingestion service ready. Run specific scripts as needed.')"]