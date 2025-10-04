# Database Service - PostgreSQL with pgvector

This folder contains the database service configuration for the NB-2 project, providing a PostgreSQL database with pgvector extension for vector storage and similarity search capabilities.

## 🏗️ Overview

The database service serves as the foundation for the RAG (Retrieval-Augmented Generation) system, storing document embeddings and enabling efficient vector similarity searches.

### Key Features

- **PostgreSQL 16**: Modern relational database system
- **pgvector Extension**: Vector similarity search and storage
- **Persistent Storage**: Docker volume for data persistence
- **Hybrid Search**: Combines vector similarity with text search
- **Multi-dimensional Embeddings**: Support for various embedding models

## 📁 Contents

```
database/
├── Dockerfile              # PostgreSQL + pgvector container setup
└── README.md               # This documentation
```

## 🐳 Docker Configuration

### Base Image
- **postgres:16**: Official PostgreSQL 16 image
- **pgvector extension**: Automatically installed for vector operations

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `POSTGRES_USER` | `admin` | Database superuser |
| `POSTGRES_PASSWORD` | `admin` | Database password |
| `POSTGRES_DB` | `nb2` | Default database name |

### Ports
- **5432**: PostgreSQL connection port (mapped to host)

### Volumes
- **nb2-postgres-data**: Persistent storage for database data

## 🔧 Setup & Usage

### 1. Start Database Service

```bash
# Start only the database
docker-compose up -d database

# Or start with the full stack
docker-compose up -d
```

### 2. Connect to Database

```bash
# Using Docker Compose
docker-compose exec database psql -U admin -d nb2

# Using psql directly
psql -h localhost -p 5432 -U admin -d nb2
```

### 3. Verify pgvector Installation

```sql
-- Check if pgvector extension is available
SELECT * FROM pg_available_extensions WHERE name = 'vector';

-- Create vector extension if not exists
CREATE EXTENSION IF NOT EXISTS vector;

-- Verify installation
\dx vector
```

## 📊 Database Schema

### Vector Storage Tables

The database contains tables created by the ingestion service for storing document embeddings:

#### Example Table Structure
```sql
-- Example vector table created by LlamaIndex
CREATE TABLE vectors_docling_nomic_embed (
    node_id VARCHAR PRIMARY KEY,
    text TEXT,
    metadata_ JSONB,
    embedding VECTOR(768)  -- 768-dimensional vectors for nomic-embed-text
);

-- Vector similarity index
CREATE INDEX ON vectors_docling_nomic_embed 
USING ivfflat (embedding vector_cosine_ops) 
WITH (lists = 100);
```

### Metadata Structure
```json
{
    "document_title": "Abu Dhabi Procurement Standards",
    "file_name": "Abu Dhabi Procurement Standards.PDF",
    "file_path": "/docs/Abu Dhabi Procurement Standards.PDF",
    "file_type": "application/pdf",
    "file_size": 2547264,
    "creation_date": "2024-10-04",
    "last_modified_date": "2024-10-04"
}
```

## 🚀 Vector Operations

### Similarity Search
```sql
-- Find similar documents using cosine similarity
SELECT 
    node_id,
    text,
    metadata_->>'document_title' as document,
    1 - (embedding <=> '[0.1, 0.2, ...]'::vector) as similarity
FROM vectors_docling_nomic_embed
ORDER BY embedding <=> '[0.1, 0.2, ...]'::vector
LIMIT 10;
```

### Hybrid Search
```sql
-- Combine vector similarity with text search
SELECT 
    node_id,
    text,
    metadata_,
    ts_rank(to_tsvector('english', text), plainto_tsquery('english', 'procurement')) as text_score,
    1 - (embedding <=> '[0.1, 0.2, ...]'::vector) as vector_score
FROM vectors_docling_nomic_embed
WHERE to_tsvector('english', text) @@ plainto_tsquery('english', 'procurement')
ORDER BY 
    (ts_rank(to_tsvector('english', text), plainto_tsquery('english', 'procurement')) * 0.3 +
     (1 - (embedding <=> '[0.1, 0.2, ...]'::vector)) * 0.7) DESC
LIMIT 10;
```

