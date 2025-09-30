#!/usr/bin/env python3
"""
Simple test to debug the NotFound error.
"""

from services.rag_v1.rag_service import government_document_tool

def test_government_document_tool_simple():
    """Test government document tool directly."""
    print("Testing government document tool directly...")
    
    question = "What are the working hours?"
    print(f"Question: {question}")
    
    result = government_document_tool._run(question)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_government_document_tool_simple()