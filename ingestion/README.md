# Document Ingestion CLI

A powerful CLI application for processing PDF documents and storing them as vectors in PostgreSQL using Ollama embeddings, Docling for document processing, and LlamaIndex for RAG methodology.

## Features

- **PDF Processing**: Extract and structure content from PDF documents using Docling
- **Vector Embeddings**: Generate embeddings using Ollama's gemma:300m model
- **Vector Storage**: Store embeddings in PostgreSQL with pgvector extension
- **CLI Interface**: Rich command-line interface with progress indicators and statistics
- **Incremental Processing**: Skip already processed documents or force re-processing
- **Configuration Management**: Environment-based configuration with sensible defaults

## Prerequisites

1. **PostgreSQL** with pgvector extension running on localhost:5432
   - Username: admin
   - Password: admin
   - Database: postgres

2. **Ollama** running on localhost:11434 with gemma:300m model installed
   ```bash
   ollama pull gemma:300m
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