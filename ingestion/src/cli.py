"""Main CLI application for document ingestion."""

import logging
import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

from .config import settings
from .database import db_manager
from .document_processor import DocumentProcessor
from .embedding_service import EmbeddingService
from .vector_store import VectorStoreManager

console = Console()


def setup_logging(log_level: str = "INFO"):
    """Setup logging with Rich handler."""
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console, rich_tracebacks=True)]
    )


@click.group()
@click.option("--log-level", default="INFO", help="Logging level")
def cli(log_level: str):
    """Document Ingestion CLI - Process and store documents as vectors."""
    setup_logging(log_level)


@cli.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option("--force", "-f", is_flag=True, help="Re-process documents even if they already exist")
@click.option("--dry-run", is_flag=True, help="Show what would be processed without actually doing it")
def ingest(directory: str, force: bool, dry_run: bool):
    """Ingest documents from a directory into the vector store."""
    
    directory_path = Path(directory)
    logger = logging.getLogger(__name__)
    
    console.print(f"🚀 Starting document ingestion from: {directory_path}", style="bold blue")
    logger.info(f"Ingestion started - Directory: {directory_path}, Force: {force}, Dry-run: {dry_run}")
    
    try:
        # Initialize services
        console.print("📦 Initializing services...", style="yellow")
        logger.info("Initializing DocumentProcessor")
        processor = DocumentProcessor()
        
        logger.info("Initializing VectorStoreManager")
        vector_store = VectorStoreManager()
        
        # Test connections first
        console.print("🔍 Testing connections...", style="yellow")
        logger.info("Starting connection tests")
        
        logger.info("Testing database connection...")
        if not db_manager.test_connection():
            logger.error("Database connection test failed")
            console.print("❌ Database connection failed", style="red")
            sys.exit(1)
        logger.info("Database connection test passed")
        
        logger.info("Testing embedding service...")
        if not vector_store.embedding_service.test_embedding():
            logger.error("Embedding service test failed")
            console.print("❌ Embedding service test failed", style="red")
            sys.exit(1)
        logger.info("Embedding service test passed")
        
        console.print("✅ All connections verified", style="green")
        logger.info("All connection tests passed successfully")
        
        # Process documents
        console.print(f"📄 Processing documents from: {directory_path}", style="cyan")
        logger.info(f"Starting document processing from directory: {directory_path}")
        processed_docs = processor.process_directory(directory_path)
        logger.info(f"Document processing completed. Found {len(processed_docs)} processed documents")
        
        if not processed_docs:
            console.print("⚠️ No documents were processed", style="yellow")
            return
        
        # Show what will be processed
        table = Table(title=f"Documents to Process ({'DRY RUN' if dry_run else 'PROCESSING'})")
        table.add_column("Document", style="cyan")
        table.add_column("Chunks", justify="right")
        table.add_column("Status", style="magenta")
        
        for doc in processed_docs:
            # Check if document exists
            exists = vector_store.check_document_exists(doc.document_id) if not dry_run else False
            
            if exists and not force:
                status = "EXISTS (skipping)"
                style = "yellow"
            elif dry_run:
                status = "WOULD PROCESS"
                style = "blue"
            else:
                status = "PROCESSING"
                style = "green"
            
            table.add_row(
                doc.name,
                str(len(doc.chunks)),
                f"[{style}]{status}[/{style}]"
            )
        
        console.print(table)
        
        if dry_run:
            console.print("🔍 Dry run completed - no documents were actually processed")
            return
        
        # Store documents
        stored_count = 0
        skipped_count = 0
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Storing documents...", total=len(processed_docs))
            
            for doc in processed_docs:
                # Check if document exists and force is not set
                if not force and vector_store.check_document_exists(doc.document_id):
                    skipped_count += 1
                    progress.update(task, advance=1)
                    continue
                
                # Delete existing if force is set
                if force and vector_store.check_document_exists(doc.document_id):
                    vector_store.delete_document(doc.document_id)
                
                progress.update(task, description=f"Processing {doc.name}...")
                
                if vector_store.store_document(doc):
                    stored_count += 1
                
                progress.update(task, advance=1)
        
        # Summary
        console.print(f"✅ Ingestion completed!", style="bold green")
        console.print(f"   📁 Processed: {len(processed_docs)} documents")
        console.print(f"   💾 Stored: {stored_count} documents")
        console.print(f"   ⏭️ Skipped: {skipped_count} documents")
        
    except Exception as e:
        console.print(f"❌ Error during ingestion: {e}", style="red")
        logger.exception("Full error traceback:")
        sys.exit(1)


@cli.command()
def stats():
    """Show statistics about stored documents."""
    try:
        vector_store = VectorStoreManager()
        stats_data = vector_store.get_stats()
        
        if "error" in stats_data:
            console.print(f"❌ Error getting stats: {stats_data['error']}", style="red")
            return
        
        # Summary stats
        console.print(f"📊 Vector Store Statistics", style="bold blue")
        console.print(f"   📄 Documents: {stats_data['unique_documents']}")
        console.print(f"   📝 Total Chunks: {stats_data['total_chunks']}")
        
        # Document details table
        if stats_data['document_details']:
            table = Table(title="Document Details")
            table.add_column("Document Name", style="cyan")
            table.add_column("Chunks", justify="right", style="magenta")
            
            for doc_detail in stats_data['document_details']:
                table.add_row(doc_detail['name'], str(doc_detail['chunks']))
            
            console.print(table)
        else:
            console.print("No documents found in the vector store")
            
    except Exception as e:
        console.print(f"❌ Error getting statistics: {e}", style="red")


@cli.command()
def test():
    """Test all service connections and configurations."""
    console.print("🧪 Testing ingestion services...", style="bold blue")
    
    success = True
    
    # Test database connection
    console.print("🔍 Testing database connection...")
    if db_manager.test_connection():
        console.print("   ✅ Database connection: OK", style="green")
    else:
        console.print("   ❌ Database connection: FAILED", style="red")
        success = False
    
    # Test database setup
    console.print("🔍 Testing database setup...")
    if db_manager.ensure_database_setup():
        console.print("   ✅ Database setup: OK", style="green")
    else:
        console.print("   ❌ Database setup: FAILED", style="red")
        success = False
    
    # Test embedding service
    console.print("🔍 Testing embedding service...")
    try:
        embedding_service = EmbeddingService()
        if embedding_service.test_embedding():
            console.print("   ✅ Embedding service: OK", style="green")
        else:
            console.print("   ❌ Embedding service: FAILED", style="red")
            success = False
    except Exception as e:
        console.print(f"   ❌ Embedding service: FAILED ({e})", style="red")
        success = False
    
    # Test vector store
    console.print("🔍 Testing vector store...")
    try:
        vector_store = VectorStoreManager()
        console.print("   ✅ Vector store initialization: OK", style="green")
    except Exception as e:
        console.print(f"   ❌ Vector store initialization: FAILED ({e})", style="red")
        success = False
    
    if success:
        console.print("🎉 All tests passed!", style="bold green")
    else:
        console.print("❌ Some tests failed. Check your configuration.", style="bold red")
        sys.exit(1)


@cli.command()
@click.argument("document_id")
def delete(document_id: str):
    """Delete a document from the vector store by document ID."""
    try:
        vector_store = VectorStoreManager()
        
        if vector_store.delete_document(document_id):
            console.print(f"✅ Document {document_id} deleted successfully", style="green")
        else:
            console.print(f"⚠️ Document {document_id} not found or could not be deleted", style="yellow")
            
    except Exception as e:
        console.print(f"❌ Error deleting document: {e}", style="red")


if __name__ == "__main__":
    cli()