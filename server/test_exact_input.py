#!/usr/bin/env python3
"""
Test the exact user input that causes the issue
"""

import sys
import os
sys.path.append('/Users/amin/projects/nb-2/server')

# Set environment variables
os.environ['DEFAULT_LLM_PROVIDER'] = 'groq'
os.environ['DEFAULT_LLM_MODEL'] = 'llama-3.1-8b-instant'
os.environ['GROQ_API_KEY'] = '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'
os.environ['PHOENIX_BASE_URL'] = 'http://localhost:6006'

try:
    from services.crewai_service import CrewAIService
    
    print("🧪 Testing CrewAI Service with exact user input...")
    service = CrewAIService()
    print("✅ Service initialized")
    
    # Test with exact input that causes the issue
    user_input = """according to hr law tell me about  
Priority for Vacant Positions"""
    
    print(f"🤔 Testing exact user input: '{user_input}'")
    result = service.chat(user_input)
    print(f"📝 Result: {result}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()