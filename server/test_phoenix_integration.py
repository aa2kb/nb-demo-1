#!/usr/bin/env python3
"""
Test script for Phoenix integration with Document Detection Service.
"""

import os
from services.rag_v1.document_detection_service import DocumentDetectionService

def test_phoenix_integration():
    """Test Phoenix integration modes."""
    print("🧪 Testing Document Detection Service with Phoenix Integration")
    print("=" * 60)
    
    # Test 1: Keyword Fallback mode
    print("\n1️⃣ Testing Keyword Fallback Mode")
    os.environ['USE_PHOENIX_PROMPTS'] = 'false'
    service = DocumentDetectionService()
    print(f"   Phoenix enabled: {service.use_phoenix}")
    print(f"   Available documents: {len(service.available_documents)}")
    
    # Test 2: Phoenix mode (will fallback if not configured)
    print("\n2️⃣ Testing Phoenix Mode")
    os.environ['USE_PHOENIX_PROMPTS'] = 'true'
    service_phoenix = DocumentDetectionService()
    print(f"   Phoenix enabled: {service_phoenix.use_phoenix}")
    print(f"   Phoenix prompt ID: {service_phoenix.phoenix_prompt_id}")
    
    # Test 3: Actual document detection
    print("\n3️⃣ Testing Document Detection")
    test_questions = [
        "What are the working hours?",
        "What are procurement procedures?", 
        "What are security policies?",
        "Tell me about government services"
    ]
    
    # Test with fallback mode
    print("   🔄 Fallback Mode Results:")
    os.environ['USE_PHOENIX_PROMPTS'] = 'false'
    service = DocumentDetectionService()
    for question in test_questions:
        result = service.detect_relevant_documents(question)
        print(f"     '{question}' -> {result}")
    
    print("\n✅ Phoenix integration test completed!")
    print("\n📋 Configuration Guide:")
    print("   - Set USE_PHOENIX_PROMPTS=true to enable Phoenix")
    print("   - Set PHOENIX_DOCUMENT_DETECTION_PROMPT_ID to your prompt version")
    print("   - Set OPENAI_API_KEY for Phoenix inference")
    print("   - Falls back to keyword detection if Phoenix fails or is disabled")
    print("   - No LLM configuration needed for document detection!")

if __name__ == "__main__":
    test_phoenix_integration()