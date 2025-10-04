# Document Ingestion Service

This service handles the complete document processing pipeline for the NB-2 RAG system, transforming PDF documents into searchable vector embeddings stored in PostgreSQL with pgvector.

## 🏗️ Overview

The ingestion service provides a comprehensive document processing workflow:

- **PDF Processing**: Advanced document parsing using Docling
- **Text Extraction**: Structured content extraction with formatting preservation
- **Chunking**: Intelligent text segmentation for optimal retrieval
- **Embeddings**: Vector generation using state-of-the-art models
- **Storage**: Efficient vector storage in PostgreSQL with metadata

### Key Features

- 📄 **Multi-format Support**: PDF processing with OCR capabilities
- 🧠 **Smart Chunking**: Context-aware text segmentation
- 🔍 **Vector Embeddings**: High-quality semantic representations
- 📊 **Metadata Preservation**: Document structure and context retention
- 🗄️ **Hybrid Storage**: Vector + full-text search capabilities

## 📁 Contents

```
ingestion/
├── Dockerfile              # Container setup for ingestion service
├── README.md               # This documentation
├── requirements.txt        # Python dependencies
├── src/                    # Source code and processing scripts
│   ├── 1_setup.py         # Database and environment setup
│   ├── 2_parse.py         # PDF parsing using Docling
│   ├── 3_chunking.py      # Text chunking and segmentation
│   ├── 4_insertion_hybrid_based.py    # Hybrid search insertion
│   ├── 5_insertion_simple_based.py    # Simple vector insertion
│   └── 6_insertion_semantic_based.py  # Semantic vector insertion
├── docs/                   # Source PDF documents
│   ├── Abu Dhabi Procurement Standards.PDF
│   ├── HR Bylaws.pdf
│   ├── Information Security.pdf
│   ├── Procurement Manual (Ariba Aligned).PDF
│   └── Procurement Manual (Business Process).PDF
├── markdown/              # Processed markdown files
│   ├── Abu Dhabi Procurement Standards.md
│   ├── HR Bylaws.md
│   ├── Information Security.md
│   ├── Procurement Manual (Ariba Aligned).md
│   └── Procurement Manual (Business Process).md
├── chunks/                # Chunked text data (JSON format)
│   ├── Abu Dhabi Procurement Standards_chunks.json
│   ├── HR Bylaws_chunks.json
│   ├── Information Security_chunks.json
│   ├── Procurement Manual (Ariba Aligned)_chunks.json
│   └── Procurement Manual (Business Process)_chunks.json
└── vectors/               # Generated vector embeddings
    ├── Abu Dhabi Procurement Standards_vectors.json
    ├── HR Bylaws_vectors.json
    ├── Information Security_vectors.json
    ├── Procurement Manual (Ariba Aligned)_vectors.json
    └── Procurement Manual (Business Process)_vectors.json
```

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Start ingestion service with dependencies
docker-compose up -d database
docker-compose run --rm ingestion