## 🔍 Monitoring & Maintenance

### Health Checks

```bash
# Check database connectivity
docker-compose exec database pg_isready -U admin

# Check database size
docker-compose exec database psql -U admin -d nb2 -c "
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables 
WHERE schemaname = 'public';"
```

### Performance Monitoring

```sql
-- Check vector index usage
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_scan as index_scans,
    idx_tup_read as tuples_read
FROM pg_stat_user_indexes 
WHERE indexname LIKE '%vector%';

-- Monitor query performance
SELECT 
    query,
    calls,
    total_time,
    mean_time,
    rows
FROM pg_stat_statements 
WHERE query LIKE '%vector%'
ORDER BY total_time DESC;
```

## 🗄️ Data Management

### Backup & Restore

```bash
# Create backup
docker-compose exec database pg_dump -U admin nb2 > backup_$(date +%Y%m%d_%H%M%S).sql

# Restore from backup
docker-compose exec -T database psql -U admin nb2 < backup_file.sql

# Volume backup
docker run --rm \
  -v nb2-postgres-data:/data \
  -v $(pwd):/backup \
  ubuntu tar czf /backup/postgres-data-$(date +%Y%m%d_%H%M%S).tar.gz /data
```

### Data Cleanup

```sql
-- Remove old vectors (if needed)
DELETE FROM vectors_docling_nomic_embed 
WHERE metadata_->>'creation_date' < '2024-01-01';

-- Vacuum and analyze for performance
VACUUM ANALYZE vectors_docling_nomic_embed;

-- Reindex vector indices
REINDEX INDEX vectors_docling_nomic_embed_embedding_idx;
```

## 🔧 Configuration

### PostgreSQL Tuning for Vectors

The Dockerfile includes optimizations for vector operations:

```sql
-- Memory settings for vector operations
shared_buffers = 256MB
work_mem = 64MB
maintenance_work_mem = 512MB

-- Vector-specific settings
shared_preload_libraries = 'vector'
```

### pgvector Configuration

```sql
-- Set vector search parameters
SET ivfflat.probes = 10;  -- Number of lists to search

-- Create optimized index
CREATE INDEX ON vectors_docling_nomic_embed 
USING ivfflat (embedding vector_cosine_ops) 
WITH (lists = 100);
```

## 🚨 Troubleshooting

### Common Issues

1. **Connection Refused**
   ```bash
   # Check if container is running
   docker-compose ps database
   
   # Check container logs
   docker-compose logs database
   ```

2. **pgvector Extension Missing**
   ```sql
   -- Install extension manually
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

3. **Permission Issues**
   ```bash
   # Check file permissions
   ls -la $(docker volume inspect nb2-postgres-data --format '{{.Mountpoint}}')
   ```

4. **Performance Issues**
   ```sql
   -- Check index usage
   EXPLAIN ANALYZE SELECT ... FROM vectors_docling_nomic_embed ...;
   
   -- Update statistics
   ANALYZE vectors_docling_nomic_embed;
   ```

## 🔗 Integration

This database service integrates with:

- **[Ingestion Service](../ingestion/README.md)**: Stores processed document embeddings
- **[Server Service](../server/README.md)**: Provides RAG functionality via vector search
- **[Testing Service](../testing/README.md)**: Validates database performance

## 📚 Additional Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [pgvector Documentation](https://github.com/pgvector/pgvector)
- [LlamaIndex Vector Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/)
- [Vector Database Best Practices](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)

---

**Built for efficient vector storage and retrieval in RAG applications** 🚀

## 👨‍💻 Author

**Amin Ahmed Khan**
- 🔗 LinkedIn: [aa2kb](https://www.linkedin.com/in/aa2kb/)
- 💻 GitHub: [aa2kb](https://github.com/aa2kb)