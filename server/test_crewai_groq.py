#!/usr/bin/env python3
"""
Test script for CrewAI with Groq
"""

import os
from crewai import Agent, LLM

# Set environment variables
os.environ['DEFAULT_LLM_PROVIDER'] = 'groq'
os.environ['DEFAULT_LLM_MODEL'] = 'llama-3.1-8b-instant'
os.environ['GROQ_API_KEY'] = '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'

def test_groq_llm():
    """Test Groq LLM with CrewAI"""
    print("🧪 Testing Groq LLM with CrewAI...")
    
    try:
        # Create LLM
        llm = LLM(
            model='groq/llama-3.1-8b-instant',
            api_key=os.getenv('GROQ_API_KEY'),
            temperature=0.7
        )
        print("✅ LLM created successfully")
        
        # Create simple agent without Phoenix dependencies
        agent = Agent(
            role="HR Assistant",
            goal="Answer questions about HR policies",
            backstory="You are an expert HR assistant for Abu Dhabi government",
            verbose=True,
            allow_delegation=False,
            llm=llm,
            max_iter=1,
            memory=False
        )
        print("✅ Agent created successfully")
        
        # Test simple question
        print("🤔 Testing simple question...")
        result = agent.kickoff("What is your role?")
        print(f"📝 Result: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_groq_llm()