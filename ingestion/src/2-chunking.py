#!/usr/bin/env python3
"""
Chunk markdown files using Docling Hybrid Chunker.
Creates chunks from markdown files and saves them in chunks/ folder.
"""

import os
import sys
import json
import hashlib
from pathlib import Path
from dotenv import load_dotenv
from docling_core.types.doc import DoclingDocument
from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter

def load_config():
    """Load configuration from .env file."""
    env_path = Path("../.env")
    if not env_path.exists():
        env_path = Path(".env")
    
    if env_path.exists():
        load_dotenv(env_path)
    
    return {
        'CHUNK_SIZE': int(os.getenv('CHUNK_SIZE', 1024)),
        'CHUNK_OVERLAP': int(os.getenv('CHUNK_OVERLAP', 200)),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO')
    }

def get_markdown_hash(markdown_path):
    """Generate a hash for the markdown file based on name and modification time."""
    stat = markdown_path.stat()
    # Use file size and modification time for consistent hash
    hash_input = f"{markdown_path.name}_{stat.st_size}_{stat.st_mtime}"
    return hashlib.md5(hash_input.encode()).hexdigest()[:8]

def get_chunks_path(markdown_path, chunks_dir):
    """Get the chunks file path for a markdown file."""
    md_hash = get_markdown_hash(markdown_path)
    stem = markdown_path.stem
    chunks_name = f"{stem}_{md_hash}_chunks.json"
    return chunks_dir / chunks_name

def should_process_markdown(markdown_path, chunks_path):
    """Check if markdown needs to be chunked."""
    if not chunks_path.exists():
        return True, "Chunks file doesn't exist"
    
    md_mtime = markdown_path.stat().st_mtime
    chunks_mtime = chunks_path.stat().st_mtime
    
    if md_mtime > chunks_mtime:
        return True, "Markdown is newer than chunks"
    
    return False, "Chunks are up to date"

def extract_metadata_from_markdown(content):
    """Extract metadata from markdown frontmatter."""
    metadata = {}
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            actual_content = parts[2].strip()
            
            # Parse YAML-style frontmatter
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
            
            return metadata, actual_content
    
    return {}, content

def chunk_markdown_with_docling(markdown_path, config):
    """Chunk markdown content using Docling Hybrid Chunker."""
    print(f"  Loading markdown content...")
    
    try:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            print(f"  WARNING: Empty markdown file")
            return []
        
        # Extract metadata and content
        metadata, clean_content = extract_metadata_from_markdown(content)
        print(f"  Extracted metadata: {len(metadata)} fields")
        print(f"  Content length: {len(clean_content)} characters")
        
        # Create a simple DoclingDocument from markdown content
        # Note: This is a simplified approach - you may need to adjust based on docling version
        try:
            # Try to create document from markdown content
            converter = DocumentConverter()
            
            # Save content to temporary file for processing
            temp_md_path = markdown_path.parent / f"temp_{markdown_path.name}"
            with open(temp_md_path, 'w', encoding='utf-8') as f:
                f.write(clean_content)
            
            # Convert markdown to DoclingDocument
            result = converter.convert(str(temp_md_path))
            document = result.document
            
            # Clean up temp file
            temp_md_path.unlink()
            
        except Exception as e:
            print(f"  WARNING: Could not create DoclingDocument - {e}")
            print(f"  Falling back to simple text chunking")
            return chunk_text_simple(clean_content, metadata, config)
        
        if not document:
            print(f"  ERROR: Failed to create document")
            return None
        
        print(f"  Creating Hybrid Chunker...")
        
        # Initialize Hybrid Chunker with configuration
        chunker = HybridChunker(
            chunk_size=config['CHUNK_SIZE'],
            overlap=config['CHUNK_OVERLAP']
        )
        
        print(f"  Chunking document...")
        
        # Perform chunking
        chunks = chunker.chunk(document)
        
        if not chunks:
            print(f"  WARNING: No chunks generated")
            return []
        
        print(f"  Generated {len(chunks)} chunks")
        
        # Convert chunks to our format
        processed_chunks = []
        for i, chunk in enumerate(chunks):
            chunk_data = {
                'chunk_index': i,
                'content': str(chunk.text) if hasattr(chunk, 'text') else str(chunk),
                'metadata': {
                    **metadata,  # Include original document metadata
                    'source_file': markdown_path.name,
                    'chunk_method': 'docling_hybrid',
                    'chunk_size_config': config['CHUNK_SIZE'],
                    'chunk_overlap_config': config['CHUNK_OVERLAP']
                }
            }
            
            # Add chunk-specific metadata if available
            if hasattr(chunk, 'meta'):
                chunk_data['metadata'].update(chunk.meta)
            
            processed_chunks.append(chunk_data)
        
        return processed_chunks
        
    except Exception as e:
        print(f"  ERROR: Docling chunking failed - {e}")
        print(f"  Falling back to simple text chunking")
        
        # Fallback to simple chunking
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
        metadata, clean_content = extract_metadata_from_markdown(content)
        return chunk_text_simple(clean_content, metadata, config)

