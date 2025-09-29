#!/usr/bin/env python3
"""
Simple test to debug the NotFound error.
"""

from services.rag_service import hr_rag_tool

def test_hr_rag_simple():
    """Test HR RAG tool directly."""
    print("Testing HR RAG tool directly...")
    
    question = "What are the working hours?"
    print(f"Question: {question}")
    
    result = hr_rag_tool._run(question)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_hr_rag_simple()