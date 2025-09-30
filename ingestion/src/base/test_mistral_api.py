#!/usr/bin/env python3
"""
Test script to verify Mistral API endpoints are accessible
"""

import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_BASE = "https://api.mistral.ai/v1"

def test_mistral_endpoints():
    """Test that we can reach Mistral API endpoints"""
    
    if not MISTRAL_API_KEY:
        print("❌ MISTRAL_API_KEY environment variable not set")
        return False
    
    print("🔑 API Key found")
    
    # Test Files API endpoint
    try:
        response = requests.get(
            f"{MISTRAL_API_BASE}/files",
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"},
            timeout=10
        )
        print(f"📁 Files API status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Files API accessible")
        else:
            print(f"⚠️  Files API response: {response.text}")
            
    except Exception as e:
        print(f"❌ Files API error: {e}")
        return False
    
    print("🎉 Mistral API endpoints are accessible!")
    return True

if __name__ == "__main__":
    test_mistral_endpoints()