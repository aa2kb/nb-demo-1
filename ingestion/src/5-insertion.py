#!/usr/bin/env python3
"""
Insert vectors and document data into PostgreSQL database.
Processes vector JSON files and inserts them into documents_sources and document_chunks tables.
"""

import os
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional

def load_config():
    """Load configuration from .env file."""
    env_path = Path("../.env")
    if not env_path.exists():
        env_path = Path(".env")
    
    if env_path.exists():
        load_dotenv(env_path)
    
    return {
        'DB_HOST': os.getenv('DB_HOST', 'localhost'),
        'DB_PORT': int(os.getenv('DB_PORT', 5432)),
        'DB_USER': os.getenv('DB_USER', 'admin'),
        'DB_PASSWORD': os.getenv('DB_PASSWORD', 'admin'),
        'DB_NAME': os.getenv('DB_NAME', 'postgres'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO')
    }

def connect_database(config):
    """Connect to PostgreSQL database."""
    try:
        import psycopg2
        from psycopg2.extras import Json
    except ImportError:
        print("ERROR: psycopg2 not installed. Run: pip install psycopg2-binary")
        sys.exit(1)
    
    try:
        conn = psycopg2.connect(
            host=config['DB_HOST'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
            database=config['DB_NAME']
        )
        return conn
    except Exception as e:
        print(f"ERROR: Failed to connect to database - {e}")
        sys.exit(1)

def check_pgvector_support(cursor):
    """Check if pgvector is installed and supported."""
    try:
        cursor.execute("SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';")
        result = cursor.fetchone()
        if result:
            print(f"pgvector extension found: v{result[1]}")
            return True
        else:
            print("pgvector extension not installed, using JSON storage")
            return False
    except Exception as e:
        print(f"WARNING: Error checking pgvector support - {e}")
        return False

def load_vectors_file(vectors_file_path):
    """Load vectors from JSON file."""
    try:
        with open(vectors_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"  ERROR: Failed to load vectors file - {e}")
        return None

def get_source_file_info(vectors_data, docs_dir):
    """Extract source file information from vectors data."""
    # Get source markdown filename from vectors data
    source_markdown = vectors_data.get('source_markdown', '')
    
    # Find the original PDF file
    if source_markdown.endswith('.md'):
        # Remove .md and find corresponding PDF
        base_name = source_markdown[:-3]  # Remove .md
        # Remove hash suffix (e.g., "_66d86f21")
        if '_' in base_name:
            pdf_base = '_'.join(base_name.split('_')[:-1])
        else:
            pdf_base = base_name
    else:
        pdf_base = source_markdown
    
    # Look for PDF file in docs directory
    possible_pdf_names = [
        f"{pdf_base}.pdf",
        f"{pdf_base}.PDF",
    ]
    
    pdf_path = None
    for pdf_name in possible_pdf_names:
        potential_path = docs_dir / pdf_name
        if potential_path.exists():
            pdf_path = potential_path
            break
    
    if not pdf_path:
        # Fallback: try to find any PDF with similar name
        for pdf_file in docs_dir.glob("*.pdf"):
            if pdf_base.lower().replace(' ', '').replace('_', '') in pdf_file.stem.lower().replace(' ', '').replace('_', ''):
                pdf_path = pdf_file
                break
        
        # Try with .PDF extension
        if not pdf_path:
            for pdf_file in docs_dir.glob("*.PDF"):
                if pdf_base.lower().replace(' ', '').replace('_', '') in pdf_file.stem.lower().replace(' ', '').replace('_', ''):
                    pdf_path = pdf_file
                    break
    
    if not pdf_path:
        print(f"  WARNING: Could not find original PDF for {source_markdown}")
        # Create dummy file info
        return {
            'file_name': f"{pdf_base}.pdf",
            'file_path': f"docs/{pdf_base}.pdf",
            'file_hash': 'unknown',
            'file_size': 0,
            'modified_at': datetime.now()
        }
    
    # Get file statistics
    stat = pdf_path.stat()
    
    # Calculate file hash
    hash_md5 = hashlib.md5()
    try:
        with open(pdf_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        file_hash = hash_md5.hexdigest()[:8]  # Short hash
    except Exception as e:
        print(f"  WARNING: Could not calculate hash for {pdf_path} - {e}")
        file_hash = 'unknown'
    
    return {
        'file_name': pdf_path.name,
        'file_path': str(pdf_path.relative_to(pdf_path.parent.parent)),  # Relative to project root
        'file_hash': file_hash,
        'file_size': stat.st_size,
        'modified_at': datetime.fromtimestamp(stat.st_mtime)
    }

def get_or_create_document_source(cursor, conn, vectors_data, docs_dir, use_pgvector):
    """Get existing document source or create new one."""
    # Get source file information
    file_info = get_source_file_info(vectors_data, docs_dir)
    
    # Check if document source already exists
    cursor.execute("""
        SELECT id, processing_status, total_chunks 
        FROM documents_sources 
        WHERE source_file_name = %s AND source_file_hash = %s
    """, (file_info['file_name'], file_info['file_hash']))
    
    existing = cursor.fetchone()
    
    if existing:
        doc_id, status, existing_chunks = existing
        total_chunks = len(vectors_data.get('chunks', []))
        
        print(f"  Found existing document source (ID: {doc_id})")
        print(f"  Status: {status}, Chunks: {existing_chunks}/{total_chunks}")
        
        # Update status if needed
        if status != 'completed' or existing_chunks != total_chunks:
            cursor.execute("""
                UPDATE documents_sources 
                SET processing_status = %s, total_chunks = %s, updated_at = CURRENT_TIMESTAMP
                WHERE id = %s
            """, ('processing', total_chunks, doc_id))
            conn.commit()
            print(f"  Updated document status to processing")
        
        return doc_id
    
    # Create new document source
    total_chunks = len(vectors_data.get('chunks', []))
    total_characters = sum(len(chunk.get('content', '')) for chunk in vectors_data.get('chunks', []))
    
    # Prepare metadata
    embedding_metadata = vectors_data.get('embedding_metadata', {})
    processing_metadata = vectors_data.get('processing_metadata', {})
    
    metadata = {
        'embedding_model': embedding_metadata.get('model', 'unknown'),
        'embedding_method': embedding_metadata.get('embedding_method', 'unknown'),
        'contextualization_method': processing_metadata.get('contextualization_method', 'unknown'),
        'llm_provider': processing_metadata.get('llm_provider', 'unknown'),
        'llm_model': processing_metadata.get('llm_model', 'unknown'),
        'use_pgvector': use_pgvector
    }
    
    cursor.execute("""
        INSERT INTO documents_sources (
            source_file_name, source_file_path, source_file_hash, 
            source_file_size, source_file_modified_at, processing_status,
            total_chunks, total_characters, extraction_method, metadata
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (
        file_info['file_name'], file_info['file_path'], file_info['file_hash'],
        file_info['file_size'], file_info['modified_at'], 'processing',
        total_chunks, total_characters, 'docling', json.dumps(metadata)
    ))
    
    doc_id = cursor.fetchone()[0]
    conn.commit()
    
    print(f"  Created new document source (ID: {doc_id})")
    return doc_id

def get_existing_chunks(cursor, doc_id):
    """Get set of chunk indices that already exist for this document."""
    cursor.execute("""
        SELECT chunk_index FROM document_chunks WHERE document_id = %s
    """, (doc_id,))
    
    return set(row[0] for row in cursor.fetchall())

def insert_chunk(cursor, conn, doc_id, chunk_data, use_pgvector):
    """Insert a single chunk into the database."""
    chunk_index = chunk_data.get('chunk_index')
    content = chunk_data.get('content', '')
    vector = chunk_data.get('vector', [])
    
    # Prepare chunk metadata
    chunk_metadata = {
        'content_contextualized': chunk_data.get('content_contextualized', ''),
        'original_metadata': chunk_data.get('metadata', {}),
        'embedding_metadata': chunk_data.get('embedding_metadata', {})
    }
    
    if use_pgvector and vector:
        # Insert with pgvector
        cursor.execute("""
            INSERT INTO document_chunks (
                document_id, chunk_index, content, embedding, chunk_metadata
            ) VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (document_id, chunk_index) 
            DO UPDATE SET 
                content = EXCLUDED.content,
                embedding = EXCLUDED.embedding,
                chunk_metadata = EXCLUDED.chunk_metadata
        """, (doc_id, chunk_index, content, vector, json.dumps(chunk_metadata)))
    else:
        # Insert with JSON embedding storage
        embedding_json = json.dumps(vector) if vector else None
        cursor.execute("""
            INSERT INTO document_chunks (
                document_id, chunk_index, content, embedding_json, chunk_metadata
            ) VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (document_id, chunk_index) 
            DO UPDATE SET 
                content = EXCLUDED.content,
                embedding_json = EXCLUDED.embedding_json,
                chunk_metadata = EXCLUDED.chunk_metadata
        """, (doc_id, chunk_index, content, embedding_json, json.dumps(chunk_metadata)))

def process_vectors_file(vectors_file_path, cursor, conn, docs_dir, use_pgvector):
    """Process a single vectors file and insert into database."""
    print(f"\nProcessing: {vectors_file_path.name}")
    
    # Load vectors data
    vectors_data = load_vectors_file(vectors_file_path)
    if not vectors_data:
        return False
    
    chunks = vectors_data.get('chunks', [])
    if not chunks:
        print(f"  No chunks found in file")
        return True
    
    print(f"  Found {len(chunks)} chunks")
    
    # Get or create document source
    doc_id = get_or_create_document_source(cursor, conn, vectors_data, docs_dir, use_pgvector)
    
    # Get existing chunks to skip
    existing_chunks = get_existing_chunks(cursor, doc_id)
    
    # Process chunks
    processed = 0
    skipped = 0
    failed = 0
    
    for chunk_data in chunks:
        chunk_index = chunk_data.get('chunk_index')
        
        if chunk_index in existing_chunks:
            print(f"    Chunk {chunk_index}: Skipping (already exists)")
            skipped += 1
            continue
        
        try:
            insert_chunk(cursor, conn, doc_id, chunk_data, use_pgvector)
            processed += 1
            
            if processed % 10 == 0:  # Commit every 10 chunks
                conn.commit()
                print(f"    Processed {processed} chunks...")
            
        except Exception as e:
            print(f"    Chunk {chunk_index}: Failed - {e}")
            failed += 1
            conn.rollback()  # Rollback failed transaction
    
    # Final commit
    conn.commit()
    
    # Update document source status
    if processed + skipped == len(chunks) and failed == 0:
        cursor.execute("""
            UPDATE documents_sources 
            SET processing_status = 'completed', updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
        """, (doc_id,))
        conn.commit()
        print(f"  Document marked as completed")
    
    print(f"  Processed: {processed}, Skipped: {skipped}, Failed: {failed}")
    
    return failed == 0

def main():
    print("Vector Database Insertion")
    print("=" * 50)
    
    # Load config
    config = load_config()
    
    # Setup database connection
    print("Connecting to database...")
    conn = connect_database(config)
    cursor = conn.cursor()
    
    # Check pgvector support
    use_pgvector = check_pgvector_support(cursor)
    
    # Setup paths
    vectors_dir = Path("../vectors")
    if not vectors_dir.exists():
        vectors_dir = Path("vectors")
    
    if not vectors_dir.exists():
        print("ERROR: vectors folder not found")
        print("Run: python src/4-vectorization.py first")
        return 1
    
    docs_dir = Path("../docs")
    if not docs_dir.exists():
        docs_dir = Path("docs")
    
    if not docs_dir.exists():
        print("ERROR: docs folder not found")
        return 1
    
    print(f"Vectors folder: {vectors_dir}")
    print(f"Docs folder: {docs_dir}")
    print(f"Using pgvector: {use_pgvector}")
    
    # Find vector files
    vector_files = list(vectors_dir.glob("*_vectors.json"))
    
    if not vector_files:
        print("No vector files found in vectors folder")
        return 0
    
    print(f"Found {len(vector_files)} vector files")
    
    # Process each vector file
    processed_files = 0
    failed_files = 0
    
    try:
        for vector_file in vector_files:
            try:
                success = process_vectors_file(vector_file, cursor, conn, docs_dir, use_pgvector)
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
                conn.rollback()
    
    finally:
        cursor.close()
        conn.close()
    
    # Summary
    print("\n" + "=" * 50)
    print("Results:")
    print(f"Files processed: {processed_files}")
    print(f"Files failed:    {failed_files}")
    print(f"Total files:     {len(vector_files)}")
    
    if failed_files > 0:
        print(f"\n{failed_files} files had errors")
        return 1
    else:
        print("\nAll files processed successfully!")
        return 0

if __name__ == "__main__":
    sys.exit(main())