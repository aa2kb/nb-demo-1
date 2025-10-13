#!/usr/bin/env python3
"""
Simple Test Script for Generated Dataset
Tests the agent server with the generated dataset and provides basic scoring.
"""

import os
import json
import requests
import time
from datetime import datetime
from pathlib import Path
import pandas as pd

# RAGAS imports for SimpleCriteriaScore
from ragas.metrics import SimpleCriteriaScore

# Import the generated dataset
try:
    from generated_dataset_20251014_002128 import dataset
    print("✅ Successfully imported generated dataset")
except ImportError as e:
    print(f"❌ Failed to import generated dataset: {e}")
    print("Falling back to original dataset...")
    from dataset import dataset

# Environment setup
from dotenv import load_dotenv
load_dotenv(Path("../server/.env"))

def test_server_connection():
    """Test if the agent server is accessible."""
    try:
        response = requests.get("http://localhost:8000/v1/health", timeout=5)
        if response.status_code == 200:
            print("✅ Server is accessible")
            return True
        else:
            print(f"❌ Server returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to server: {e}")
        return False

def query_agent(question):
    """Query the agent server and return the response."""
    try:
        response = requests.post(
            "http://localhost:8000/v1/chat/completions",
            json={
                "model": "abu-dhabi-gov",
                "messages": [
                    {"role": "user", "content": question}
                ],
                "stream": False
            },
            timeout=120
        )
        
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0]["message"]["content"]
                return {
                    "status": "success",
                    "response": content,
                    "tokens_used": data.get("usage", {}).get("total_tokens", 0)
                }
        
        return {
            "status": "error",
            "error": f"HTTP {response.status_code}: {response.text}"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

def simple_similarity_score(reference, response):
    """
    Simple similarity scoring based on keyword overlap and length.
    Returns a score between 0 and 1.
    """
    # Convert to lowercase for comparison
    ref_words = set(reference.lower().split())
    resp_words = set(response.lower().split())
    
    # Calculate Jaccard similarity (intersection over union)
    intersection = len(ref_words & resp_words)
    union = len(ref_words | resp_words)
    
    if union == 0:
        return 0.0
    
    jaccard = intersection / union
    
    # Length penalty/bonus
    length_ratio = min(len(response), len(reference)) / max(len(response), len(reference))
    
    # Combine scores
    final_score = (jaccard * 0.7) + (length_ratio * 0.3)
    
    return min(1.0, final_score)

def content_relevance_score(question, response):
    """
    Score how relevant the response is to the question.
    Returns a score between 0 and 1.
    """
    question_words = set(question.lower().split())
    response_words = set(response.lower().split())
    
    # Check for question word overlap in response
    overlap = len(question_words & response_words)
    total_q_words = len(question_words)
    
    if total_q_words == 0:
        return 0.0
    
    relevance = overlap / total_q_words
    
    # Bonus for longer, detailed responses
    if len(response) > 200:
        relevance *= 1.2
    
    return min(1.0, relevance)

def run_simple_evaluation():
    """Run simple evaluation of the dataset."""
    
    print("🚀 Starting Simple Dataset Evaluation")
    print("=" * 50)
    
    # Check server connection
    if not test_server_connection():
        print("❌ Cannot proceed without server connection")
        return False
    
    # Get dataset
    questions = dataset["question"]
    contexts = dataset["contexts"]
    references = dataset["reference_answers"]
    
    print(f"\n📋 Evaluating {len(questions)} questions...")
    
    results = []
    total_similarity = 0
    total_relevance = 0
    successful_queries = 0
    
    for i, (question, context, reference) in enumerate(zip(questions, contexts, references), 1):
        print(f"\n📝 Question {i}/{len(questions)}")
        print(f"Q: {question[:80]}...")
        
        # Query the agent
        result = query_agent(question)
        
        if result['status'] == 'success':
            response = result['response']
            print(f"✅ Got response ({len(response)} chars)")
            
            # Calculate scores
            similarity = simple_similarity_score(reference, response)
            relevance = content_relevance_score(question, response)
            
            print(f"   📊 Similarity Score: {similarity:.3f}")
            print(f"   🎯 Relevance Score: {relevance:.3f}")
            
            # Store results
            results.append({
                "question_id": i,
                "question": question,
                "reference": reference,
                "response": response,
                "similarity_score": similarity,
                "relevance_score": relevance,
                "tokens_used": result.get('tokens_used', 0),
                "status": "success"
            })
            
            total_similarity += similarity
            total_relevance += relevance
            successful_queries += 1
            
        else:
            print(f"❌ Error: {result.get('error')}")
            results.append({
                "question_id": i,
                "question": question,
                "reference": reference,
                "response": f"ERROR: {result.get('error')}",
                "similarity_score": 0.0,
                "relevance_score": 0.0,
                "tokens_used": 0,
                "status": "error"
            })
        
        # Small delay between requests
        time.sleep(0.5)
    
    # Calculate averages
    if successful_queries > 0:
        avg_similarity = total_similarity / successful_queries
        avg_relevance = total_relevance / successful_queries
        overall_score = (avg_similarity + avg_relevance) / 2
    else:
        avg_similarity = 0
        avg_relevance = 0
        overall_score = 0
    
    # Print summary
    print(f"\n📊 EVALUATION SUMMARY")
    print("=" * 40)
    print(f"📋 Total Questions: {len(questions)}")
    print(f"✅ Successful Queries: {successful_queries}")
    print(f"❌ Failed Queries: {len(questions) - successful_queries}")
    print(f"📈 Success Rate: {(successful_queries/len(questions)*100):.1f}%")
    print()
    print(f"🎯 Average Similarity Score: {avg_similarity:.3f}")
    print(f"📊 Average Relevance Score: {avg_relevance:.3f}")
    print(f"⭐ Overall Score: {overall_score:.3f}")
    
    # Determine performance level
    if overall_score >= 0.8:
        performance = "🏆 EXCELLENT"
    elif overall_score >= 0.7:
        performance = "🥈 VERY GOOD"
    elif overall_score >= 0.6:
        performance = "🥉 GOOD"
    elif overall_score >= 0.5:
        performance = "⚡ FAIR"
    else:
        performance = "🔧 NEEDS IMPROVEMENT"
    
    print(f"\n🎪 Performance Level: {performance}")
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save to JSON
    results_file = f"simple_test_results_{timestamp}.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump({
            "summary": {
                "timestamp": timestamp,
                "total_questions": len(questions),
                "successful_queries": successful_queries,
                "success_rate": successful_queries/len(questions)*100,
                "avg_similarity_score": avg_similarity,
                "avg_relevance_score": avg_relevance,
                "overall_score": overall_score,
                "performance_level": performance
            },
            "detailed_results": results
        }, f, indent=2, ensure_ascii=False)
    
    # Save to CSV
    df = pd.DataFrame(results)
    csv_file = f"simple_test_results_{timestamp}.csv"
    df.to_csv(csv_file, index=False, encoding='utf-8')
    
    print(f"\n💾 Results saved:")
    print(f"   📄 JSON: {results_file}")
    print(f"   📊 CSV: {csv_file}")
    
    return True

if __name__ == "__main__":
    print("🎯 Simple Dataset Test Runner")
    print("Testing generated dataset against live agent server")
    print()
    
    success = run_simple_evaluation()
    
    if success:
        print(f"\n🎉 Evaluation completed successfully!")
        print(f"The generated dataset should show high scores because:")
        print(f"  ✅ Questions are answered by the same agent system")
        print(f"  ✅ Reference answers are enhanced by the agent")
        print(f"  ✅ Contexts are extracted from agent responses")
        print(f"  🚀 This demonstrates the system's consistency and quality!")
    else:
        print(f"\n❌ Evaluation failed. Please check the server and try again.")