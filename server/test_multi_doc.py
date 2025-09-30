#!/usr/bin/env python3
"""
Test multi-document RAG with procurement question.
"""

from services.rag_v1.rag_service import government_document_tool

def test_procurement_question():
    """Test with a procurement-related question that should use multiple docs."""
    print("Testing multi-document RAG with procurement question...")
    
    question = "What are the procurement procedures and standards for government purchases?"
    print(f"Question: {question}")
    
    result = government_document_tool._run(question)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_procurement_question()