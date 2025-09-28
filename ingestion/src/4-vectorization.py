#!/usr/bin/env python3
"""
Generate embeddings for contextualized chunks using Ollama's embeddinggemma model.
Combines original content with contextualized content to create rich vector representations.
"""

import os
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from typing import List, Dict, Any

# LlamaIndex imports for embeddings
try:
    from llama_index.embeddings.ollama import OllamaEmbedding
    from llama_index.core import Settings
except ImportError as e:
    print(f"ERROR: Required packages not installed - {e}")
    print("Run: pip install llama-index llama-index-embeddings-ollama")
    sys.exit(1)

def load_config():
    """Load configuration from .env file."""
    env_path = Path("../.env")
    if not env_path.exists():
        env_path = Path(".env")
    
    if env_path.exists():
        load_dotenv(env_path)
    
    return {
        'OLLAMA_HOST': os.getenv('OLLAMA_HOST', 'http://localhost:11434'),
        'EMBEDDING_MODEL': os.getenv('EMBEDDING_MODEL', 'embeddinggemma:300m'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO')
    }

def setup_embeddings(config):
    """Setup Ollama embedding model."""
    try:
        embedding_model = OllamaEmbedding(
            model_name=config['EMBEDDING_MODEL'],
            base_url=config['OLLAMA_HOST']
        )
        
        # Set global LlamaIndex settings
        Settings.embed_model = embedding_model
        
        return embedding_model
    except Exception as e:
        print(f"ERROR: Failed to setup embedding model - {e}")
        raise

def load_contextual_chunks(contextual_file_path):
    """Load contextualized chunks from JSON file."""
    try:
        with open(contextual_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"  ERROR: Failed to load contextual chunks file - {e}")
        return None

def get_vectors_path(contextual_file_path, vectors_dir):
    """Get the vectors file path."""
    stem = contextual_file_path.stem
    # Replace _contextual_chunks with _vectors
    if stem.endswith('_contextual_chunks'):
        base_name = stem[:-19]  # Remove '_contextual_chunks'
    else:
        base_name = stem
    vectors_name = f"{base_name}_vectors.json"
    return vectors_dir / vectors_name

def create_embedding_text(chunk):
    """Create combined text for embedding generation."""
    content = chunk.get('content', '')
    context = chunk.get('content_contextualized', '')
    
    # Combine content and context for rich embeddings
    if context and context.strip() and context.strip().lower() != 'no context':
        embedding_text = f"Content: {content}\n\nContext: {context}"
    else:
        # If no context, use just the content
        embedding_text = f"Content: {content}"
    
    return embedding_text

def generate_embedding(embedding_model, text):
    """Generate embedding for given text."""
    try:
        # Generate embedding using LlamaIndex OllamaEmbedding
        embedding = embedding_model.get_text_embedding(text)
        return embedding
    except Exception as e:
        print(f"    WARNING: Embedding generation failed - {e}")
        return None

def should_process_chunk(chunk_data, existing_vectors_data):
    """Check if a chunk needs vectorization."""
    chunk_id = chunk_data.get('chunk_index', -1)
    
    if not existing_vectors_data:
        return True
    
    # Check if this chunk already has a vector
    existing_chunks = existing_vectors_data.get('chunks', [])
    
    for existing_chunk in existing_chunks:
        if existing_chunk.get('chunk_index') == chunk_id:
            # Check if content matches and already has vector
            if (existing_chunk.get('content') == chunk_data.get('content') and 
                'vector' in existing_chunk and 
                existing_chunk['vector']):
                return False  # Already processed
    
    return True

def save_vectors_data(vectors_path, vectors_data):
    """Save vectors data to JSON file."""
    try:
        with open(vectors_path, 'w', encoding='utf-8') as f:
            json.dump(vectors_data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"    ERROR: Failed to save vectors data - {e}")
        return False

def process_contextual_chunks_file(contextual_file_path, vectors_dir, embedding_model, config):
    """Process a single contextual chunks file to generate embeddings."""
    print(f"\nProcessing: {contextual_file_path.name}")
    
    # Load contextual chunks
    contextual_data = load_contextual_chunks(contextual_file_path)
    if not contextual_data:
        return False
    
    chunks = contextual_data.get('chunks', [])
    if not chunks:
        print(f"  No chunks found in file")
        return True
    
    print(f"  Found {len(chunks)} chunks")
    
    # Get vectors file path
    vectors_path = get_vectors_path(contextual_file_path, vectors_dir)
    
    # Load existing vectors data if it exists
    vectors_data = {}
    if vectors_path.exists():
        try:
            with open(vectors_path, 'r', encoding='utf-8') as f:
                vectors_data = json.load(f)
        except Exception as e:
            print(f"  WARNING: Could not load existing vectors data - {e}")
    
    # Initialize vectors data structure
    if not vectors_data:
        vectors_data = {
            'source_contextual_file': contextual_file_path.name,
            'source_markdown': contextual_data.get('source_markdown', 'unknown'),
            'total_chunks': len(chunks),
            'embedding_metadata': {
                'model': config['EMBEDDING_MODEL'],
                'ollama_host': config['OLLAMA_HOST'],
                'embedding_method': 'content_plus_context',
                'processing_status': 'in_progress'
            },
            'chunks': []
        }
    
    # Create a lookup of existing chunks by index
    existing_chunks = {chunk.get('chunk_index'): chunk for chunk in vectors_data.get('chunks', [])}
    
    # Process chunks
    processed = 0
    skipped = 0
    failed = 0
    
    for chunk in chunks:
        chunk_id = chunk.get('chunk_index', -1)
        
        # Check if chunk needs processing
        if not should_process_chunk(chunk, vectors_data):
            print(f"    Chunk {chunk_id}: Skipping (already processed)")
            skipped += 1
            continue
        print(f"Chunk: {chunk_id}")
        print(f"    Chunk {chunk_id}: Generating embedding...")
        
        try:
            # Create embedding text
            embedding_text = create_embedding_text(chunk)
            
            # Generate embedding
            vector = generate_embedding(embedding_model, embedding_text)
            
            if vector is None:
                print(f"    Chunk {chunk_id}: Failed to generate embedding")
                failed += 1
                continue
            
            # Create vectorized chunk (copy original chunk and add vector)
            vectorized_chunk = {
                'chunk_index': chunk_id,
                'content_contextualized': chunk.get('content_contextualized', ''),
                'content': chunk.get('content', ''),
                'metadata': chunk.get('metadata', {}),
                'vector': vector,
                'embedding_metadata': {
                    'embedding_text_length': len(embedding_text),
                    'vector_dimension': len(vector),
                    'has_context': bool(chunk.get('content_contextualized', '').strip()),
                    'embedding_model': config['EMBEDDING_MODEL']
                }
            }
            
            # Update existing chunks
            existing_chunks[chunk_id] = vectorized_chunk
            processed += 1
            
            print(f"    Chunk {chunk_id}: Embedding generated ({len(vector)} dimensions)")
            
            # Update vectors data and save immediately after each chunk
            vectors_data['chunks'] = sorted(existing_chunks.values(), key=lambda x: x['chunk_index'])
            vectors_data['embedding_metadata']['last_processed_chunk'] = chunk_id
            vectors_data['embedding_metadata']['processed_count'] = processed + skipped
            
            # Save after each chunk is processed
            if not save_vectors_data(vectors_path, vectors_data):
                print(f"    WARNING: Failed to save after processing chunk {chunk_id}")
            else:
                print(f"    Chunk {chunk_id}: Saved to {vectors_path.name}")
            
            # Small delay to avoid overwhelming Ollama
            time.sleep(0.1)
            
        except Exception as e:
            print(f"    Chunk {chunk_id}: Failed - {e}")
            failed += 1
    
    # Final update
    vectors_data['embedding_metadata']['processed_chunks'] = processed + skipped
    vectors_data['embedding_metadata']['failed_chunks'] = failed
    vectors_data['embedding_metadata']['total_chunks'] = len(chunks)
    
    # Update processing status
    if processed + skipped == len(chunks):
        vectors_data['embedding_metadata']['processing_status'] = 'completed'
    
    # Final save
    success = save_vectors_data(vectors_path, vectors_data)
    
    print(f"  Final save to {vectors_path.name}")
    print(f"  Processed: {processed}, Skipped: {skipped}, Failed: {failed}")
    
    return success and failed == 0

def main():
    print("Vector Generation with Ollama EmbeddingGemma")
    print("=" * 50)
    
    # Load config
    config = load_config()
    
    # Setup embedding model
    try:
        print("Setting up embedding model...")
        embedding_model = setup_embeddings(config)
        print(f"Embedding model configured: {config['EMBEDDING_MODEL']} @ {config['OLLAMA_HOST']}")
    except Exception as e:
        print(f"ERROR: Failed to setup embedding model - {e}")
        return 1
    
    # Setup paths
    contextual_dir = Path("../contextual_chunks")
    if not contextual_dir.exists():
        contextual_dir = Path("contextual_chunks")
    
    if not contextual_dir.exists():
        print("ERROR: contextual_chunks folder not found")
        print("Run: python src/3-contextualized_chunking.py first")
        return 1
    
    vectors_dir = Path("../vectors")
    if not vectors_dir.exists():
        vectors_dir = Path("vectors")
    
    # Create vectors directory
    vectors_dir.mkdir(exist_ok=True)
    
    print(f"Input folder: {contextual_dir}")
    print(f"Output folder: {vectors_dir}")
    print(f"Embedding model: {config['EMBEDDING_MODEL']}")
    
    # Find contextual chunk files
    contextual_files = list(contextual_dir.glob("*_contextual_chunks.json"))
    
    if not contextual_files:
        print("No contextual chunk files found in contextual_chunks folder")
        return 0
    
    print(f"Found {len(contextual_files)} contextual chunk files")
    
    # Process each contextual chunks file
    processed_files = 0
    failed_files = 0
    
    for contextual_file in contextual_files:
        try:
            success = process_contextual_chunks_file(contextual_file, vectors_dir, embedding_model, config)
            if success:
                processed_files += 1
            else:
                failed_files += 1
        except KeyboardInterrupt:
            print("\nInterrupted by user")
            break
        except Exception as e:
            print(f"  ERROR: Unexpected error - {e}")
            failed_files += 1
    
    # Summary
    print("\n" + "=" * 50)
    print("Results:")
    print(f"Files processed: {processed_files}")
    print(f"Files failed:    {failed_files}")
    print(f"Total files:     {len(contextual_files)}")
    
    if failed_files > 0:
        print(f"\n{failed_files} files had errors")
        return 1
    else:
        print("\nAll files processed successfully!")
        return 0

if __name__ == "__main__":
    sys.exit(main())