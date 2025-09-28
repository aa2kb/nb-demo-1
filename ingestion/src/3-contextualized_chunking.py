import os
import sys
import json
import hashlib
from pathlib import Path
from dotenv import load_dotenv
from typing import List, Dict, Any
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.llms.gemini import Gemini

# Context prompt template
CONTEXT_PROMPT_TEMPLATE = """
You are analyzing a document. Your task is to provide concise context for a specific section.

<context>
{context_chunks}
</context> 

<section>
{current_chunk}
</section>

Provide a brief context (1–2 sentences) that explains:

The topic this part relates to

How it connects to the overall document

Its relationship to other sections

Rules:

Do not use phrases like “This text…”, “This section…”, or “This passage…”.

Do not mention the word “section,” “chunk,” or “excerpt.”

Begin directly with the context itself (e.g., “Focuses on procurement policies…” instead of “This text focuses on…”).

Respond with only the context, nothing else.

also try to detect if the text is just navigational or non-content text and if so, return: “No Context”
"""

def load_config():
    """Load configuration from .env file."""
    env_path = Path("../.env")
    if not env_path.exists():
        env_path = Path(".env")
    
    if env_path.exists():
        load_dotenv(env_path)
    
    return {
        'OLLAMA_HOST': os.getenv('OLLAMA_HOST', 'http://localhost:11434'),
        'CONTEXT_WINDOW_SIZE': int(os.getenv('CONTEXT_WINDOW_SIZE', 10)),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
        'DEFAULT_LLM_PROVIDER': os.getenv('DEFAULT_LLM_PROVIDER', 'ollama'),
        'DEFAULT_LLM_MODEL': os.getenv('DEFAULT_LLM_MODEL', 'mistral:7b'),
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY')
    }

def setup_llm(config):
    """Setup LLM instance for contextualization based on provider."""
    provider = config['DEFAULT_LLM_PROVIDER'].lower()
    model = config['DEFAULT_LLM_MODEL']
    
    if provider == 'gemini':
        # Gemini LLM for context generation
        if not config['GEMINI_API_KEY']:
            raise ValueError("GEMINI_API_KEY is required when using Gemini provider")
        
        llm = Gemini(
            model=model,
            api_key=config['GEMINI_API_KEY']
        )
        print(f"Using Gemini LLM: {model}")
        
    elif provider == 'ollama':
        # Ollama LLM for context generation
        llm = Ollama(
            model=model,
            base_url=config['OLLAMA_HOST']
        )
        print(f"Using Ollama LLM: {model} @ {config['OLLAMA_HOST']}")
        
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}. Use 'gemini' or 'ollama'")
    
    # Set global LlamaIndex settings
    Settings.llm = llm
    
    return llm

def load_chunk_file(chunk_file_path):
    """Load chunks from JSON file."""
    try:
        with open(chunk_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"  ERROR: Failed to load chunk file - {e}")
        return None

def get_contextual_chunks_path(chunk_file_path, contextual_dir):
    """Get the contextual chunks file path."""
    stem = chunk_file_path.stem
    # Remove _chunks suffix if present and add _contextual
    if stem.endswith('_chunks'):
        base_name = stem[:-7]  # Remove '_chunks'
    else:
        base_name = stem
    contextual_name = f"{base_name}_contextual_chunks.json"
    return contextual_dir / contextual_name

def get_context_window(chunks: List[Dict], current_index: int, window_size: int = 10) -> str:
    """Get surrounding chunks for context."""
    start_idx = max(0, current_index - window_size)
    end_idx = min(len(chunks), current_index + window_size + 1)
    
    context_parts = []
    
    for i in range(start_idx, end_idx):
        if i == current_index:
            continue  # Skip the current chunk itself
        
        chunk = chunks[i]
        position = "before" if i < current_index else "after"
        context_parts.append(f"Chunk {i} ({position}): {chunk['content'][:200]}...")
    
    return "\n\n".join(context_parts)

