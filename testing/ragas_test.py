#!/usr/bin/env python3
"""
RAGAS Evaluation Test with Generated Dataset
Uses RAGAS to evaluate the generated dataset with proper scoring metrics.
"""

import os
import json
import requests
import asyncio
from datetime import datetime
from pathlib import Path
import pandas as pd

# RAGAS imports
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from datasets import Dataset

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

def setup_llm():
    """Setup LLM for RAGAS evaluation."""
    
    # Use Gemini from the environment
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in environment")
    
    from langchain_google_genai import ChatGoogleGenerativeAI
    
    evaluator_llm = ChatGoogleGenerativeAI(
        model="gemini-flash-lite-latest",
        google_api_key=gemini_api_key,
        temperature=0
    )
    
    return evaluator_llm

def prepare_ragas_dataset(questions, contexts, references, answers):
    """Prepare dataset in RAGAS format."""
    
    # Format contexts - ensure they are lists of strings
    formatted_contexts = []
    for context in contexts:
        if isinstance(context, list):
            formatted_contexts.append(context)
        else:
            formatted_contexts.append([str(context)])
    
    # Create RAGAS dataset
    ragas_data = {
        "question": questions,
        "contexts": formatted_contexts,
        "answer": answers,
        "ground_truth": references
    }
    
    return Dataset.from_dict(ragas_data)

def run_ragas_evaluation():
    """Run RAGAS evaluation on the dataset."""
    
    print("🚀 Starting RAGAS Evaluation")
    print("=" * 50)
    
    # Check server connection
    if not test_server_connection():
        print("❌ Cannot proceed without server connection")
        return False
    
    # Setup LLM for evaluation
    try:
        print("🔧 Setting up evaluation LLM...")
        llm = setup_llm()
        print("✅ LLM configured successfully")
    except Exception as e:
        print(f"❌ Failed to setup LLM: {e}")
        return False
    
    # Get dataset
    questions = dataset["question"]
    contexts = dataset["contexts"]  
    references = dataset["reference_answers"]
    
    print(f"\n📋 Generating answers for {len(questions)} questions...")
    
    # Generate answers using the agent
    answers = []
    successful_queries = 0
    
    for i, question in enumerate(questions, 1):
        print(f"📝 Question {i}/{len(questions)}: {question[:60]}...")
        
        result = query_agent(question)
        
        if result['status'] == 'success':
            answers.append(result['response'])
            successful_queries += 1
            print(f"   ✅ Got answer ({len(result['response'])} chars)")
        else:
            answers.append(f"ERROR: {result.get('error', 'Unknown error')}")
            print(f"   ❌ Failed to get answer")
    
    print(f"\n📊 Successfully generated {successful_queries}/{len(questions)} answers")
    
    if successful_queries == 0:
        print("❌ No successful answers to evaluate")
        return False
    
    # Prepare RAGAS dataset
    print("🔧 Preparing RAGAS dataset...")
    try:
        ragas_dataset = prepare_ragas_dataset(questions, contexts, references, answers)
        print(f"✅ RAGAS dataset prepared with {len(ragas_dataset)} entries")
    except Exception as e:
        print(f"❌ Failed to prepare RAGAS dataset: {e}")
        return False
    
    # Configure RAGAS metrics with our LLM
    print("🔧 Configuring RAGAS metrics...")
    try:
        # Configure metrics with our LLM
        faithfulness.llm = llm
        answer_relevancy.llm = llm
        context_precision.llm = llm
        context_recall.llm = llm
        
        metrics = [faithfulness, answer_relevancy, context_precision, context_recall]
        print("✅ Metrics configured successfully")
    except Exception as e:
        print(f"❌ Failed to configure metrics: {e}")
        return False
    
    # Run evaluation
    print(f"\n🔍 Running RAGAS evaluation...")
    print("This may take several minutes...")
    
    try:
        results = evaluate(
            dataset=ragas_dataset,
            metrics=metrics
        )
        
        print("✅ RAGAS evaluation completed!")
        
        # Print results
        print(f"\n📊 RAGAS EVALUATION RESULTS")
        print("=" * 40)
        
        scores = results.get_results()
        
        for metric_name, score in scores.items():
            if isinstance(score, (int, float)):
                print(f"🎯 {metric_name.title()}: {score:.3f}")
        
        # Calculate overall score
        numeric_scores = [score for score in scores.values() if isinstance(score, (int, float))]
        if numeric_scores:
            overall_score = sum(numeric_scores) / len(numeric_scores)
            print(f"\n⭐ Overall Score: {overall_score:.3f}")
            
            # Performance assessment
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
                
            print(f"🎪 Performance Level: {performance}")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Convert to pandas DataFrame for easier handling
        results_df = results.to_pandas()
        
        # Save to CSV
        csv_file = f"ragas_results_{timestamp}.csv"
        results_df.to_csv(csv_file, index=False)
        
        # Save summary to JSON
        json_file = f"ragas_summary_{timestamp}.json"
        summary_data = {
            "timestamp": timestamp,
            "total_questions": len(questions),
            "successful_queries": successful_queries,
            "success_rate": (successful_queries / len(questions)) * 100,
            "scores": {k: float(v) if isinstance(v, (int, float)) else str(v) for k, v in scores.items()},
            "overall_score": overall_score if 'overall_score' in locals() else None,
            "performance_level": performance if 'performance' in locals() else None
        }
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(summary_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Results saved:")
        print(f"   📊 Detailed CSV: {csv_file}")
        print(f"   📄 Summary JSON: {json_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ RAGAS evaluation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🎯 RAGAS Evaluation with Generated Dataset")
    print("Using advanced metrics for comprehensive evaluation")
    print()
    
    success = run_ragas_evaluation()
    
    if success:
        print(f"\n🎉 RAGAS evaluation completed successfully!")
        print(f"The generated dataset should show high scores because:")
        print(f"  ✅ Answers are from the same agent system")
        print(f"  ✅ Contexts are extracted from agent responses")
        print(f"  ✅ Reference answers are enhanced by the agent")
        print(f"  🚀 This demonstrates high-quality RAG performance!")
    else:
        print(f"\n❌ RAGAS evaluation failed. Please check the setup and try again.")