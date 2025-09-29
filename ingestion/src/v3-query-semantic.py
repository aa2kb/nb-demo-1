"""
Simple query script for testing vector search.
"""

from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.vector_stores import MetadataFilters, MetadataFilter, FilterOperator
from base.common import get_vector_store_v2

questions = [
    # "Transition from Full Time to Part Time or Vice Versa"
    # "Appointment of Graduate Trainees"
    "Priority for Vacant Positions"
]

def main():
    print("🔍 Simple Query Test")
    print("=" * 40)
    
    # --- Step 1: Get vector store ---
    try:
        vector_store = get_vector_store_v2()
        print("✅ Connected to vector store")
    except Exception as e:
        print(f"❌ Failed to connect to vector store: {e}")
        return 1
    
    # --- Step 2: Setup embedding model and index ---
    try:
        embed_model = OllamaEmbedding(model_name="bge-m3:latest")
        index = VectorStoreIndex.from_vector_store(vector_store, embed_model=embed_model)
        print("✅ Created index with BGE-M3 embeddings")
    except Exception as e:
        print(f"❌ Failed to create index: {e}")
        return 1
    
    # --- Step 3: Setup LLM for answering ---
    try:
        llm = Ollama(model="mistral:7b")
        print("✅ Initialized mistral:7b")
    except Exception as e:
        print(f"❌ Failed to initialize LLM: {e}")
        return 1
    
    # --- Step 4: Create query engine with retriever and response synthesizer ---
    try:
        # Configure retriever with metadata filters
        metadata_filters = MetadataFilters(
            filters=[
                MetadataFilter(
                    key="filename",
                    value="HR Bylaws_2f9c1749.md",
                    operator=FilterOperator.EQ
                )
            ]
        )
        
        retriever = VectorIndexRetriever(
            index=index,
            similarity_top_k=10,
            filters=metadata_filters
        )
        
        # Configure response synthesizer
        response_synthesizer = get_response_synthesizer(
            response_mode="tree_summarize",
            llm=llm
        )
        
        # Assemble query engine
        query_engine = RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
        )
        
        print("✅ Created query engine with retriever and response synthesizer")
    except Exception as e:
        print(f"❌ Failed to create query engine: {e}")
        return 1
    
    # --- Step 5: Ask questions ---

    
    print("\n" + "=" * 40)
    print("Running Queries:")
    
    for i, question in enumerate(questions, 1):
        print(f"\n🔍 Question {i}: {question}")
        print("-" * 50)
        
        try:
            # Run as Query Engine with retriever and response synthesizer
            print("Running query engine with tree_summarize...")
            response = query_engine.query(question)
            
            # Clear and write to output.txt
            with open("output.txt", "w") as f:
                f.write(f"Question: {question}\n")
                f.write(f"Filter: filename = 'HR Bylaws_2f9c1749.md'\n")
                f.write(f"Response Mode: tree_summarize\n")
                f.write("=" * 50 + "\n\n")
                
                # Write the synthesized response
                f.write(f"Answer:\n{response}\n\n")
                
                # Write source information if available
                if hasattr(response, 'source_nodes') and response.source_nodes:
                    f.write(f"Sources ({len(response.source_nodes)} chunks used):\n\n")
                    for j, node in enumerate(response.source_nodes, 1):
                        filename = node.metadata.get('filename', 'Unknown')
                        f.write(f"Source {j} (from {filename}):\n")
                        f.write("-" * 30 + "\n")
                        f.write(f"{node.text[:200]}...\n\n")  # First 200 chars
                        f.write(f"Score: {node.score}\n\n")
                else:
                    f.write("No source nodes available.\n")
            
            print(f"Results written to output.txt")
            print(f"Answer preview: {str(response)[:100]}...")
            
        except Exception as e:
            print(f"❌ Query failed: {e}")
    
    print("\n" + "=" * 40)
    print("Query test completed!")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())