def generate_context_for_chunk(llm, chunk: Dict, context_window: str) -> str:
    """Generate context for a single chunk using LLM."""
    try:
        prompt = CONTEXT_PROMPT_TEMPLATE.format(
            context_chunks=context_window,
            current_chunk=chunk['content']
        )
        
        # Use LlamaIndex Ollama LLM to generate context
        response = llm.complete(prompt)
        
        return str(response).strip()
            
    except Exception as e:
        print(f"    WARNING: Context generation failed - {e}")
        return f"Auto-generated context for chunk in document (context generation failed)"

def should_process_chunk(chunk_data: Dict, existing_contextual_data: Dict) -> bool:
    """Check if a chunk needs contextualization."""
    chunk_id = chunk_data.get('chunk_index', -1)
    
    if not existing_contextual_data:
        return True
    
    # Check if this chunk already has context
    existing_chunks = existing_contextual_data.get('chunks', [])
    
    for existing_chunk in existing_chunks:
        if existing_chunk.get('chunk_index') == chunk_id:
            # Check if content matches and already has contextualized content
            if (existing_chunk.get('content') == chunk_data.get('content') and 
                'content_contextualized' in existing_chunk and 
                existing_chunk['content_contextualized']):
                return False  # Already processed and content matches
    
    return True

def save_contextual_data(contextual_path, contextual_data):
    """Save contextual data to JSON file."""
    try:
        with open(contextual_path, 'w', encoding='utf-8') as f:
            json.dump(contextual_data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"    ERROR: Failed to save contextual data - {e}")
        return False

def process_chunk_file(chunk_file_path, contextual_dir, llm, config):
    """Process a single chunk file to add contextual information."""
    print(f"\nProcessing: {chunk_file_path.name}")
    
    # Load original chunks
    chunk_data = load_chunk_file(chunk_file_path)
    if not chunk_data:
        return False
    
    chunks = chunk_data.get('chunks', [])
    if not chunks:
        print(f"  No chunks found in file")
        return True
    
    print(f"  Found {len(chunks)} chunks")
    
    # Get contextual chunks path
    contextual_path = get_contextual_chunks_path(chunk_file_path, contextual_dir)
    
    # Load existing contextual data if it exists, otherwise start with original structure
    contextual_data = {}
    if contextual_path.exists():
        try:
            with open(contextual_path, 'r', encoding='utf-8') as f:
                contextual_data = json.load(f)
        except Exception as e:
            print(f"  WARNING: Could not load existing contextual data - {e}")
    
    # Initialize contextual data structure (preserve original structure)
    if not contextual_data:
        contextual_data = {
            'source_chunk_file': chunk_file_path.name,
            'source_markdown': chunk_data.get('source_markdown', 'unknown'),
            'total_chunks': len(chunks),
            'processing_metadata': {
                'contextualization_method': f'llamaindex_{config["DEFAULT_LLM_PROVIDER"]}_{config["DEFAULT_LLM_MODEL"].replace(":", "_").replace("-", "_")}',
                'llm_provider': config['DEFAULT_LLM_PROVIDER'],
                'llm_model': config['DEFAULT_LLM_MODEL'],
                'context_window_size': config['CONTEXT_WINDOW_SIZE'],
                'processing_status': 'in_progress'
            },
            'chunks': []
        }
    
    # Create a lookup of existing chunks by index
    existing_chunks = {chunk.get('chunk_index'): chunk for chunk in contextual_data.get('chunks', [])}
    
    # Process chunks
    processed = 0
    skipped = 0
    failed = 0
    
    for i, original_chunk in enumerate(chunks):
        chunk_id = original_chunk.get('chunk_index', i)
        
        # Check if chunk needs processing
        if not should_process_chunk(original_chunk, contextual_data):
            print(f"    Chunk {chunk_id}: Skipping (already processed)")
            skipped += 1
            continue
        print(f"Chunk: {chunk_id}")
        print(f"    Chunk {chunk_id}: Generating context...")
        
        try:
            # Get context window
            context_window = get_context_window(chunks, i, config['CONTEXT_WINDOW_SIZE'])
            
            # Generate context
            context = generate_context_for_chunk(llm, original_chunk, context_window)
            
            # Create contextualized chunk with your required structure
            contextual_chunk = {
                'chunk_index': chunk_id,
                'content_contextualized': context,
                'content': original_chunk['content'],
                'metadata': original_chunk.get('metadata', {})
            }
            
            # Update existing chunks
            existing_chunks[chunk_id] = contextual_chunk
            processed += 1
            
            print(f"    Chunk {chunk_id}: Context generated ({len(context)} chars)")
            
            # Update contextual data and save immediately after each chunk
            contextual_data['chunks'] = sorted(existing_chunks.values(), key=lambda x: x['chunk_index'])
            contextual_data['processing_metadata']['last_processed_chunk'] = chunk_id
            contextual_data['processing_metadata']['processed_count'] = processed + skipped
            
            # Save after each chunk is processed
            if not save_contextual_data(contextual_path, contextual_data):
                print(f"    WARNING: Failed to save after processing chunk {chunk_id}")
            else:
                print(f"    Chunk {chunk_id}: Saved to {contextual_path.name}")
            
        except Exception as e:
            print(f"    Chunk {chunk_id}: Failed - {e}")
            failed += 1
    
    # Final update
    contextual_data['processing_metadata']['processed_chunks'] = processed + skipped
    contextual_data['processing_metadata']['failed_chunks'] = failed
    contextual_data['processing_metadata']['total_chunks'] = len(chunks)
    
    # Update processing status
    if processed + skipped == len(chunks):
        contextual_data['processing_metadata']['processing_status'] = 'completed'
    
    # Final save
    success = save_contextual_data(contextual_path, contextual_data)
    
    print(f"  Final save to {contextual_path.name}")
    print(f"  Processed: {processed}, Skipped: {skipped}, Failed: {failed}")
    
    return success and failed == 0