# Or run specific processing steps
docker-compose run --rm ingestion python src/2_parse.py
docker-compose run --rm ingestion python src/3_chunking.py
```

### Manual Setup

```bash
# Navigate to ingestion directory
cd ingestion

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run processing pipeline
python src/1_setup.py      # Setup database
python src/2_parse.py      # Parse PDFs to markdown
python src/3_chunking.py   # Create text chunks
python src/4_insertion_hybrid_based.py  # Insert with hybrid search
```

## Document Ingestion CLI

## ⚙️ Processing Pipeline

### 1. Document Setup (`1_setup.py`)
- Initializes PostgreSQL database connection
- Creates necessary tables and indexes
- Sets up pgvector extension
- Validates environment configuration

### 2. PDF Parsing (`2_parse.py`)
- Extracts text and structure from PDF documents
- Uses Docling for advanced document understanding
- Preserves formatting and document hierarchy
- Outputs clean markdown representations

### 3. Text Chunking (`3_chunking.py`)
- Segments documents into optimal chunk sizes
- Maintains context and semantic coherence
- Configurable chunk size and overlap parameters
- Preserves document metadata in each chunk

### 4. Vector Insertion (Multiple Strategies)

#### Hybrid Search (`4_insertion_hybrid_based.py`)
- Combines vector similarity with full-text search
- Optimal for complex queries requiring both semantic and keyword matching
- Best performance for government document retrieval

#### Simple Vector (`5_insertion_simple_based.py`)
- Pure vector similarity search
- Fastest insertion and retrieval
- Suitable for semantic-only queries

#### Semantic Vector (`6_insertion_semantic_based.py`)
- Enhanced semantic understanding
- Advanced context preservation
- Optimized for complex document relationships

## A powerful CLI application for processing PDF documents and storing them as vectors in PostgreSQL using Ollama embeddings, Docling for document processing, and LlamaIndex for RAG methodology.

## 📊 Document Coverage

### Abu Dhabi Government Documents

The service processes comprehensive government documentation:

| Document | Type | Content |
|----------|------|---------|
| **Abu Dhabi Procurement Standards** | Policy | Procurement guidelines and standards |
| **HR Bylaws** | Legal | Human resources regulations |
| **Information Security** | Technical | Cybersecurity policies and procedures |
| **Procurement Manual (Ariba Aligned)** | Operational | Ariba-specific procurement processes |
| **Procurement Manual (Business Process)** | Operational | General business process guidelines |

### Processing Statistics

- **Total Documents**: 5 government publications
- **Average Document Size**: ~50-150 pages
- **Chunk Size**: 1024 characters with 200 character overlap
- **Embedding Dimensions**: 768 (nomic-embed-text:v1.5)
- **Vector Index Type**: IVFFlat with cosine similarity

## Features

### Advanced Features

- **PDF Processing**: Extract and structure content from PDF documents using Docling
- **Smart Embeddings**: Generate high-quality embeddings using Ollama's nomic-embed-text:v1.5
- **Hybrid Storage**: Store embeddings in PostgreSQL with pgvector for optimal retrieval
- **Rich CLI**: Interactive command-line interface with progress indicators and statistics
- **Incremental Processing**: Skip already processed documents or force re-processing
- **Environment Config**: Flexible configuration management with sensible defaults
- **Metadata Preservation**: Maintain document structure and context information
- **Multiple Insertion Strategies**: Choose optimal vector storage approach

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DB_HOST` | `localhost` | PostgreSQL host |
| `DB_PORT` | `5432` | PostgreSQL port |
| `DB_USER` | `admin` | Database username |
| `DB_PASSWORD` | `admin` | Database password |
| `DB_NAME` | `postgres` | Database name |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama API endpoint |
| `EMBEDDING_MODEL` | `nomic-embed-text:v1.5` | Embedding model name |
| `EMBEDDING_DIM` | `768` | Embedding dimensions |
| `CHUNK_SIZE` | `1024` | Text chunk size |
| `CHUNK_OVERLAP` | `200` | Chunk overlap size |

### Model Requirements

```bash
# Pull required embedding model
ollama pull nomic-embed-text:v1.5

# Verify model is available
ollama list | grep nomic-embed-text
```

## Prerequisites

### System Requirements

1. **PostgreSQL** with pgvector extension
   - Host: localhost:5432 (or configured endpoint)
   - Database: postgres (or custom name)
   - User: admin with full permissions

2. **Ollama** with embedding model
   - Service: localhost:11434
   - Model: nomic-embed-text:v1.5 (768 dimensions)
   ```bash
   ollama pull nomic-embed-text:v1.5
   ```

3. **Python Environment**
   - Python 3.8+ with virtual environment
   - Required packages in requirements.txt

## 🔍 Monitoring & Validation

### Processing Verification

```bash
# Check database contents
docker-compose exec database psql -U admin -d postgres -c "
SELECT 
    table_name,
    pg_size_pretty(pg_total_relation_size(table_name)) as size
FROM information_schema.tables 
WHERE table_schema = 'public' AND table_name LIKE '%vector%';"

# Verify embeddings
docker-compose exec database psql -U admin -d postgres -c "
SELECT 
    COUNT(*) as total_vectors,
    AVG(array_length(embedding::float[], 1)) as avg_dimensions
FROM vectors_docling_nomic_embed;"
```

