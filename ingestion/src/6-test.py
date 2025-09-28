import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
from typing import List, Dict, Any, Tuple
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.core.vector_stores import VectorStoreQuery
from llama_index.core.postprocessor.llm_rerank import LLMRerank
from llama_index.llms.ollama import Ollama


query = "Please tell me HR Bylaws for Priority for Vacant Positions"

# Global query variable
def main():
    """Semantic search using LlamaIndex PGVectorStore."""
    print("Semantic Search with LlamaIndex PGVectorStore")
    print("=" * 60)
    
    # Load config
    config = load_config()
    
    # Setup embedding model
    print("Setting up embedding model...")
    embedding_model = setup_embedding_model(config)
    
    # Setup LlamaIndex PGVectorStore
    print("Creating LlamaIndex PGVectorStore...")
    vector_store = create_vector_store(config)
    
    # Check database stats
    vector_status = check_vector_availability(vector_store)
    print(f"Vector database: {vector_status}")
    
    print(f"\nSearching for: '{query}'")
    
    try:
        # Generate query embedding
        print(f"\nGenerating embedding for query...")
        query_embedding = generate_query_embedding(embedding_model, query)
        if not query_embedding:
            print("Failed to generate query embedding")
            return
        
        # Search using LlamaIndex PGVectorStore (get more results for reranking)
        print("Searching with LlamaIndex PGVectorStore...")
        original_results = search_similar_chunks_llamaindex(vector_store, query_embedding, top_k=10)
        
        if not original_results:
            print("❌ No results found")
            print("Note: LlamaIndex PGVectorStore table might be empty.")
            print("You may need to run the insertion script first.")
            return
        
        # Setup LLM for reranking  
        print("\nSetting up LLM for reranking...")
        llm = setup_llm(config)
        
        # Use custom reranking to preserve all results
        print("Custom LLM scoring all results...")
        print(f"Input to reranker: {len(original_results)} results")
        reranked_results = rerank_results_custom(llm, original_results, query)
        print(f"Output from reranker: {len(reranked_results)} results")
        
        # Print comparison table for all 10 positions
        print_comparison_table(original_results, reranked_results, query)
        
        # Show LLM scores for all reranked results
        print("\n🎯 ALL RERANKED RESULTS WITH LLM SCORES:")
        for i, result in enumerate(reranked_results):
            llm_score = result.get('llm_score', 0.0)
            sim_score = result['similarity_score'] * 100
            print(f"  [{i+1:2d}] LLM: {llm_score:.1f}/10 | Sim: {sim_score:.1f}% | {result['source_file'][:30]}")
        
        # Print full results summary
        print(f"\n📊 FULL RESULTS SUMMARY:")
        print(f"Original results: {len(original_results)}")
        print(f"Reranked results: {len(reranked_results)}")
        
        # Show all position mappings in compact format
        print("\n🔄 ALL POSITION CHANGES (Original → Reranked):")
        position_changes = []
        for new_pos, reranked_result in enumerate(reranked_results):
            for orig_pos, orig_result in enumerate(original_results):
                if orig_result['id'] == reranked_result['id']:
                    position_changes.append(f"{orig_pos}→{new_pos}")
                    break
        
        # Print all position changes (should be 10 items)
        if len(position_changes) <= 10:
            print(" ".join(f"{change:>6}" for change in position_changes))
        else:
            # If more than 10, show in rows of 10
            for i in range(0, len(position_changes), 10):
                chunk = position_changes[i:i+10]
                print(" ".join(f"{change:>6}" for change in chunk))
        
        # Save results to file
        print("\n💾 Saving results to file...")
        saved_file = save_results_to_file(query, original_results, reranked_results)
        if saved_file:
            print(f"✅ Results saved to: {saved_file}")
        
        print(f"\n✅ Found {len(original_results)} original results, reranked all {len(reranked_results)}")
        print(f"Original best match: {original_results[0]['similarity_score']*100:.1f}% similarity")
        if reranked_results:
            print(f"Reranked results: All {len(reranked_results)} results reordered by LLM scoring")
    
    except KeyboardInterrupt:
        print("\nSearch interrupted by user")
    except Exception as e:
        print(f"ERROR: Search failed - {e}")
    
    print("\nSearch completed!")

