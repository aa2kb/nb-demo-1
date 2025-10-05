#!/usr/bin/env python3
"""
Test the actual CrewAI service with Groq
"""

import sys
import os
sys.path.append('/Users/amin/projects/nb-2/server')

# Set environment variables
os.environ['DEFAULT_LLM_PROVIDER'] = 'groq'
os.environ['DEFAULT_LLM_MODEL'] = 'llama-3.1-8b-instant'
os.environ['GROQ_API_KEY'] = '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'

try:
    from services.crewai_service import CrewAIService
    
    print("🧪 Testing CrewAI Service with Groq...")
    service = CrewAIService()
    print("✅ Service initialized")
    
    # Test simple question
    print("🤔 Testing HR question...")
    result = service.chat("according to hr law tell me about Priority for Vacant Positions")
    print(f"📝 Result: {result}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()