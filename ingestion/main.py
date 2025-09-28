#!/usr/bin/env python3
"""
Main entry point for the document ingestion CLI.

Usage:
    python main.py ingest /path/to/documents
    python main.py stats
    python main.py test
"""

from src.cli import cli

if __name__ == "__main__":
    cli()