def load_config():
    """Load configuration from .env file."""
    env_path = Path("../.env")
    if not env_path.exists():
        env_path = Path(".env")
    
    if env_path.exists():
        load_dotenv(env_path)
    
    return {
        'DB_HOST': os.getenv('DB_HOST', 'localhost'),
        'DB_PORT': int(os.getenv('DB_PORT', 5432)),
        'DB_USER': os.getenv('DB_USER', 'admin'),
        'DB_PASSWORD': os.getenv('DB_PASSWORD', 'admin'),
        'DB_NAME': os.getenv('DB_NAME', 'postgres'),
        'VECTOR_TABLE_NAME': os.getenv('VECTOR_TABLE_NAME', 'vectors'),
        'OLLAMA_HOST': os.getenv('OLLAMA_HOST', 'http://localhost:11434'),
        'EMBEDDING_MODEL': os.getenv('EMBEDDING_MODEL', 'embeddinggemma:300m'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO')
    }

def setup_embedding_model(config):
    """Setup embedding model for query vectorization."""
    try:
        embedding_model = OllamaEmbedding(
            model_name=config['EMBEDDING_MODEL'],
            base_url=config['OLLAMA_HOST']
        )
        print(f"✅ Connected to Ollama embedding model: {config['EMBEDDING_MODEL']}")
        return embedding_model
    except Exception as e:
        print(f"ERROR: Failed to setup embedding model - {e}")
        sys.exit(1)

def setup_llm(config):
    """Setup LLM for reranking."""
    try:
        llm = Ollama(
            model="mistral:7b",
            base_url=config['OLLAMA_HOST']
        )
        print(f"✅ Connected to Ollama LLM: mistral:7b")
        return llm
    except Exception as e:
        print(f"ERROR: Failed to setup LLM - {e}")
        sys.exit(1)

def create_vector_store(config):
    """Create LlamaIndex PGVectorStore for searching."""
    try:
        # Create PGVectorStore with consistent configuration
        vector_store = PGVectorStore.from_params(
            database=config['DB_NAME'],
            host=config['DB_HOST'],
            password=config['DB_PASSWORD'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            table_name=config['VECTOR_TABLE_NAME'],  # This creates data_vectors table
            embed_dim=768,
            hybrid_search=False,
            text_search_config="english"
        )
        
        print("✅ Connected to LlamaIndex PGVectorStore")
        print(f"   Database: {config['DB_NAME']}@{config['DB_HOST']}:{config['DB_PORT']}")
        print(f"   Table: data_vectors")
        return vector_store
        
    except Exception as e:
        print(f"ERROR: Failed to create PGVectorStore - {e}")
        sys.exit(1)

def check_vector_availability(vector_store):
    """Check if vectors are available in the store."""
    try:
        # Create a test query to check if the store has data
        test_query = VectorStoreQuery(
            query_embedding=[0.0] * 768,  # Dummy embedding
            similarity_top_k=1,
            mode="default"
        )
        
        # Try to execute a minimal query
        result = vector_store.query(test_query)
        
        # Check if the query returned any results
        if hasattr(result, 'nodes') and result.nodes:
            return "Available (contains data)"
        else:
            return "Empty (no data found)"
            
    except Exception as e:
        return "Not accessible or not initialized"



def generate_query_embedding(embedding_model, query: str) -> List[float]:
    """Generate embedding for the query string."""
    try:
        print(f"Generating embedding for query: '{query[:50]}{'...' if len(query) > 50 else ''}'")
        embedding = embedding_model.get_text_embedding(query)
        print(f"Generated {len(embedding)}-dimensional embedding")
        return embedding
    except Exception as e:
        print(f"ERROR: Failed to generate query embedding - {e}")
        return []

def search_similar_chunks_llamaindex(vector_store, query_embedding: List[float], top_k: int = 25) -> List[Dict]:
    """Search for similar chunks using LlamaIndex PGVectorStore."""
    try:
        # Create a VectorStoreQuery
        query_obj = VectorStoreQuery(
            query_embedding=query_embedding,
            similarity_top_k=top_k,
            mode="default"
        )
        
        # Execute the query
        print(f"  Executing similarity search for top {top_k} results...")
        query_result = vector_store.query(query_obj)
        
        search_results = []
        
        # Handle case where no results are returned
        if not query_result.nodes:
            print("  No nodes returned from vector store")
            return []
        
        print(f"  Found {len(query_result.nodes)} matching nodes")
        
        for i, node in enumerate(query_result.nodes):
            # Get similarity score if available
            similarity = query_result.similarities[i] if query_result.similarities and i < len(query_result.similarities) else 0.0
            
            # Extract metadata from the node
            metadata = node.metadata if hasattr(node, 'metadata') else {}
            
            # Parse metadata if it's a JSON string
            if isinstance(metadata, dict):
                parsed_metadata = metadata
            elif isinstance(metadata, str):
                try:
                    parsed_metadata = json.loads(metadata)
                except json.JSONDecodeError:
                    parsed_metadata = {}
            else:
                parsed_metadata = {}
            
            search_results.append({
                'id': getattr(node, 'node_id', f'node_{i}'),
                'chunk_index': parsed_metadata.get('chunk_index', i),
                'content': node.text if hasattr(node, 'text') else str(node),
                'content_contextualized': parsed_metadata.get('content_contextualized', ''),
                'source_file': parsed_metadata.get('source_file', parsed_metadata.get('source_file_name', 'Unknown')),
                'source_path': parsed_metadata.get('source_file_path', ''),
                'similarity_score': float(similarity) if similarity is not None else 0.0,
                'metadata': parsed_metadata
            })
        
        return search_results
        
    except Exception as e:
        print(f"ERROR: Failed to search with LlamaIndex PGVectorStore - {e}")
        return []







def rerank_results_custom(llm, results: List[Dict], query: str) -> List[Dict]:
    """Custom reranking that preserves all results but reorders them."""
    try:
        from llama_index.core.schema import NodeWithScore, TextNode
        
        print(f"  Custom reranking {len(results)} results...")
        
        # For each result, get an LLM relevance score
        scored_results = []
        for i, result in enumerate(results):
            # Create a simple relevance prompt for each result
            relevance_prompt = f"""Query: {query}
            
Document: {result['content'][:500]}
            
Rate the relevance of this document to the query on a scale of 0-10, where 10 is highly relevant and 0 is not relevant. Respond with only a number."""
            
            try:
                # Get LLM score (this is a simplified approach)
                # In practice, you might want to batch these calls for efficiency
                response = llm.complete(relevance_prompt)
                score_text = response.text.strip()
                
                # Extract numeric score
                import re
                score_match = re.search(r'(\d+(?:\.\d+)?)', score_text)
                llm_score = float(score_match.group(1)) if score_match else result['similarity_score'] * 10
                
            except Exception as e:
                print(f"    Warning: Failed to get LLM score for result {i}, using similarity score")
                llm_score = result['similarity_score'] * 10
            
            result_copy = result.copy()
            result_copy['llm_score'] = llm_score
            scored_results.append(result_copy)
            
            if (i + 1) % 5 == 0:
                print(f"    Scored {i + 1}/{len(results)} results...")
        
        # Sort by LLM score (highest first)
        reranked_results = sorted(scored_results, key=lambda x: x['llm_score'], reverse=True)
        
        print(f"  Custom reranking completed: {len(reranked_results)} results")
        return reranked_results
        
    except Exception as e:
        print(f"ERROR: Failed to custom rerank results - {e}")
        return results  # Return original results as fallback

def rerank_results(reranker, results: List[Dict], query: str) -> List[Dict]:
    """Rerank search results using LLMRerank."""
    try:
        from llama_index.core.schema import NodeWithScore, TextNode
        
        # Convert results to NodeWithScore objects
        nodes_with_scores = []
        for result in results:
            text_node = TextNode(
                text=result['content'],
                metadata=result['metadata'],
                id_=result['id']
            )
            node_with_score = NodeWithScore(node=text_node, score=result['similarity_score'])
            nodes_with_scores.append(node_with_score)
        
        print(f"  Converting {len(nodes_with_scores)} nodes for reranking...")
        
        # Rerank using LLMRerank
        reranked_nodes = reranker.postprocess_nodes(nodes_with_scores, query_str=query)
        print(f"  LLMRerank returned {len(reranked_nodes)} nodes")
        
        # Convert back to our format
        reranked_results = []
        for i, node_with_score in enumerate(reranked_nodes):
            node = node_with_score.node
            original_result = next((r for r in results if r['id'] == node.id_), {})
            
            reranked_results.append({
                'id': node.id_,
                'chunk_index': original_result.get('chunk_index', i),
                'content': node.text,
                'content_contextualized': original_result.get('content_contextualized', ''),
                'source_file': original_result.get('source_file', 'Unknown'),
                'source_path': original_result.get('source_path', ''),
                'similarity_score': original_result.get('similarity_score', 0.0),
                'rerank_score': node_with_score.score if node_with_score.score is not None else 0.0,
                'metadata': node.metadata or {}
            })
        
        return reranked_results
        
    except Exception as e:
        print(f"ERROR: Failed to rerank results - {e}")
        return results  # Return all original results as fallback

def save_results_to_file(query: str, original_results: List[Dict], reranked_results: List[Dict]) -> str:
    """Save search results to a text file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"search_results_{timestamp}.txt"
    filepath = Path(filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write header
            f.write("SEMANTIC SEARCH RESULTS WITH LLM RERANKING\n")
            f.write("=" * 60 + "\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Query: {query}\n")
            f.write("=" * 60 + "\n\n")
            
            # Write position mapping
            f.write("POSITION MAPPING\n")
            f.write("=" * 30 + "\n")
            f.write("Original - Reranked\n")
            f.write("-" * 18 + "\n")
            
            position_changes = []
            for new_pos, reranked_result in enumerate(reranked_results):
                original_pos = None
                for orig_pos, orig_result in enumerate(original_results):
                    if orig_result['id'] == reranked_result['id']:
                        original_pos = orig_pos
                        position_changes.append(f"{orig_pos}→{new_pos}")
                        break
                
                if original_pos is not None:
                    f.write(f"{new_pos:<8} - {original_pos}\n")
                else:
                    f.write(f"{new_pos:<8} - ?\n")
            
            f.write("=" * 30 + "\n\n")
            
            # Write reranked results with scores
            f.write("🎯 ALL RERANKED RESULTS WITH LLM SCORES:\n")
            for i, result in enumerate(reranked_results):
                llm_score = result.get('llm_score', 0.0)
                sim_score = result['similarity_score'] * 100
                f.write(f"  [{i+1:2d}] LLM: {llm_score:.1f}/10 | Sim: {sim_score:.1f}% | {result['source_file'][:30]}\n")
            
            f.write("\n")
            
            # Write summary
            f.write("📊 FULL RESULTS SUMMARY:\n")
            f.write(f"Original results: {len(original_results)}\n")
            f.write(f"Reranked results: {len(reranked_results)}\n")
            f.write(f"Original best match: {original_results[0]['similarity_score']*100:.1f}% similarity\n")
            f.write(f"Reranked results: All {len(reranked_results)} results reordered by LLM scoring\n\n")
            
            # Write position changes
            f.write("🔄 ALL POSITION CHANGES (Original → Reranked):\n")
            if len(position_changes) <= 10:
                f.write(" ".join(f"{change:>6}" for change in position_changes) + "\n")
            else:
                for i in range(0, len(position_changes), 10):
                    chunk = position_changes[i:i+10]
                    f.write(" ".join(f"{change:>6}" for change in chunk) + "\n")
            
            f.write("\n")
            
            # Write detailed results
            f.write("DETAILED SEARCH RESULTS\n")
            f.write("=" * 100 + "\n")
            
            for i, result in enumerate(reranked_results, 1):
                llm_score = result.get('llm_score', 0.0)
                similarity_percent = result['similarity_score'] * 100
                
                f.write(f"[{i:2d}] LLM: {llm_score:.1f}/10 | Similarity: {similarity_percent:.1f}% | Source: {result['source_file']}\n")
                f.write(f"     Chunk #{result['chunk_index']} (ID: {result['id']})\n")
                f.write(f"     Source Path: {result.get('source_path', 'N/A')}\n")
                
                # Show full context if available
                if result.get('content_contextualized'):
                    f.write(f"\n     FULL CONTEXT:\n")
                    f.write(f"     {result['content_contextualized']}\n")
                else:
                    f.write(f"     Context: No Context Available\n")
                
                # Show full content
                f.write(f"\n     FULL CONTENT:\n")
                content_lines = result['content'].split('\n')
                for line in content_lines:
                    f.write(f"     {line}\n")
                
                f.write("\n" + "-" * 100 + "\n\n")
        
        return str(filepath.absolute())
        
    except Exception as e:
        print(f"ERROR: Failed to save results to file - {e}")
        return None

def print_comparison_table(original_results: List[Dict], reranked_results: List[Dict], query: str):
    """Print a simple position mapping table."""
    print("\n" + "=" * 30)
    print("POSITION MAPPING")
    print("=" * 30)
    print("Original - Reranked")
    print("-" * 18)
    
    # Create mapping of reranked results to their original positions
    for new_pos, reranked_result in enumerate(reranked_results):
        # Find this result's original position
        original_pos = None
        for orig_pos, orig_result in enumerate(original_results):
            if orig_result['id'] == reranked_result['id']:
                original_pos = orig_pos
                break
        
        if original_pos is not None:
            print(f"{new_pos:<8} - {original_pos}")
        else:
            print(f"{new_pos:<8} - ?")
    
    print("=" * 30)

def print_search_results(results: List[Dict], query: str):
    """Print search results in a readable format."""
    print("\n" + "=" * 80)
    print(f"SEARCH RESULTS FOR: '{query}'")
    print("=" * 80)
    
    if not results:
        print("No results found.")
        return
    
    print(f"Found {len(results)} results:")
    print()
    
    for i, result in enumerate(results, 1):
        similarity_percent = result['similarity_score'] * 100
        
        print(f"[{i:2d}] Similarity: {similarity_percent:.1f}% | Source: {result['source_file']}")
        print(f"     Chunk #{result['chunk_index']} (ID: {result['id']})")
        
        # Show context if available
        if result.get('content_contextualized'):
            print(f"     Context: {result['content_contextualized'][:100]}{'...' if len(result['content_contextualized']) > 100 else ''}")
        
        # Show content preview
        content_preview = result['content'][:200].replace('\n', ' ').strip()
        print(f"     Content: {content_preview}{'...' if len(result['content']) > 200 else ''}")
        print()




if __name__ == "__main__":
    main()