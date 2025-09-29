#!/usr/bin/env python3
"""
Test CrewAI service to verify HR RAG tool is called only once.
"""

from services.crewai_service import CrewAIService

def test_single_tool_call():
    """Test that the HR RAG tool is called only once"""
    print("Testing CrewAI service with HR question...")
    
    # Initialize the service
    service = CrewAIService()
    
    # Test with an HR-related question
    hr_question = "What are the working hours mentioned in the HR bylaws?"
    
    print(f"\nQuestion: {hr_question}")
    print("-" * 50)
    
    # Call the service
    result = service.chat(hr_question)
    
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        print(f"Response: {result['response']}")
    else:
        print(f"Error: {result['error']}")
    
    print("-" * 50)
    print("Test completed. Check the verbose output above to see if the HR RAG tool was called only once.")

if __name__ == "__main__":
    test_single_tool_call()