def chunk_text_simple(content, metadata, config):
    """Simple fallback text chunking when Docling chunking fails."""
    chunk_size = config['CHUNK_SIZE']
    overlap = config['CHUNK_OVERLAP']
    
    chunks = []
    start = 0
    chunk_index = 0
    
    while start < len(content):
        end = start + chunk_size
        
        # Try to break at word boundary
        if end < len(content):
            # Look for last space or newline within reasonable distance
            for i in range(min(100, chunk_size // 4)):
                if end - i >= start and content[end - i] in [' ', '\n', '.', '!', '?']:
                    end = end - i
                    break
        
        chunk_text = content[start:end].strip()
        
        if chunk_text:
            chunk_data = {
                'chunk_index': chunk_index,
                'content': chunk_text,
                'metadata': {
                    **metadata,
                    'chunk_method': 'simple_text',
                    'chunk_size_config': config['CHUNK_SIZE'],
                    'chunk_overlap_config': config['CHUNK_OVERLAP'],
                    'start_pos': start,
                    'end_pos': end
                }
            }
            chunks.append(chunk_data)
            chunk_index += 1
        
        # Move start position with overlap
        start = end - overlap if overlap < end - start else end
        
        # Prevent infinite loop
        if start >= len(content):
            break
    
    return chunks

def save_chunks(chunks, chunks_path, markdown_path):
    """Save chunks as JSON file with metadata."""
    try:
        # Create chunk file metadata
        chunk_file_data = {
            'source_markdown': markdown_path.name,
            'created_at': markdown_path.stat().st_mtime,
            'total_chunks': len(chunks),
            'chunking_method': chunks[0]['metadata'].get('chunk_method', 'unknown') if chunks else 'unknown',
            'chunks': chunks
        }
        
        # Write to file
        with open(chunks_path, 'w', encoding='utf-8') as f:
            json.dump(chunk_file_data, f, indent=2, ensure_ascii=False)
        
        print(f"  Saved {len(chunks)} chunks to {chunks_path.name}")
        return True
        
    except Exception as e:
        print(f"  ERROR: Failed to save chunks - {e}")
        return False

def process_markdown(markdown_path, chunks_dir, config):
    """Process a single markdown file."""
    print(f"\nProcessing: {markdown_path.name}")
    
    # Get chunks path
    chunks_path = get_chunks_path(markdown_path, chunks_dir)
    
    # Check if processing is needed
    should_process, reason = should_process_markdown(markdown_path, chunks_path)
    
    if not should_process:
        print(f"  Skipping: {reason}")
        return True
    
    print(f"  Processing: {reason}")
    
    # Get file stats
    stat = markdown_path.stat()
    print(f"  Size: {stat.st_size / 1024:.1f} KB")
    
    # Chunk markdown
    chunks = chunk_markdown_with_docling(markdown_path, config)
    
    if chunks is None:
        return False
    
    if not chunks:
        print(f"  WARNING: No chunks generated")
        return True
    
    # Save chunks
    return save_chunks(chunks, chunks_path, markdown_path)

def main():
    print("Markdown Chunking with Docling Hybrid Chunker")
    print("=" * 50)
    
    # Load config
    config = load_config()
    
    # Setup paths
    markdown_dir = Path("../markdown")
    if not markdown_dir.exists():
        markdown_dir = Path("markdown")
    
    if not markdown_dir.exists():
        print("ERROR: markdown folder not found")
        print("Run: python src/1-parse.py first")
        return 1
    
    chunks_dir = Path("../chunks")
    if not chunks_dir.exists():
        chunks_dir = Path("chunks")
    
    # Create chunks directory if it doesn't exist
    chunks_dir.mkdir(exist_ok=True)
    
    print(f"Input folder: {markdown_dir}")
    print(f"Output folder: {chunks_dir}")
    print(f"Chunk size: {config['CHUNK_SIZE']}")
    print(f"Chunk overlap: {config['CHUNK_OVERLAP']}")
    
    # Find markdown files
    md_files = list(markdown_dir.glob("*.md"))
    
    if not md_files:
        print("No markdown files found in markdown folder")
        return 0
    
    print(f"Found {len(md_files)} markdown files")
    
    # Process each markdown file
    processed = 0
    skipped = 0
    failed = 0
    
    for md_file in md_files:
        try:
            success = process_markdown(md_file, chunks_dir, config)
            if success:
                # Check if it was actually processed or skipped
                chunks_path = get_chunks_path(md_file, chunks_dir)
                should_process, reason = should_process_markdown(md_file, chunks_path)
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
    print("\n" + "=" * 50)
    print("Results:")
    print(f"Processed: {processed}")
    print(f"Skipped:   {skipped}")
    print(f"Failed:    {failed}")
    print(f"Total:     {len(md_files)}")
    
    if failed > 0:
        print(f"\n{failed} files failed to process")
        return 1
    else:
        print("\nAll files processed successfully!")
        return 0

if __name__ == "__main__":
    sys.exit(main())