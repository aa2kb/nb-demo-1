#!/usr/bin/env python3
"""
Test CrewAI integration with generalized government document tool.
"""

from services.crewai_service import CrewAIService

def test_crewai_government_search():
    """Test CrewAI agent with government document search."""
    print("Testing CrewAI integration with government document search...")
    
    # Initialize service
    service = CrewAIService()
    
    # Test information security question
    question = "What are the information security requirements and policies?"
    print(f"Question: {question}")
    
    # Execute through CrewAI agent
    result = service.chat(question)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_crewai_government_search()