#!/usr/bin/env python3
"""
Test script to verify Ollama connectivity and Mistral model availability.
Run this script to ensure everything is working before starting the main application.
"""

import requests
import json


def test_ollama_connection():
    """Test if Ollama is running and accessible."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json()
            print("✅ Ollama is running and accessible")

            # Check if mistral:7b is available
            model_names = [model['name'] for model in models.get('models', [])]
            if 'mistral:7b' in model_names:
                print("✅ mistral:7b model is available")
                return True
            else:
                print("❌ mistral:7b model not found")
                print("Available models:", model_names)
                print("Run: ollama pull mistral:7b")
                return False
        else:
            print(f"❌ Ollama responded with status {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama at http://localhost:11434")
        print("Make sure Ollama is running: ollama serve")
        return False
    except Exception as e:
        print(f"❌ Error testing Ollama: {e}")
        return False


def test_mistral_generation():
    """Test Mistral model generation."""
    try:
        payload = {
            "model": "mistral:7b",
            "prompt": "What is artificial intelligence?",
            "stream": False
        }
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Mistral 7B generation test successful")
            print(f"Response: {result.get('response', 'No response')[:100]}...")
            return True
        else:
            print(f"❌ Generation failed with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing generation: {e}")
        return False


def main():
    """Run all tests."""
    print("🧪 Testing Ollama Setup for CrewAI")
    print("=" * 40)
    
    if test_ollama_connection():
        print()
        print("🧪 Testing Mistral 7B generation...")
        if test_mistral_generation():
            print()
            print("🎉 All tests passed! You can now run the CrewAI application.")
        else:
            print()
            print("⚠️  Ollama is running but generation failed.")
    else:
        print()
        print("⚠️  Please fix Ollama setup before running the application.")


if __name__ == "__main__":
    main()