### Quality Checks

```bash
# Test similarity search
docker-compose exec database psql -U admin -d postgres -c "
SELECT 
    metadata_->>'document_title' as document,
    substring(text, 1, 100) as preview,
    1 - (embedding <=> (SELECT embedding FROM vectors_docling_nomic_embed LIMIT 1)) as similarity
FROM vectors_docling_nomic_embed
ORDER BY embedding <=> (SELECT embedding FROM vectors_docling_nomic_embed LIMIT 1)
LIMIT 5;"
```

## Installation

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy environment configuration:
   ```bash
   cp .env.example .env
   ```

4. Edit `.env` if you need to change default settings

**Note**: Always ensure your virtual environment is activated before running any commands:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Usage

### Basic Commands

**Important**: Make sure your virtual environment is activated before running any commands:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

1. **Test all connections**:
   ```bash
   python src/main.py test
   ```

2. **Ingest documents from a directory**:
   ```bash
   python src/main.py ingest docs/
   ```

3. **Show statistics**:
   ```bash
   python src/main.py stats
   ```

### Advanced Options

- **Force re-processing** existing documents:
  ```bash
  python src/main.py ingest docs/ --force
  ```

- **Dry run** to see what would be processed:
  ```bash
  python src/main.py ingest docs/ --dry-run
  ```

- **Delete a specific document**:
  ```bash
  python src/main.py delete <document_id>
  ```

- **Custom log level**:
  ```bash
  python src/main.py --log-level DEBUG ingest docs/
  ```

### Example Workflow

1. First, test your setup:
   ```bash
   python src/main.py test
   ```

2. Process documents in the docs folder:
   ```bash
   python src/main.py ingest docs/
   ```

3. Check what was stored:
   ```bash
   python src/main.py stats
   ```

## Architecture

### Components

- **Document Processor** (`document_processor.py`): PDF processing using Docling
- **Embedding Service** (`embedding_service.py`): Text-to-vector conversion using Ollama
- **Vector Store Manager** (`vector_store.py`): PostgreSQL vector storage with LlamaIndex
- **Database Manager** (`database.py`): PostgreSQL connection and setup
- **CLI Interface** (`cli.py`): Command-line interface with Rich formatting

### Data Flow

1. **PDF Processing**: Docling extracts structured content from PDFs
2. **Text Chunking**: Content is split into manageable chunks (1024 chars with 200 overlap)
3. **Embedding Generation**: Ollama generates 384-dimensional vectors for each chunk
4. **Vector Storage**: LlamaIndex stores vectors in PostgreSQL with metadata
5. **Retrieval**: Vectors can be queried for similarity search (RAG functionality)

### Database Schema

The application creates a `document_chunks` table with:
- `id`: Primary key
- `document_id`: Unique document identifier
- `document_name`: Original file name
- `chunk_index`: Position of chunk within document
- `content`: Text content of the chunk
- `embedding`: 384-dimensional vector (pgvector)
- `metadata`: JSON metadata about the document and chunk
- `created_at`: Timestamp

## Configuration

All configuration is handled through environment variables (see `.env.example`):

- **Database**: Connection details for PostgreSQL
- **Ollama**: Host and model configuration
- **Processing**: Chunk size and overlap settings
- **Logging**: Log level configuration

## 🚨 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   ```bash
   # Verify PostgreSQL is running
   docker-compose ps database
   
   # Test connection
   docker-compose exec database psql -U admin -d postgres -c "SELECT version();"
   
   # Check logs
   docker-compose logs database
   ```

2. **Ollama Model Not Found**
   ```bash
   # List available models
   ollama list
   
   # Pull required model
   ollama pull nomic-embed-text:v1.5
   
   # Test model
   curl http://localhost:11434/api/embeddings -d '{"model": "nomic-embed-text:v1.5", "prompt": "test"}'
   ```

3. **Memory Issues During Processing**
   ```bash
   # Monitor resource usage
   docker stats
   
   # Increase Docker memory limits
   # Or process documents in smaller batches
   ```

4. **Incomplete Processing**
   ```bash
   # Check processing logs
   docker-compose logs ingestion
   
   # Restart specific stage
   docker-compose run --rm ingestion python src/3_chunking.py
   ```

### Performance Optimization

```bash
# Monitor processing speed
time docker-compose run --rm ingestion python src/4_insertion_hybrid_based.py

