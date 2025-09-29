"""
Simple query script for testing vector search.
"""

from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex
from common import get_vector_store

questions = [
    "Priority for Vacant Positions"
]

def main():
    print("🔍 Simple Query Test")
    print("=" * 40)
    
    # --- Step 1: Get vector store ---
    try:
        vector_store = get_vector_store()
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
    
    # --- Step 4: Create query engine ---
    try:
        query_engine = index.as_query_engine(llm=llm)
        print("✅ Created query engine")
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
            # response = query_engine.query(question)
            # print(f"Answer: {response}")
            # Show source information if available
            # if hasattr(response, 'source_nodes') and response.source_nodes:
            #     print(f"\nSources ({len(response.source_nodes)} documents):")
            #     for j, node in enumerate(response.source_nodes[:2], 1):  # Show top 2 sources
            #         filename = node.metadata.get('filename', 'Unknown')
            #         print(f"  {j}. {filename}")

            # Run as Retriever with metadata filter
            print("Running as Retriever with HR Bylaws filter...")
            from llama_index.core.vector_stores import MetadataFilters, MetadataFilter, FilterOperator
            
            # Create metadata filter for HR Bylaws file
            metadata_filters = MetadataFilters(
                filters=[
                    MetadataFilter(
                        key="filename",
                        value="HR Bylaws_2f9c1749.md",
                        operator=FilterOperator.EQ
                    )
                ]
            )
            
            retriever = index.as_retriever(
                similarity_top_k=10,
                filters=metadata_filters
            ) 
            response = retriever.retrieve(question)
            
            # Clear and write to output.txt
            with open("output.txt", "w") as f:
                f.write(f"Question: {question}\n")
                f.write(f"Filter: filename = 'HR Bylaws_2f9c1749.md'\n")
                f.write("=" * 50 + "\n\n")
                
                if response:
                    f.write(f"Found {len(response)} relevant chunks (HR Bylaws only):\n\n")
                    for j, node in enumerate(response, 1):
                        filename = node.metadata.get('filename', 'Unknown')
                        f.write(f"Chunk {j} (from {filename}):\n")
                        f.write("-" * 30 + "\n")
                        f.write(f"{node.text}\n\n")
                        f.write(f"Score: {node.score}\n\n")
                else:
                    f.write("No relevant chunks found in HR Bylaws document.\n")
            
            print(f"Results written to output.txt")
            
        
        except Exception as e:
            print(f"❌ Query failed: {e}")
    
    print("\n" + "=" * 40)
    print("Query test completed!")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())