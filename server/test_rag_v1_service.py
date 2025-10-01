#!/usr/bin/env python3
"""
Simple RAG v1 Service Test Script

This script directly tests the RAG v1 service with simple imports and execution.
"""

import os
import sys
import traceback
from pathlib import Path

# Add server directory to path for imports
sys.path.append(str(Path(__file__).parent))

def test_rag_v1_direct():
    """Test RAG v1 service directly."""
    print("🧪 Testing RAG v1 Service Directly")
    print("=" * 50)
    
    try:
        print("🔄 Importing RAG v1 service...")
        from services.rag_v1 import rag_document_tool
        print("✅ RAG v1 service imported successfully")
        
        # Test questions
        test_questions = [
            "What are the HR working hours?",
            "What are the procurement standards?",
            "What are the information security policies?"
        ]
        
        for i, question in enumerate(test_questions, 1):
            print(f"\n📋 Test {i}: {question}")
            print("-" * 40)
            
            try:
                print("🔄 Running RAG v1 query...")
                result = rag_document_tool._run(question)
                
                print(f"✅ Success: {len(result)} characters")
                print(f"📝 Preview: {result[:200]}...")
                
                if len(result) > 200:
                    print(f"📄 Full response: {result}")
                
            except Exception as e:
                print(f"❌ Query failed: {e}")
                print(f"🔍 Error type: {type(e).__name__}")
                if "format" in str(e) and "real number" in str(e):
                    print("� This is the SQL parameter formatting issue we identified")
                traceback.print_exc()
        
        return True
        
    except Exception as e:
        print(f"❌ RAG v1 import/setup failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run the simple RAG v1 test."""
    print("🚀 Simple RAG v1 Test")
    print("=" * 30)
    
    # Environment check
    print("🔧 Environment:")
    print(f"GEMINI_API_KEY: {'✅ Set' if os.getenv('GEMINI_API_KEY') else '❌ Missing'}")
    print(f"DATABASE_URL: {'✅ Set' if os.getenv('DATABASE_URL') else '❌ Missing'}")
    print()
    
    # Run test
    success = test_rag_v1_direct()
    
    print("\n" + "=" * 30)
    if success:
        print("✅ RAG v1 test completed")
    else:
        print("❌ RAG v1 test failed")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()