# Database performance tuning
docker-compose exec database psql -U admin -d postgres -c "
ANALYZE vectors_docling_nomic_embed;
VACUUM vectors_docling_nomic_embed;"

# Index optimization
docker-compose exec database psql -U admin -d postgres -c "
REINDEX INDEX vectors_docling_nomic_embed_embedding_idx;"
```

### Legacy Troubleshooting

1. **Database connection fails**:
   - Ensure PostgreSQL is running on localhost:5432
   - Check username/password in `.env`
   - Ensure pgvector extension is available

2. **Embedding model not found**:
   - Run `ollama pull nomic-embed-text:v1.5` (updated model)
   - Check if Ollama is running on localhost:11434

3. **PDF processing errors**:
   - Ensure PDF files are not corrupted
   - Check file permissions
   - Some PDFs may have content extraction limitations

### Debug Logging

```bash
# Enable debug mode
python src/main.py --log-level DEBUG test

# Docker debug
docker-compose run --rm -e DEBUG=1 ingestion
```

## 📈 Performance Metrics

### Processing Benchmarks

| Stage | Time (Est.) | Output |
|-------|-------------|---------|
| **Setup** | 5-10 seconds | Database tables created |
| **Parsing** | 2-5 minutes | 5 markdown files |
| **Chunking** | 30-60 seconds | ~500-1000 chunks |
| **Vector Generation** | 5-10 minutes | 768-dim embeddings |
| **Database Insertion** | 1-3 minutes | Indexed vectors |

### Storage Requirements

- **Source PDFs**: ~10-15 MB total
- **Markdown Files**: ~2-5 MB total  
- **Vector Database**: ~50-100 MB (with indexes)
- **JSON Exports**: ~20-30 MB total

## 🔗 Integration

This ingestion service integrates with:

- **[Database Service](../database/README.md)**: Stores processed vectors and metadata
- **[Server Service](../server/README.md)**: Provides RAG search capabilities using ingested data
- **[Testing Service](../testing/README.md)**: Validates ingestion quality and search performance

## Troubleshooting

### Common Issues

1. **Database connection fails**:
   - Ensure PostgreSQL is running on localhost:5432
   - Check username/password in `.env`
   - Ensure pgvector extension is available

2. **Embedding model not found**:
   - Run `ollama pull gemma:300m`
   - Check if Ollama is running on localhost:11434

3. **PDF processing errors**:
   - Ensure PDF files are not corrupted
   - Check file permissions
   - Some PDFs may have content extraction limitations

### Debugging

Use debug logging for detailed information:
```bash
python src/main.py --log-level DEBUG test
```

## Development

### Project Structure
```
src/
├── __init__.py          # Package initialization
├── main.py             # Main entry point
├── cli.py              # CLI interface
├── config.py           # Configuration management
├── database.py         # Database connection and setup
├── document_processor.py  # PDF processing with Docling
├── embedding_service.py   # Ollama embedding service
└── vector_store.py     # Vector storage with LlamaIndex
```

### Adding New Features

1. **New document types**: Extend `DocumentProcessor` class
2. **Different embedding models**: Modify `EmbeddingService` configuration
3. **Additional metadata**: Update `ProcessedDocument` dataclass
4. **New CLI commands**: Add to `cli.py`

## License

MIT License - See LICENSE file for details.

## 👨‍💻 Author

**Amin Ahmed Khan**
- 🔗 LinkedIn: [aa2kb](https://www.linkedin.com/in/aa2kb/)
- 💻 GitHub: [aa2kb](https://github.com/aa2kb)