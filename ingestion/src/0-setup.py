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
        
        # Check if table exists
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'document_chunks'
            );
        """)
        
        if cursor.fetchone()[0]:
            print("Table 'document_chunks' exists")
        else:
            print("Creating table 'document_chunks'...")
            cursor.execute("""
                CREATE TABLE document_chunks (
                    id SERIAL PRIMARY KEY,
                    document_id VARCHAR(255) NOT NULL,
                    document_name VARCHAR(255) NOT NULL,
                    chunk_index INTEGER NOT NULL,
                    content TEXT NOT NULL,
                    embedding_json TEXT,
                    metadata JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                CREATE INDEX idx_document_chunks_doc_id ON document_chunks(document_id);
            """)
            conn.commit()
            print("Table created")
        
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
    
    print("\n" + "=" * 40)
    print("Results:")
    print(f"PostgreSQL: {'OK' if postgres_ok else 'FAILED'}")
    print(f"Ollama:     {'OK' if ollama_ok else 'FAILED'}")
    print(f"Docling:    {'OK' if docling_ok else 'FAILED'}")
    
    if all([postgres_ok, ollama_ok, docling_ok]):
        print("\nAll systems ready!")
        return 0
    else:
        print("\nSome checks failed. Fix issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())