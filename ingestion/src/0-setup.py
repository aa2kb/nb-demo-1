#!/usr/bin/env python3
"""
Setup verification for document ingestion system.
Checks PostgreSQL, Ollama, and Docling are working.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def load_config():
    """Load configuration from .env file."""
    env_path = Path("../.env")  # Look for .env in parent directory
    if not env_path.exists():
        env_path = Path(".env")  # Try current directory
    
    if env_path.exists():
        load_dotenv(env_path)
        print(f"Using config from {env_path}")
    else:
        print("No .env file found, using defaults")
    
    config = {
        'DB_HOST': os.getenv('DB_HOST', 'localhost'),
        'DB_PORT': int(os.getenv('DB_PORT', 5432)),
        'DB_USER': os.getenv('DB_USER', 'admin'),
        'DB_PASSWORD': os.getenv('DB_PASSWORD', 'admin'),
        'DB_NAME': os.getenv('DB_NAME', 'postgres'),
        'OLLAMA_HOST': os.getenv('OLLAMA_HOST', 'http://localhost:11434'),
        'EMBEDDING_MODEL': os.getenv('EMBEDDING_MODEL', 'embeddinggemma:300m'),
        'CHUNK_SIZE': int(os.getenv('CHUNK_SIZE', 1024)),
        'CHUNK_OVERLAP': int(os.getenv('CHUNK_OVERLAP', 200)),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'DEBUG')
    }
    
    return config

def check_and_enable_pgvector(cursor, conn):
    """Check if pgvector extension is available and enable it."""
    try:
        # Check if pgvector is available
        cursor.execute("SELECT name, default_version FROM pg_available_extensions WHERE name = 'vector';")
        result = cursor.fetchone()
        
        if not result:
            print("WARNING: pgvector extension not available in this PostgreSQL instance")
            print("Falling back to JSON embedding storage")
            return True  # Continue with JSON storage
        
        # Check if pgvector is already installed
        cursor.execute("SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';")
        installed = cursor.fetchone()
        
        if installed:
            print(f"pgvector extension already installed (v{installed[1]})")
            return True
        
        # Install pgvector extension
        print(f"Installing pgvector extension v{result[1]}...")
        cursor.execute("CREATE EXTENSION vector;")
        conn.commit()
        print("pgvector extension installed successfully")
        
        # Verify installation
        cursor.execute("SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';")
        verified = cursor.fetchone()
        if verified:
            print(f"pgvector verified: v{verified[1]}")
            return True
        else:
            print("ERROR: pgvector installation verification failed")
            return False
            
    except Exception as e:
        print(f"ERROR: Failed to install pgvector - {e}")
        print("Continuing with JSON embedding storage")
        return True  # Continue even if pgvector fails

def check_postgres(config):
    """Check PostgreSQL connection and create table if needed."""
    print("\nChecking PostgreSQL...")
    
    try:
        import psycopg2
    except ImportError:
        print("ERROR: psycopg2 not installed. Run: pip install psycopg2-binary")
        return False
    
    try:
        conn = psycopg2.connect(
            host=config['DB_HOST'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
            database=config['DB_NAME']
        )
        cursor = conn.cursor()
        
        # Check version
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0].split(',')[0]
        print(f"Connected to {version}")
        
        # Check and enable pgvector extension
        if not check_and_enable_pgvector(cursor, conn):
            return False
        
        # Check if tables exist
        cursor.execute("""
            SELECT 
                (SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'documents_sources')) as sources_exists,
                (SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'document_chunks')) as chunks_exists;
        """)
        
        tables_result = cursor.fetchone()
        sources_exists, chunks_exists = tables_result
        
        if sources_exists and chunks_exists:
            print("Tables 'documents_sources' and 'document_chunks' exist")
            
            # Check embedding column type
            cursor.execute("""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = 'document_chunks' 
                AND column_name IN ('embedding', 'embedding_json');
            """)
            embedding_cols = cursor.fetchall()
            
            embedding_type = "Unknown"
            for col_name, col_type in embedding_cols:
                if col_name == 'embedding' and col_type == 'USER-DEFINED':
                    # Check if it's actually a vector type
                    cursor.execute("""
                        SELECT pg_type.typname 
                        FROM information_schema.columns 
                        JOIN pg_type ON pg_type.oid = (
                            SELECT atttypid FROM pg_attribute 
                            WHERE attrelid = 'document_chunks'::regclass 
                            AND attname = 'embedding'
                        )
                        WHERE table_name = 'document_chunks' 
                        AND column_name = 'embedding';
                    """)
                    type_result = cursor.fetchone()
                    if type_result and type_result[0] == 'vector':
                        embedding_type = "pgvector"
                elif col_name == 'embedding_json':
                    embedding_type = "JSON"
            
            # Show table info
            cursor.execute("SELECT COUNT(*) FROM documents_sources;")
            sources_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM document_chunks;")
            chunks_count = cursor.fetchone()[0]
            print(f"  - {sources_count} documents in sources table")
            print(f"  - {chunks_count} chunks in chunks table")
            print(f"  - Embedding storage: {embedding_type}")
        else:
            # Check if pgvector is installed to determine table schema
            cursor.execute("SELECT extname FROM pg_extension WHERE extname = 'vector';")
            pgvector_installed = cursor.fetchone() is not None
            
            print("Creating tables...")
            if pgvector_installed:
                print("Using pgvector for embeddings")
                cursor.execute("""
                    -- Create documents_sources table first
                    CREATE TABLE documents_sources (
                        id SERIAL PRIMARY KEY,
                        source_file_name VARCHAR(255) NOT NULL UNIQUE,
                        source_file_path VARCHAR(500) NOT NULL,
                        source_file_hash VARCHAR(64) NOT NULL,
                        source_file_size BIGINT NOT NULL,
                        source_file_modified_at TIMESTAMP NOT NULL,
                        processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        processing_status VARCHAR(50) DEFAULT 'pending',
                        total_chunks INTEGER DEFAULT 0,
                        total_characters BIGINT DEFAULT 0,
                        extraction_method VARCHAR(100) DEFAULT 'docling',
                        metadata JSONB,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                    
                    -- Create document_chunks table with pgvector embedding column
                    CREATE TABLE document_chunks (
                        id SERIAL PRIMARY KEY,
                        document_id INTEGER NOT NULL REFERENCES documents_sources(id) ON DELETE CASCADE,
                        chunk_index INTEGER NOT NULL,
                        content TEXT NOT NULL,
                        embedding vector(768),
                        chunk_metadata JSONB,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(document_id, chunk_index)
                    );
                    
                    -- Create indexes including vector similarity indexes
                    CREATE INDEX idx_document_chunks_doc_id ON document_chunks(document_id);
                    CREATE INDEX idx_documents_sources_filename ON documents_sources(source_file_name);
                    CREATE INDEX idx_documents_sources_hash ON documents_sources(source_file_hash);
                    CREATE INDEX idx_documents_sources_status ON documents_sources(processing_status);
                    
                    -- Create HNSW index for fast vector similarity search
                    CREATE INDEX idx_document_chunks_embedding_hnsw ON document_chunks 
                    USING hnsw (embedding vector_cosine_ops);
                """)
            else:
                print("Using JSON for embeddings (pgvector not available)")
                cursor.execute("""
                    -- Create documents_sources table first
                    CREATE TABLE documents_sources (
                        id SERIAL PRIMARY KEY,
                        source_file_name VARCHAR(255) NOT NULL UNIQUE,
                        source_file_path VARCHAR(500) NOT NULL,
                        source_file_hash VARCHAR(64) NOT NULL,
                        source_file_size BIGINT NOT NULL,
                        source_file_modified_at TIMESTAMP NOT NULL,
                        processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        processing_status VARCHAR(50) DEFAULT 'pending',
                        total_chunks INTEGER DEFAULT 0,
                        total_characters BIGINT DEFAULT 0,
                        extraction_method VARCHAR(100) DEFAULT 'docling',
                        metadata JSONB,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                    
                    -- Create document_chunks table with JSON embedding column
                    CREATE TABLE document_chunks (
                        id SERIAL PRIMARY KEY,
                        document_id INTEGER NOT NULL REFERENCES documents_sources(id) ON DELETE CASCADE,
                        chunk_index INTEGER NOT NULL,
                        content TEXT NOT NULL,
                        embedding_json TEXT,
                        chunk_metadata JSONB,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(document_id, chunk_index)
                    );
                    
                    -- Create indexes
                    CREATE INDEX idx_document_chunks_doc_id ON document_chunks(document_id);
                    CREATE INDEX idx_documents_sources_filename ON documents_sources(source_file_name);
                    CREATE INDEX idx_documents_sources_hash ON documents_sources(source_file_hash);
                    CREATE INDEX idx_documents_sources_status ON documents_sources(processing_status);
                """)
            
            conn.commit()
            print("Tables created")
        
        cursor.close()
        conn.close()
        print("PostgreSQL OK")
        return True
        
    except Exception as e:
        print(f"PostgreSQL ERROR: {e}")
        return False

def check_ollama(config):
    """Check Ollama service and embedding model."""
    print("\nChecking Ollama...")
    
    try:
        import requests
    except ImportError:
        print("ERROR: requests not installed. Run: pip install requests")
        return False
    
    try:
        # Check if Ollama is running
        response = requests.get(f"{config['OLLAMA_HOST']}/api/tags", timeout=10)
        if response.status_code != 200:
            print(f"Ollama not responding (status {response.status_code})")
            return False
        
        print("Ollama service running")
        
        # Check models
        models_data = response.json()
        available_models = []
        
        if 'models' in models_data:
            for model in models_data['models']:
                if isinstance(model, dict) and 'name' in model:
                    available_models.append(model['name'])
        
        print(f"Found {len(available_models)} models")
        
        # Check for embedding model
        embedding_model = config['EMBEDDING_MODEL']
        if embedding_model in available_models:
            print(f"Found embedding model: {embedding_model}")
            
            # Test embedding
            embed_response = requests.post(
                f"{config['OLLAMA_HOST']}/api/embed",
                json={"model": embedding_model, "input": "test"},
                timeout=30
            )
            
            if embed_response.status_code == 200:
                embed_data = embed_response.json()
                if 'embeddings' in embed_data and len(embed_data['embeddings']) > 0:
                    dim = len(embed_data['embeddings'][0])
                    print(f"Embedding test successful ({dim} dimensions)")
                    print("Ollama OK")
                    return True
            
            print("Embedding test failed")
            return False
        else:
            print(f"Model {embedding_model} not found")
            print("Available models:", available_models)
            print(f"Run: ollama pull {embedding_model}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("Can't connect to Ollama. Is it running?")
        return False
    except Exception as e:
        print(f"Ollama ERROR: {e}")
        return False

def check_docling():
    """Check Docling document processing."""
    print("\nChecking Docling...")
    
    try:
        from docling.document_converter import DocumentConverter
    except ImportError:
        print("ERROR: Docling not installed. Run: pip install docling")
        return False
    
    # Find test PDF
    test_pdf = Path("hello_world.pdf")
    if not test_pdf.exists():
        test_pdf = Path("src/hello_world.pdf")
    
    if not test_pdf.exists():
        print("No test PDF found (need hello_world.pdf)")
        return False
    
    try:
        print(f"Testing with {test_pdf}")
        converter = DocumentConverter()
        result = converter.convert(str(test_pdf))
        
        if not result or not result.document:
            print("Conversion failed")
            return False
        
        content = result.document.export_to_markdown()
        if not content.strip():
            print("No content extracted")
            return False
        
        print(f"Extracted {len(content)} characters")
        print("Docling OK")
        return True
        
    except Exception as e:
        print(f"Docling ERROR: {e}")
        return False

def check_docs_folder():
    """Check if docs folder exists and has PDF files."""
    print("\nChecking docs folder...")
    
    # Check for docs folder
    docs_dir = Path("../docs")
    if not docs_dir.exists():
        docs_dir = Path("docs")
    
    if not docs_dir.exists():
        print("ERROR: docs folder not found")
        return False
    
    print(f"Found docs folder: {docs_dir}")
    
    # Find PDF files
    pdf_files = list(docs_dir.glob("*.pdf")) + list(docs_dir.glob("*.PDF"))
    
    if not pdf_files:
        print("ERROR: No PDF files found in docs folder")
        return False
    
    print(f"Found {len(pdf_files)} PDF files:")
    for pdf in pdf_files:
        size_kb = pdf.stat().st_size / 1024
        print(f"  - {pdf.name} ({size_kb:.1f} KB)")
    
    print("Docs folder OK")
    return True

def check_markdown_folder():
    """Create markdown folder if it doesn't exist."""
    print("\nChecking markdown folder...")
    
    # Check for markdown folder
    markdown_dir = Path("../markdown")
    if not markdown_dir.exists():
        markdown_dir = Path("markdown")
    
    if markdown_dir.exists():
        print(f"Markdown folder exists: {markdown_dir}")
        # Count existing markdown files
        md_files = list(markdown_dir.glob("*.md"))
        if md_files:
            print(f"Found {len(md_files)} existing markdown files")
    else:
        print(f"Creating markdown folder: {markdown_dir}")
        try:
            markdown_dir.mkdir(parents=True, exist_ok=True)
            print("Markdown folder created")
        except Exception as e:
            print(f"ERROR: Failed to create markdown folder - {e}")
            return False
    
    print("Markdown folder OK")
    return True

def main():
    print("Document Ingestion Setup Check")
    print("=" * 40)
    
    # Load configuration
    config = load_config()
    if not config:
        return 1
    
    # Run checks
    postgres_ok = check_postgres(config)
    ollama_ok = check_ollama(config)
    docling_ok = check_docling()
    docs_ok = check_docs_folder()
    markdown_ok = check_markdown_folder()
    
    print("\n" + "=" * 40)
    print("Results:")
    print(f"PostgreSQL:     {'OK' if postgres_ok else 'FAILED'}")
    print(f"Ollama:         {'OK' if ollama_ok else 'FAILED'}")
    print(f"Docling:        {'OK' if docling_ok else 'FAILED'}")
    print(f"Docs folder:    {'OK' if docs_ok else 'FAILED'}")
    print(f"Markdown folder: {'OK' if markdown_ok else 'FAILED'}")
    
    if all([postgres_ok, ollama_ok, docling_ok, docs_ok, markdown_ok]):
        print("\nAll systems ready!")
        print("Ready to run: python src/1-parse.py")
        return 0
    else:
        print("\nSome checks failed. Fix issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())