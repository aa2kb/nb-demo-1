"""
Simple Ragas Evaluation Test using SingleTurnSample API
Tests: Faithfulness, Factual Correctness, and Simple Criteria Score
Exports to JSON and CSV
"""

import os
import json
import csv
import asyncio
import requests
from datetime import datetime
from pathlib import Path
import pandas as pd

from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import Faithfulness, SimpleCriteriaScore
from ragas.metrics._factual_correctness import FactualCorrectness

# Import dataset
from dataset import dataset

# Environment setup
from dotenv import load_dotenv
load_dotenv(Path("../server/.env"))

def setup_evaluator_llm():
    """Setup LLM for evaluation based on environment configuration."""
    
    llm_provider = os.getenv("DEFAULT_LLM_PROVIDER", "gemini")
    llm_model = os.getenv("DEFAULT_LLM_MODEL", "gemini-flash-lite-latest")
    
    print(f"🤖 Setting up evaluator with {llm_provider} - {llm_model}")
    
    if llm_provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")
        
        evaluator_llm = ChatGoogleGenerativeAI(
            model=llm_model,
            google_api_key=gemini_api_key,
            temperature=0
        )
        
    else:
        from langchain_community.llms import Ollama
        
        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
        evaluator_llm = Ollama(
            model=llm_model,
            base_url=ollama_base_url,
            temperature=0
        )
    
    return evaluator_llm

def create_http_agent():
    """Create HTTP client for CrewAI server."""
    
    class CrewAIHTTPClient:
        def __init__(self):
            self.base_url = "http://localhost:8000"
            
        def chat(self, question):
            try:
                response = requests.post(
                    f"{self.base_url}/v1/chat/completions",
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
                            "response": content
                        }
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
            except Exception as e:
                return {
                    "status": "error",
                    "error": f"Request failed: {str(e)}"
                }
    
    try:
        requests.get("http://localhost:8000/v1/health", timeout=5)
        print("✅ Connected to CrewAI server via HTTP")
        return CrewAIHTTPClient()
    except:
        print("❌ Cannot connect to CrewAI server. Please start the server first.")
        return None

async def evaluate_single_sample(sample, evaluator_llm):
    """Evaluate a single sample with all three metrics."""
    
    # Initialize metrics
    faithfulness_scorer = Faithfulness(llm=evaluator_llm)
    factual_correctness_scorer = FactualCorrectness(llm=evaluator_llm, mode="precision")
    simple_criteria_scorer = SimpleCriteriaScore(
        name="response_quality", 
        definition="Score the response quality from 0-1 based on clarity, completeness, and accuracy",
        llm=evaluator_llm
    )
    
    results = {}
    
    try:
        # Faithfulness evaluation
        faithfulness_result = await faithfulness_scorer.single_turn_ascore(sample)
        results['faithfulness'] = float(faithfulness_result)
        print(f"   🎯 Faithfulness: {faithfulness_result:.3f}")
    except Exception as e:
        print(f"   ❌ Faithfulness error: {e}")
        results['faithfulness'] = None
    
    try:
        # Factual Correctness evaluation
        factual_result = await factual_correctness_scorer.single_turn_ascore(sample)
        results['factual_correctness'] = float(factual_result)
        print(f"   🔍 Factual Correctness: {factual_result:.3f}")
    except Exception as e:
        print(f"   ❌ Factual Correctness error: {e}")
        results['factual_correctness'] = None
    
    try:
        # Simple Criteria Score evaluation
        criteria_result = await simple_criteria_scorer.single_turn_ascore(sample)
        results['response_quality'] = float(criteria_result)
        print(f"   ⭐ Response Quality: {criteria_result:.3f}")
    except Exception as e:
        print(f"   ❌ Response Quality error: {e}")
        results['response_quality'] = None
    
    return results

