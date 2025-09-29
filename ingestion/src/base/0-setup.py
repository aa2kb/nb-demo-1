import sys
from pathlib import Path
import requests
from docling.document_converter import DocumentConverter
from common import get_config, get_vector_store

def check_postgres():
    """Check PostgreSQL connection using common.py."""
    print("\n🗄️  Checking PostgreSQL...")
    
    try:
        config = get_config()
        print(f"Config: {config['DB_NAME']}@{config['DB_HOST']}:{config['DB_PORT']}")
        
        vector_store = get_vector_store()
        print("✅ PGVectorStore created successfully")
        print(f"   Table: data_{config['VECTOR_TABLE_NAME']}")
        print(f"   Embedding dimension: {config['EMBEDDING_DIM']}")
        return True
        
    except Exception as e:
        print(f"❌ PostgreSQL ERROR: {e}")
        print("💡 Make sure PostgreSQL is running with pgvector extension")
        return False

def check_ollama():
    """Check Ollama service and embedding model."""
    print("\n🤖 Checking Ollama...")
    
    try:
        config = get_config()
        ollama_host = config.get('OLLAMA_HOST', 'http://localhost:11434')
        embedding_model = config.get('EMBEDDING_MODEL', 'bge-m3:latest')
        
        # Check if Ollama is running
        response = requests.get(f"{ollama_host}/api/tags", timeout=10)
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
        if embedding_model in available_models:
            print(f"Found embedding model: {embedding_model}")
            
            # Test embedding
            embed_response = requests.post(
                f"{ollama_host}/api/embed",
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
    print("🚀 Document Ingestion Setup Check")
    print("=" * 40)
    print("Using common.py for configuration")
    
    # Show config
    try:
        config = get_config()
        print(f"✅ Config loaded: {len(config)} settings")
    except Exception as e:
        print(f"❌ Config failed: {e}")
        return 1
    
    # Run checks
    postgres_ok = check_postgres()
    ollama_ok = check_ollama()
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
        return 0
    else:
        print("\nSome checks failed. Fix issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())