#!/usr/bin/env python3
"""
Simple 3-Score Evaluation Test
Just similarity, relevance, and criteria scores saved to CSV in results folder.
"""

import requests
import pandas as pd
from datetime import datetime
from pathlib import Path
from dataset import dataset

# Configuration: Set to None to run all questions, or set a number to limit
TEST_LIMIT = 20  # Change this to limit number of questions (e.g., 5, 10, etc.)

def query_agent(question):
    """Query the agent server."""
    try:
        response = requests.post(
            "http://localhost:8000/v1/chat/completions",
            json={
                "model": "abu-dhabi-gov", 
                "messages": [{"role": "user", "content": question}],
                "stream": False
            },
            timeout=120
        )
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None
    except:
        return None

def similarity_score(reference, response):
    """Simple similarity based on word overlap."""
    ref_words = set(reference.lower().split())
    resp_words = set(response.lower().split())
    
    intersection = len(ref_words & resp_words)
    union = len(ref_words | resp_words)
    
    if union == 0:
        return 0.0
    
    jaccard = intersection / union
    length_ratio = min(len(response), len(reference)) / max(len(response), len(reference))
    
    return (jaccard * 0.7) + (length_ratio * 0.3)

def relevance_score(question, response):
    """Simple relevance based on question word overlap."""
    question_words = set(question.lower().split())
    response_words = set(response.lower().split())
    
    overlap = len(question_words & response_words)
    total_q_words = len(question_words)
    
    if total_q_words == 0:
        return 0.0
    
    relevance = overlap / total_q_words
    
    if len(response) > 200:
        relevance *= 1.2
    
    return min(1.0, relevance)

def criteria_score(question, response, reference):
    """Simple criteria score based on response completeness."""
    score = 0.0
    
    # Length bonus (responses should be detailed)
    if len(response) > 100:
        score += 0.3
    if len(response) > 300:
        score += 0.2
    
    # Key question words in response
    question_words = question.lower().split()
    response_lower = response.lower()
    
    key_word_matches = sum(1 for word in question_words if word in response_lower)
    if len(question_words) > 0:
        score += (key_word_matches / len(question_words)) * 0.3
    
    # Reference similarity component
    ref_words = set(reference.lower().split())
    resp_words = set(response.lower().split())
    
    if len(ref_words) > 0:
        word_overlap = len(ref_words & resp_words) / len(ref_words)
        score += word_overlap * 0.2
    
    return min(1.0, score)

def main():
    print("🎯 Simple 3-Score Evaluation")
    print("=" * 40)
    
    # Check server
    try:
        requests.get("http://localhost:8000/v1/health", timeout=5)
        print("✅ Server accessible")
    except:
        print("❌ Server not accessible")
        return
    
    questions = dataset["question"]
    references = dataset["reference_answers"]
    contexts = dataset["contexts"]
    
    # Apply limit if set
    if TEST_LIMIT is not None:
        questions = questions[:TEST_LIMIT]
        references = references[:TEST_LIMIT]
        contexts = contexts[:TEST_LIMIT]
        print(f"\n⚠️  Limited to first {TEST_LIMIT} questions")
    
    print(f"\n📋 Processing {len(questions)} questions...")
    
    results = []
    
    for i, (question, reference, context) in enumerate(zip(questions, references, contexts), 1):
        print(f"\n📝 {i}/{len(questions)}")
        
        # Get agent response
        response = query_agent(question)
        
        if response:
            # Calculate 3 scores
            sim_score = similarity_score(reference, response)
            rel_score = relevance_score(question, response) 
            crit_score = criteria_score(question, response, reference)
            
            print(f"   Similarity: {sim_score:.3f}")
            print(f"   Relevance:  {rel_score:.3f}")
            print(f"   Criteria:   {crit_score:.3f}")
            
            results.append({
                "question": question,
                "context": context,
                "reference_answer": reference,
                "agent_response": response,
                "similarity_score": sim_score,
                "relevance_score": rel_score, 
                "criteria_score": crit_score
            })
        else:
            print("   ❌ Failed")
            results.append({
                "question": question,
                "context": context,
                "reference_answer": reference,
                "agent_response": "Failed to get response",
                "similarity_score": 0.0,
                "relevance_score": 0.0,
                "criteria_score": 0.0
            })
    
    # Save to CSV in results folder
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = results_dir / f"simple_scores_{timestamp}.csv"
    
    df = pd.DataFrame(results)
    df.to_csv(csv_file, index=False)
    
    # Print summary
    print(f"\n📊 SUMMARY")
    print(f"   Avg Similarity: {df['similarity_score'].mean():.3f}")
    print(f"   Avg Relevance:  {df['relevance_score'].mean():.3f}")  
    print(f"   Avg Criteria:   {df['criteria_score'].mean():.3f}")
    
    print(f"\n💾 Saved to: {csv_file}")

if __name__ == "__main__":
    main()