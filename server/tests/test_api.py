#!/usr/bin/env python3
"""
Test script for OpenAI-compatible API endpoints.
Tests the newly created OpenAI-compatible API with CrewAI integration.
"""

import requests
import json
import time
from typing import Dict, Any


class APITester:
    """Test client for the OpenAI-compatible API."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url.rstrip("/")
    
    def test_health_check(self) -> bool:
        """Test the health check endpoint."""
        try:
            response = requests.get(f"{self.base_url}/v1/health", timeout=10)
            if response.status_code == 200:
                print("✅ Health check passed")
                print(f"   Response: {response.json()}")
                return True
            else:
                print(f"❌ Health check failed with status {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Health check error: {e}")
            return False
    
    def test_list_models(self) -> Dict[str, Any]:
        """Test the models listing endpoint."""
        try:
            response = requests.get(f"{self.base_url}/v1/models", timeout=10)
            if response.status_code == 200:
                data = response.json()
                print("✅ Models listing successful")
                print(f"   Found {len(data.get('data', []))} models:")
                for model in data.get('data', []):
                    print(f"   - {model['id']}")
                return data
            else:
                print(f"❌ Models listing failed with status {response.status_code}")
                print(f"   Error: {response.text}")
                return {}
        except Exception as e:
            print(f"❌ Models listing error: {e}")
            return {}
    
    def test_chat_completion(self, model_name: str) -> bool:
        """Test chat completion endpoint (non-streaming)."""
        try:
            payload = {
                "model": model_name,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "What is artificial intelligence? Please keep your answer brief."}
                ],
                "max_tokens": 150,
                "temperature": 0.7,
                "stream": False
            }
            
            response = requests.post(
                f"{self.base_url}/v1/chat/completions",
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Chat completion successful")
                print(f"   Model: {data.get('model')}")
                print(f"   Response: {data['choices'][0]['message']['content'][:100]}...")
                print(f"   Tokens: {data.get('usage', {})}")
                return True
            else:
                print(f"❌ Chat completion failed with status {response.status_code}")
                print(f"   Error: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Chat completion error: {e}")
            return False
    
    def test_streaming_chat_completion(self, model_name: str) -> bool:
        """Test streaming chat completion endpoint."""
        try:
            payload = {
                "model": model_name,
                "messages": [
                    {"role": "user", "content": "Count from 1 to 5, one number per response."}
                ],
                "max_tokens": 50,
                "temperature": 0.1,
                "stream": True
            }
            
            response = requests.post(
                f"{self.base_url}/v1/chat/completions",
                json=payload,
                stream=True,
                timeout=60
            )
            
            if response.status_code == 200:
                print("✅ Streaming chat completion started")
                print("   Stream content:")
                
                chunks_received = 0
                for line in response.iter_lines():
                    if line:
                        line_str = line.decode('utf-8')
                        if line_str.startswith('data: '):
                            data_str = line_str[6:]  # Remove 'data: ' prefix
                            if data_str.strip() == '[DONE]':
                                print("   Stream ended with [DONE]")
                                break
                            try:
                                chunk_data = json.loads(data_str)
                                chunks_received += 1
                                if chunks_received <= 5:  # Show first few chunks
                                    content = chunk_data.get('choices', [{}])[0].get('delta', {}).get('content', '')
                                    if content:
                                        print(f"   Chunk {chunks_received}: '{content}'")
                            except json.JSONDecodeError:
                                continue
                
                print(f"✅ Streaming completed with {chunks_received} chunks")
                return True
            else:
                print(f"❌ Streaming failed with status {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Streaming error: {e}")
            return False
    
    def test_get_specific_model(self, model_name: str) -> bool:
        """Test getting information about a specific model."""
        try:
            response = requests.get(f"{self.base_url}/v1/models/{model_name}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                print("✅ Model retrieval successful")
                print(f"   Model ID: {data.get('id')}")
                print(f"   Owned by: {data.get('owned_by')}")
                return True
            else:
                print(f"❌ Model retrieval failed with status {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Model retrieval error: {e}")
            return False


def main():
    """Run all tests for the OpenAI-compatible API."""
    print("🧪 Testing OpenAI-Compatible API with CrewAI Integration")
    print("=" * 60)
    
    tester = APITester()
    
    # Test 1: Health Check
    print("\n1. Testing Health Check...")
    health_ok = tester.test_health_check()
    
    if not health_ok:
        print("\n⚠️  Health check failed. Make sure:")
        print("   - The server is running (python main.py)")
        print("   - Ollama is running (ollama serve)")
        return
    
    # Test 2: List Models
    print("\n2. Testing Models Listing...")
    models_data = tester.test_list_models()
    
    if not models_data.get('data'):
        print("\n⚠️  No models found. Make sure:")
        print("   - Ollama has models installed (e.g., ollama pull gemma3:27b)")
        return
    
    # Use the first available model for further testing
    test_model = models_data['data'][0]['id']
    print(f"\n📋 Using model '{test_model}' for further testing...")
    
    # Test 3: Get Specific Model
    print(f"\n3. Testing Model Retrieval for '{test_model}'...")
    tester.test_get_specific_model(test_model)
    
    # Test 4: Chat Completion (Non-streaming)
    print(f"\n4. Testing Chat Completion (Non-streaming) with '{test_model}'...")
    chat_ok = tester.test_chat_completion(test_model)
    
    # Test 5: Streaming Chat Completion
    if chat_ok:
        print(f"\n5. Testing Streaming Chat Completion with '{test_model}'...")
        tester.test_streaming_chat_completion(test_model)
    else:
        print("\n5. Skipping streaming test due to previous failure")
    
    print("\n🎉 OpenAI-Compatible API Testing Complete!")
    print("\nYou can now use this API with any OpenAI-compatible client by pointing it to:")
    print(f"   Base URL: http://localhost:8000/v1")
    print(f"   Available models: {', '.join([m['id'] for m in models_data.get('data', [])])}")


if __name__ == "__main__":
    main()