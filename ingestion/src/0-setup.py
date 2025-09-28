import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import requests
from llama_index.vector_stores.postgres import PGVectorStore
from docling.document_converter import DocumentConverter

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
    """Check PostgreSQL connection and create LlamaIndex PGVectorStore."""
    print("\nChecking PostgreSQL...")
    
    try:
        # Create LlamaIndex PGVectorStore
        print("Creating LlamaIndex PGVectorStore...")
        vector_store = PGVectorStore.from_params(
            database=config['DB_NAME'],
            host=config['DB_HOST'],
            password=config['DB_PASSWORD'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            table_name="vectors",  # Creates data_vectors table
            embed_dim=768,
            hybrid_search=False,
            text_search_config="english"
        )
        
        print("✅ LlamaIndex PGVectorStore created successfully")
        print(f"   Database: {config['DB_NAME']}@{config['DB_HOST']}:{config['DB_PORT']}")
        print(f"   Table: data_vectors")
        print(f"   Embedding dimension: 768")
        print("✅ PostgreSQL connection and vector store setup complete")
        
        return True
        
    except Exception as e:
        print(f"PostgreSQL ERROR: {e}")
        print("Make sure PostgreSQL is running and pgvector extension is available")
        return False

def check_ollama(config):
    """Check Ollama service and embedding model."""
    print("\nChecking Ollama...")
    
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