def main():
    print("Contextual Chunk Generation with Mistral 7B")
    print("=" * 50)
    
    # Load config
    config = load_config()
    
    # Setup LLM
    try:
        print("Setting up LLM...")
        llm = setup_llm(config)
        print(f"LLM configured successfully")
    except Exception as e:
        print(f"ERROR: Failed to setup LLM - {e}")
        return 1
    
    # Setup paths
    chunks_dir = Path("../chunks")
    if not chunks_dir.exists():
        chunks_dir = Path("chunks")
    
    if not chunks_dir.exists():
        print("ERROR: chunks folder not found")
        print("Run: python src/2-chunking.py first")
        return 1
    
    contextual_dir = Path("../contextual_chunks")
    if not contextual_dir.exists():
        contextual_dir = Path("contextual_chunks")
    
    # Create contextual chunks directory
    contextual_dir.mkdir(exist_ok=True)
    
    print(f"Input folder: {chunks_dir}")
    print(f"Output folder: {contextual_dir}")
    print(f"Context window size: {config['CONTEXT_WINDOW_SIZE']} chunks")
    
    # Find chunk files
    chunk_files = list(chunks_dir.glob("*_chunks.json"))
    
    if not chunk_files:
        print("No chunk files found in chunks folder")
        return 0
    
    print(f"Found {len(chunk_files)} chunk files")
    
    # Process each chunk file
    processed_files = 0
    failed_files = 0
    
    for chunk_file in chunk_files:
        try:
            success = process_chunk_file(chunk_file, contextual_dir, llm, config)
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
    print(f"Total files:     {len(chunk_files)}")
    
    if failed_files > 0:
        print(f"\n{failed_files} files had errors")
        return 1
    else:
        print("\nAll files processed successfully!")
        return 0

if __name__ == "__main__":
    sys.exit(main())