async def main():
    """Main evaluation pipeline."""
    
    print("🚀 Starting Simple Ragas Evaluation")
    print("=" * 50)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        # 1. Setup evaluator LLM
        print("\n🔧 Setting up evaluator LLM...")
        evaluator_llm = setup_evaluator_llm()
        
        # 2. Setup CrewAI agent
        print("\n🤖 Setting up CrewAI agent...")
        agent = create_http_agent()
        if not agent:
            print("❌ Cannot proceed without CrewAI agent")
            return 1
        
        # 3. Extract data from dataset
        questions = dataset["question"]
        contexts = dataset["contexts"]
        references = dataset["reference_answers"]
        
        print(f"\n📋 Dataset loaded: {len(questions)} questions")
        
        # 4. Generate answers and evaluate
        print(f"\n🔄 Processing {len(questions)} questions...")
        
        all_results = []
        
        for i, (question, context, reference) in enumerate(zip(questions, contexts, references), 1):
            print(f"\n📝 Question {i}/{len(questions)}: {question[:60]}...")
            
            # Generate answer using CrewAI agent
            result = agent.chat(question)
            
            if result['status'] == 'success':
                answer = result['response']
                print(f"✅ Generated answer ({len(answer)} chars)")
                
                # Create SingleTurnSample
                sample = SingleTurnSample(
                    user_input=question,
                    response=answer,
                    reference=reference,
                    retrieved_contexts=context
                )
                
                # Evaluate the sample
                print("🔍 Evaluating...")
                scores = await evaluate_single_sample(sample, evaluator_llm)
                
                # Store results
                question_result = {
                    "question_id": i,
                    "question": question,
                    "answer": answer,
                    "reference": reference,
                    "context": context,
                    "faithfulness": scores.get('faithfulness'),
                    "factual_correctness": scores.get('factual_correctness'),
                    "response_quality": scores.get('response_quality')
                }
                
                all_results.append(question_result)
                
            else:
                print(f"❌ Error generating answer: {result.get('error')}")
                # Still add to results with error
                question_result = {
                    "question_id": i,
                    "question": question,
                    "answer": f"ERROR: {result.get('error')}",
                    "reference": reference,
                    "context": context,
                    "faithfulness": None,
                    "factual_correctness": None,
                    "response_quality": None
                }
                all_results.append(question_result)
        
        # 5. Calculate summary statistics
        print(f"\n📊 EVALUATION SUMMARY")
        print("=" * 40)
        
        valid_results = [r for r in all_results if r['faithfulness'] is not None]
        
        if valid_results:
            avg_faithfulness = sum(r['faithfulness'] for r in valid_results) / len(valid_results)
            avg_factual = sum(r['factual_correctness'] for r in valid_results if r['factual_correctness'] is not None) / len([r for r in valid_results if r['factual_correctness'] is not None])
            avg_quality = sum(r['response_quality'] for r in valid_results if r['response_quality'] is not None) / len([r for r in valid_results if r['response_quality'] is not None])
            
            print(f"🎯 Average Faithfulness:      {avg_faithfulness:.3f}")
            print(f"🔍 Average Factual Correctness: {avg_factual:.3f}")
            print(f"⭐ Average Response Quality:   {avg_quality:.3f}")
            
            summary_stats = {
                "timestamp": timestamp,
                "total_questions": len(questions),
                "successful_evaluations": len(valid_results),
                "average_scores": {
                    "faithfulness": avg_faithfulness,
                    "factual_correctness": avg_factual,
                    "response_quality": avg_quality
                }
            }
        else:
            print("❌ No valid results to summarize")
            summary_stats = {
                "timestamp": timestamp,
                "total_questions": len(questions),
                "successful_evaluations": 0,
                "average_scores": {
                    "faithfulness": None,
                    "factual_correctness": None,
                    "response_quality": None
                }
            }
        
        # 6. Export results
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        
        # Export to JSON
        json_file = results_dir / f"evaluation_{timestamp}.json"
        export_data = {
            "summary": summary_stats,
            "detailed_results": all_results
        }
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Results exported to JSON: {json_file}")
        
        # Export to CSV
        csv_file = results_dir / f"evaluation_{timestamp}.csv"
        
        # Flatten data for CSV
        csv_data = []
        for result in all_results:
            csv_row = {
                "question_id": result["question_id"],
                "question": result["question"],
                "answer": result["answer"],
                "reference": result["reference"],
                "context": "; ".join(result["context"]) if isinstance(result["context"], list) else str(result["context"]),
                "faithfulness": result["faithfulness"],
                "factual_correctness": result["factual_correctness"],
                "response_quality": result["response_quality"]
            }
            csv_data.append(csv_row)
        
        # Write CSV
        df = pd.DataFrame(csv_data)
        df.to_csv(csv_file, index=False, encoding='utf-8')
        
        print(f"💾 Results exported to CSV: {csv_file}")
        
        print(f"\n🎉 Evaluation completed successfully!")
        print(f"📁 Results saved with timestamp: {timestamp}")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Evaluation failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(asyncio.run(main()))