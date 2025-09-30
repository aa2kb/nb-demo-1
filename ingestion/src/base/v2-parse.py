#!/usr/bin/env python3
"""
PDF Document Parser using pure Mistral OCR API
Uploads PDFs to Mistral Files API and processes them with OCR API.
"""

import os
import sys
import logging
import json
import hashlib
import time
from pathlib import Path
from typing import Optional, Dict, Any

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
DOCS_FOLDER = "../../docs"
OUTPUT_FOLDER = "../../markdown-by-mistral-clean"
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_BASE = "https://api.mistral.ai/v1"

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main function to process all PDFs in the docs folder."""
    # Check for Mistral API key
    if not MISTRAL_API_KEY:
        logger.error("MISTRAL_API_KEY environment variable not set")
        sys.exit(1)
    
    # Setup paths
    script_dir = Path(__file__).parent
    docs_dir = script_dir / DOCS_FOLDER
    output_dir = script_dir / OUTPUT_FOLDER
    
    # Validate docs directory
    if not docs_dir.exists():
        logger.error(f"Docs directory not found: {docs_dir}")
        sys.exit(1)
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    logger.info(f"Output directory: {output_dir}")
    
    # Find PDF files
    pdf_files = list(docs_dir.glob("*.pdf")) + list(docs_dir.glob("*.PDF"))
    
    if not pdf_files:
        logger.warning(f"No PDF files found in {docs_dir}")
        return
    
    logger.info(f"Found {len(pdf_files)} PDF files to process")
    
    # Process each PDF
    success_count = 0
    for pdf_file in pdf_files:
        try:
            if process_pdf(str(pdf_file), str(output_dir)):
                success_count += 1
        except Exception as e:
            logger.error(f"Unexpected error processing {pdf_file.name}: {e}")
    
    logger.info(f"Processing complete: {success_count}/{len(pdf_files)} files successful")


def upload_file_to_mistral(file_path: str) -> Optional[str]:
    """
    Upload a file to Mistral Files API for OCR processing.
    
    Args:
        file_path: Path to the PDF file
        
    Returns:
        File ID if upload successful, None otherwise
    """
    if not MISTRAL_API_KEY:
        logger.error("MISTRAL_API_KEY environment variable not set")
        return None
    
    try:
        with open(file_path, 'rb') as file:
            files = {
                'file': (Path(file_path).name, file, 'application/pdf')
            }
            data = {
                'purpose': 'ocr'
            }
            
            response = requests.post(
                f"{MISTRAL_API_BASE}/files",
                headers={
                    "Authorization": f"Bearer {MISTRAL_API_KEY}"
                },
                files=files,
                data=data,
                timeout=300  # 5 minutes for large files
            )
            
            if response.status_code == 200:
                result = response.json()
                file_id = result.get('id')
                logger.info(f"Successfully uploaded {Path(file_path).name} with ID: {file_id}")
                return file_id
            else:
                logger.error(f"Failed to upload file: {response.status_code} - {response.text}")
                return None
                
    except Exception as e:
        logger.error(f"Failed to upload file {file_path}: {e}")
        return None


def process_with_ocr_api(file_id: str, filename: str) -> Optional[str]:
    """
    Process uploaded file using Mistral OCR API.
    
    Args:
        file_id: ID of the uploaded file
        filename: Original filename for context
        
    Returns:
        Processed markdown text or None if processing fails
    """
    if not MISTRAL_API_KEY:
        logger.error("MISTRAL_API_KEY environment variable not set")
        return None
        
    try:
        response = requests.post(
            f"{MISTRAL_API_BASE}/ocr",
            headers={
                "Authorization": f"Bearer {MISTRAL_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistral-ocr-latest",
                "document": {
                    "type": "file",
                    "file_id": file_id
                }
            },
            timeout=300  # 5 minutes for OCR processing
        )
        
        if response.status_code == 200:
            result = response.json()
            
            # Extract markdown from all pages
            markdown_content = ""
            pages = result.get("pages", [])
            
            for page in pages:
                page_index = page.get("index", 0)
                page_markdown = page.get("markdown", "")
                
                if page_markdown:
                    markdown_content += f"\n\n--- Page {page_index + 1} ---\n\n"
                    markdown_content += page_markdown
            
            if markdown_content.strip():
                # Add document header
                header = f"# {filename}\n\n*Processed with Mistral OCR API*\n"
                return header + markdown_content.strip()
            else:
                logger.warning(f"No content extracted from {filename}")
                return None
                
        else:
            logger.error(f"OCR API error: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        logger.error(f"Failed to process file with OCR API: {e}")
        return None


def delete_uploaded_file(file_id: str) -> bool:
    """
    Delete uploaded file from Mistral to clean up.
    
    Args:
        file_id: ID of the uploaded file
        
    Returns:
        True if deletion successful, False otherwise
    """
    if not MISTRAL_API_KEY:
        return False
        
    try:
        response = requests.delete(
            f"{MISTRAL_API_BASE}/files/{file_id}",
            headers={
                "Authorization": f"Bearer {MISTRAL_API_KEY}"
            },
            timeout=30
        )
        
        if response.status_code == 200:
            logger.info(f"Successfully deleted file {file_id}")
            return True
        else:
            logger.warning(f"Failed to delete file {file_id}: {response.status_code}")
            return False
            
    except Exception as e:
        logger.warning(f"Failed to delete file {file_id}: {e}")
        return False


def process_pdf(pdf_path: str, output_dir: str) -> bool:
    """
    Process a single PDF file using pure Mistral OCR workflow.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Output directory for markdown files
        
    Returns:
        True if processing was successful, False otherwise
    """
    pdf_file = Path(pdf_path)
    output_file = Path(output_dir) / f"{pdf_file.stem}.md"
    
    # Check if file already processed (simple check - if output exists)
    if output_file.exists():
        logger.info(f"Skipping {pdf_file.name} - output already exists")
        return True
    
    logger.info(f"Processing {pdf_file.name} with Mistral OCR API...")
    
    # Step 1: Upload file to Mistral
    logger.info(f"Uploading {pdf_file.name} to Mistral Files API...")
    file_id = upload_file_to_mistral(pdf_path)
    
    if not file_id:
        logger.error(f"Failed to upload {pdf_file.name}")
        return False
    
    try:
        # Step 2: Process with OCR API
        logger.info(f"Processing {pdf_file.name} with OCR API...")
        processed_text = process_with_ocr_api(file_id, pdf_file.name)
        
        if not processed_text:
            logger.error(f"Failed to process {pdf_file.name} with OCR API")
            return False
        
        # Step 3: Save processed markdown
        try:
            output_file.write_text(processed_text, encoding='utf-8')
            logger.info(f"Successfully processed {pdf_file.name} -> {output_file.name}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save output for {pdf_file.name}: {e}")
            return False
            
    finally:
        # Step 4: Clean up - delete uploaded file
        logger.info(f"Cleaning up uploaded file {file_id}...")
        delete_uploaded_file(file_id)


if __name__ == "__main__":
    main()
