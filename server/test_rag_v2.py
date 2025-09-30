#!/usr/bin/env python3
"""
Test script for RAG v2 Full Document Service
"""

import sys
import os
from pathlib import Path

# Add the server directory to the path
server_dir = Path(__file__).parent
sys.path.insert(0, str(server_dir))

from services.rag_v2 import full_document_tool


def test_rag_v2():
    """Test the RAG v2 full document approach."""
    print("🧪 Testing RAG v2 Full Document Service")
    print("=" * 60)
    
    # Test questions
    test_questions = [
        "What are the core principles of Abu Dhabi procurement?",
        "What is the Code of Business Ethics for procurement practitioners?", 
        "What are the requirements for HR bylaw compliance?",
        "What are the information security standards?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n🔍 Test {i}: {question}")
        print("-" * 40)
        
        try:
            response = full_document_tool._run(question)
            print(f"✅ Response received ({len(response)} characters)")
            print(f"📝 Response preview: {response[:200]}...")
            if "Sources:" in response:
                sources = response.split("Sources:")[-1].strip()
                print(f"📚 Sources: {sources}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()


if __name__ == "__main__":
    test_rag_v2()