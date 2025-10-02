import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from docling.document_converter import DocumentConverter
from llama_index.core import SimpleDirectoryReader

def load_config():
    """Load configuration from .env file."""
    env_path = Path("../.env")
    if not env_path.exists():
        env_path = Path(".env")
    
    if env_path.exists():
        load_dotenv(env_path)
    
    return {
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO')
    }

def get_markdown_path(pdf_path, markdown_dir):
    """Get the markdown file path for a PDF."""
    stem = pdf_path.stem
    markdown_name = f"{stem}.md"
    return markdown_dir / markdown_name

def should_process_pdf(pdf_path, markdown_path):
    """Check if PDF needs to be processed."""
    if not markdown_path.exists():
        return True, "Markdown file doesn't exist"
    
    pdf_mtime = pdf_path.stat().st_mtime
    md_mtime = markdown_path.stat().st_mtime
    
    if pdf_mtime > md_mtime:
        return True, "PDF is newer than markdown"
    
    return False, "Markdown is up to date"

def parse_pdf_with_docling(pdf_path):
    """Parse PDF using Docling and return markdown content."""
    
    print(f"  Converting with Docling...")
    
    try:
        converter = DocumentConverter()
        result = converter.convert(str(pdf_path))
        
        if not result or not result.document:
            print(f"  ERROR: Docling conversion failed")
            return None
        
        content = result.document.export_to_markdown()
        
        if not content.strip():
            print(f"  WARNING: No content extracted")
            return ""
        
        print(f"  Extracted {len(content)} characters")
        return content
        
    except Exception as e:
        print(f"  ERROR: Docling failed - {e}")
        return None

def create_markdown_metadata(pdf_path, content_length):
    """Create metadata section for markdown file."""
    stat = pdf_path.stat()
    
    metadata = f"""---
source_file: {pdf_path.name}
file_size: {stat.st_size}
processed_at: {stat.st_mtime}
content_length: {content_length}
---

"""
    return metadata

def save_markdown(content, markdown_path, pdf_path):
    """Save content as markdown file with metadata."""
    try:
        # Create metadata
        metadata = create_markdown_metadata(pdf_path, len(content))
        
        # Combine metadata and content
        full_content = metadata + content
        
        # Write to file
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"  Saved to {markdown_path.name}")
        return True
        
    except Exception as e:
        print(f"  ERROR: Failed to save markdown - {e}")
        return False

def process_pdf(pdf_path, markdown_dir):
    """Process a single PDF file."""
    print(f"\nProcessing: {pdf_path.name}")
    
    # Get markdown path
    markdown_path = get_markdown_path(pdf_path, markdown_dir)
    
    # Check if processing is needed
    should_process, reason = should_process_pdf(pdf_path, markdown_path)
    
    if not should_process:
        print(f"  Skipping: {reason}")
        return True
    
    print(f"  Processing: {reason}")
    print(f"  Size: {pdf_path.stat().st_size / 1024:.1f} KB")
    
    # Parse PDF
    content = parse_pdf_with_docling(pdf_path)
    
    if content is None:
        return False
    
    # Save markdown
    return save_markdown(content, markdown_path, pdf_path)

def main():
    print("PDF to Markdown Parser")
    print("=" * 40)
    
    # Load config
    config = load_config()
    
    # Setup paths
    docs_dir = Path("../docs")
    if not docs_dir.exists():
        docs_dir = Path("docs")
    
    if not docs_dir.exists():
        print("ERROR: docs folder not found")
        return 1
    
    markdown_dir = Path("../markdown")
    if not markdown_dir.exists():
        markdown_dir = Path("markdown")
    
    # Create markdown directory if it doesn't exist
    markdown_dir.mkdir(exist_ok=True)
    
    print(f"Input folder: {docs_dir}")
    print(f"Output folder: {markdown_dir}")
    
    # Use LlamaIndex to get PDF files
    try:
        reader = SimpleDirectoryReader(
            input_dir=str(docs_dir),
            required_exts=[".pdf", ".PDF"],
            recursive=False
        )
        
        # Get file paths from the reader
        input_files = reader.input_files
        pdf_files = [Path(f) for f in input_files]
        
    except Exception as e:
        print(f"ERROR: Failed to read directory with LlamaIndex - {e}")
        # Fallback to manual glob
        pdf_files = list(docs_dir.glob("*.pdf")) + list(docs_dir.glob("*.PDF"))
    
    if not pdf_files:
        print("No PDF files found in docs folder")
        return 0
    
    print(f"Found {len(pdf_files)} PDF files")
    
    # Process each PDF
    processed = 0
    skipped = 0
    failed = 0
    
    for pdf_file in pdf_files:
        try:
            success = process_pdf(pdf_file, markdown_dir)
            if success:
                # Check if it was actually processed or skipped
                markdown_path = get_markdown_path(pdf_file, markdown_dir)
                should_process, reason = should_process_pdf(pdf_file, markdown_path)
                if should_process:
                    processed += 1
                else:
                    skipped += 1
            else:
                failed += 1
        except KeyboardInterrupt:
            print("\nInterrupted by user")
            break
        except Exception as e:
            print(f"  ERROR: Unexpected error - {e}")
            failed += 1
    
    # Summary
    print("\n" + "=" * 40)
    print("Results:")
    print(f"Processed: {processed}")
    print(f"Skipped:   {skipped}")
    print(f"Failed:    {failed}")
    print(f"Total:     {len(pdf_files)}")
    
    if failed > 0:
        print(f"\n{failed} files failed to process")
        return 1
    else:
        print("\nAll files processed successfully!")
        return 0

if __name__ == "__main__":
    sys.exit(main())