#!/usr/bin/env python3
"""
Token Counter Script

Analyzes markdown files in multiple directories and provides detailed token statistics
using tiktoken for accurate token counting compatible with OpenAI models.
"""

import os
import sys
import csv
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime
import tiktoken

try:
    import tiktoken
except ImportError:
    print("❌ tiktoken not installed. Please run: pip install tiktoken")
    sys.exit(1)


@dataclass
class FileStats:
    """Statistics for a single file."""
    path: Path
    size_bytes: int
    char_count: int
    word_count: int
    token_count: int
    line_count: int


@dataclass
class DirectoryStats:
    """Statistics for a directory."""
    path: Path
    file_count: int
    total_size_bytes: int
    total_char_count: int
    total_word_count: int
    total_token_count: int
    total_line_count: int
    files: List[FileStats]


class TokenCounter:
    """Token counter for markdown files using tiktoken."""
    
    def __init__(self, encoding_name: str = "cl100k_base"):
        """
        Initialize token counter.
        
        Args:
            encoding_name: Tiktoken encoding to use (cl100k_base for GPT-4, GPT-3.5-turbo)
        """
        try:
            self.encoding = tiktoken.get_encoding(encoding_name)
            self.encoding_name = encoding_name
        except Exception as e:
            print(f"❌ Failed to load encoding {encoding_name}: {e}")
            print("🔄 Falling back to cl100k_base encoding...")
            self.encoding = tiktoken.get_encoding("cl100k_base")
            self.encoding_name = "cl100k_base"
    
    def count_tokens(self, text: str) -> int:
        """Count tokens in text using tiktoken."""
        try:
            return len(self.encoding.encode(text))
        except Exception as e:
            print(f"⚠️  Error counting tokens: {e}")
            return 0
    
    def analyze_file(self, file_path: Path) -> FileStats:
        """Analyze a single markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Calculate statistics
            size_bytes = file_path.stat().st_size
            char_count = len(content)
            word_count = len(content.split())
            token_count = self.count_tokens(content)
            line_count = len(content.splitlines())
            
            return FileStats(
                path=file_path,
                size_bytes=size_bytes,
                char_count=char_count,
                word_count=word_count,
                token_count=token_count,
                line_count=line_count
            )
            
        except Exception as e:
            print(f"⚠️  Error analyzing {file_path}: {e}")
            return FileStats(
                path=file_path,
                size_bytes=0,
                char_count=0,
                word_count=0,
                token_count=0,
                line_count=0
            )
    
    def analyze_directory(self, dir_path: Path) -> DirectoryStats:
        """Analyze all markdown files in a directory."""
        if not dir_path.exists():
            print(f"⚠️  Directory not found: {dir_path}")
            return DirectoryStats(
                path=dir_path,
                file_count=0,
                total_size_bytes=0,
                total_char_count=0,
                total_word_count=0,
                total_token_count=0,
                total_line_count=0,
                files=[]
            )
        
        # Find all markdown files
        markdown_files = list(dir_path.glob("*.md")) + list(dir_path.glob("*.markdown"))
        
        if not markdown_files:
            print(f"📝 No markdown files found in {dir_path}")
            return DirectoryStats(
                path=dir_path,
                file_count=0,
                total_size_bytes=0,
                total_char_count=0,
                total_word_count=0,
                total_token_count=0,
                total_line_count=0,
                files=[]
            )
        
        # Analyze each file
        file_stats = []
        for file_path in sorted(markdown_files):
            stats = self.analyze_file(file_path)
            file_stats.append(stats)
        
        # Calculate totals
        total_size_bytes = sum(f.size_bytes for f in file_stats)
        total_char_count = sum(f.char_count for f in file_stats)
        total_word_count = sum(f.word_count for f in file_stats)
        total_token_count = sum(f.token_count for f in file_stats)
        total_line_count = sum(f.line_count for f in file_stats)
        
        return DirectoryStats(
            path=dir_path,
            file_count=len(file_stats),
            total_size_bytes=total_size_bytes,
            total_char_count=total_char_count,
            total_word_count=total_word_count,
            total_token_count=total_token_count,
            total_line_count=total_line_count,
            files=file_stats
        )
    
    def format_bytes(self, bytes_count: int) -> str:
        """Format bytes in human readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_count < 1024.0:
                return f"{bytes_count:.1f} {unit}"
            bytes_count /= 1024.0
        return f"{bytes_count:.1f} TB"
    
    def print_file_stats(self, stats: FileStats, show_details: bool = True):
        """Print statistics for a single file."""
        if show_details:
            print(f"    📄 {stats.path.name}")
            print(f"       Size: {self.format_bytes(stats.size_bytes)}")
            print(f"       Lines: {stats.line_count:,}")
            print(f"       Characters: {stats.char_count:,}")
            print(f"       Words: {stats.word_count:,}")
            print(f"       Tokens: {stats.token_count:,}")
        else:
            print(f"    📄 {stats.path.name:<40} {stats.token_count:>8,} tokens")
    
    def print_directory_stats(self, stats: DirectoryStats, show_file_details: bool = True):
        """Print statistics for a directory."""
        print(f"\n📁 {stats.path.name}/")
        print("=" * 60)
        
        if stats.file_count == 0:
            print("   (No markdown files found)")
            return
        
        print(f"Files: {stats.file_count}")
        print(f"Total Size: {self.format_bytes(stats.total_size_bytes)}")
        print(f"Total Lines: {stats.total_line_count:,}")
        print(f"Total Characters: {stats.total_char_count:,}")
        print(f"Total Words: {stats.total_word_count:,}")
        print(f"Total Tokens: {stats.total_token_count:,}")
        
        if show_file_details and stats.files:
            print(f"\n📋 File Details:")
            for file_stats in stats.files:
                self.print_file_stats(file_stats, show_details=True)
    
    def print_summary(self, all_stats: List[DirectoryStats]):
        """Print overall summary across all directories."""
        print("\n" + "=" * 80)
        print("📊 OVERALL SUMMARY")
        print("=" * 80)
        
        total_files = sum(s.file_count for s in all_stats)
        total_size = sum(s.total_size_bytes for s in all_stats)
        total_chars = sum(s.total_char_count for s in all_stats)
        total_words = sum(s.total_word_count for s in all_stats)
        total_tokens = sum(s.total_token_count for s in all_stats)
        total_lines = sum(s.total_line_count for s in all_stats)
        
        print(f"📁 Directories analyzed: {len(all_stats)}")
        print(f"📄 Total markdown files: {total_files}")
        print(f"💾 Total size: {self.format_bytes(total_size)}")
        print(f"📏 Total lines: {total_lines:,}")
        print(f"🔤 Total characters: {total_chars:,}")
        print(f"📝 Total words: {total_words:,}")
        print(f"🎯 Total tokens: {total_tokens:,}")
        print(f"🔧 Encoding used: {self.encoding_name}")
        
        # Cost estimation for OpenAI APIs (rough estimates)
        print(f"\n💰 Rough Cost Estimates (if all content was processed):")
        print(f"   GPT-4 Input: ~${total_tokens * 0.00003:.2f}")
        print(f"   GPT-3.5-turbo Input: ~${total_tokens * 0.0000015:.4f}")
        
        # Show directory comparison
        if len(all_stats) > 1:
            print(f"\n📊 Directory Comparison:")
            for stats in sorted(all_stats, key=lambda x: x.total_token_count, reverse=True):
                if stats.file_count > 0:
                    percentage = (stats.total_token_count / total_tokens) * 100
                    print(f"   {stats.path.name:<25} {stats.total_token_count:>8,} tokens ({percentage:>5.1f}%)")
    
    def export_to_csv(self, all_stats: List[DirectoryStats], output_file: str = "token_analysis.csv"):
        """Export all statistics to a CSV file."""
        csv_path = Path(output_file)
        
        try:
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'directory', 'filename', 'file_path', 'size_bytes', 'size_human',
                    'lines', 'characters', 'words', 'tokens', 'tokens_per_kb',
                    'analysis_date', 'encoding_used'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                analysis_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Write individual file data
                for dir_stats in all_stats:
                    for file_stats in dir_stats.files:
                        tokens_per_kb = (file_stats.token_count / (file_stats.size_bytes / 1024)) if file_stats.size_bytes > 0 else 0
                        
                        writer.writerow({
                            'directory': dir_stats.path.name,
                            'filename': file_stats.path.name,
                            'file_path': str(file_stats.path.relative_to(Path.cwd())),
                            'size_bytes': file_stats.size_bytes,
                            'size_human': self.format_bytes(file_stats.size_bytes),
                            'lines': file_stats.line_count,
                            'characters': file_stats.char_count,
                            'words': file_stats.word_count,
                            'tokens': file_stats.token_count,
                            'tokens_per_kb': round(tokens_per_kb, 2),
                            'analysis_date': analysis_date,
                            'encoding_used': self.encoding_name
                        })
                
                # Add summary rows
                writer.writerow({})  # Empty row separator
                
                # Directory summaries
                writer.writerow({
                    'directory': 'DIRECTORY_SUMMARIES',
                    'filename': '',
                    'file_path': '',
                    'size_bytes': '',
                    'size_human': '',
                    'lines': '',
                    'characters': '',
                    'words': '',
                    'tokens': '',
                    'tokens_per_kb': '',
                    'analysis_date': '',
                    'encoding_used': ''
                })
                
                for dir_stats in all_stats:
                    if dir_stats.file_count > 0:
                        tokens_per_kb = (dir_stats.total_token_count / (dir_stats.total_size_bytes / 1024)) if dir_stats.total_size_bytes > 0 else 0
                        writer.writerow({
                            'directory': f"TOTAL_{dir_stats.path.name}",
                            'filename': f"{dir_stats.file_count} files",
                            'file_path': str(dir_stats.path.relative_to(Path.cwd())),
                            'size_bytes': dir_stats.total_size_bytes,
                            'size_human': self.format_bytes(dir_stats.total_size_bytes),
                            'lines': dir_stats.total_line_count,
                            'characters': dir_stats.total_char_count,
                            'words': dir_stats.total_word_count,
                            'tokens': dir_stats.total_token_count,
                            'tokens_per_kb': round(tokens_per_kb, 2),
                            'analysis_date': analysis_date,
                            'encoding_used': self.encoding_name
                        })
                
                # Overall total
                total_files = sum(s.file_count for s in all_stats)
                total_size = sum(s.total_size_bytes for s in all_stats)
                total_chars = sum(s.total_char_count for s in all_stats)
                total_words = sum(s.total_word_count for s in all_stats)
                total_tokens = sum(s.total_token_count for s in all_stats)
                total_lines = sum(s.total_line_count for s in all_stats)
                tokens_per_kb = (total_tokens / (total_size / 1024)) if total_size > 0 else 0
                
                writer.writerow({})  # Empty row separator
                writer.writerow({
                    'directory': 'GRAND_TOTAL',
                    'filename': f"{total_files} files across {len(all_stats)} directories",
                    'file_path': 'All directories',
                    'size_bytes': total_size,
                    'size_human': self.format_bytes(total_size),
                    'lines': total_lines,
                    'characters': total_chars,
                    'words': total_words,
                    'tokens': total_tokens,
                    'tokens_per_kb': round(tokens_per_kb, 2),
                    'analysis_date': analysis_date,
                    'encoding_used': self.encoding_name
                })
                
            print(f"\n💾 CSV exported to: {csv_path.absolute()}")
            print(f"📊 Contains {total_files} files + directory summaries + grand total")
            
        except Exception as e:
            print(f"❌ Failed to export CSV: {e}")


def main():
    """Main function to analyze markdown files in specified directories."""
    print("🎯 Token Counter for Markdown Files")
    print("=" * 80)
    
    # Initialize token counter
    counter = TokenCounter()
    print(f"🔧 Using encoding: {counter.encoding_name}")
    
    # Define directories to analyze
    base_dir = Path(__file__).parent
    directories = [
        base_dir / "markdown",
        base_dir / "markdown-by-mistral",
        base_dir / "markdown-by-llamaindex-parse"
    ]
    
    # Analyze each directory
    all_stats = []
    for dir_path in directories:
        print(f"\n🔍 Analyzing {dir_path}...")
        stats = counter.analyze_directory(dir_path)
        all_stats.append(stats)
        counter.print_directory_stats(stats, show_file_details=True)
    
    # Print overall summary
    counter.print_summary(all_stats)
    
    # Export to CSV
    counter.export_to_csv(all_stats)
    
    print(f"\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
