import os
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.postprocessor import LLMRerank
from llama_index.core.schema import QueryBundle
from llama_index.core.vector_stores import MetadataFilters, MetadataFilter, FilterOperator
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class HRQueryInput(BaseModel):
    """Input schema for HR RAG tool."""
    question: str = Field(..., description="HR-related question to search for")


class HRRAGTool(BaseTool):
    name: str = "hr_rag_search"
    description: str = """Use this tool to search HR bylaws, policies, and employment regulations. 
    This is your ONLY source for HR information - do not attempt to use web searches or other tools.
    The tool contains comprehensive HR documentation including employee policies, procedures, and bylaws.
    Always use this tool for any HR-related questions."""
    args_schema: Type[BaseModel] = HRQueryInput
    
    # === RAG CONFIGURATION CONTROLS ===
    # Retrieval settings
    retriever_top_k: int = 5          # Number of documents to retrieve initially
    
    # Reranking settings  
    use_reranking: bool = False         # Enable/disable reranking step
    reranking_top_n: int = 3          # Number of documents after reranking
    
    # Generation settings
    max_context_chunks: int = 3        # Maximum chunks to use for response generation
    
    def _run(self, question: str) -> str:
        """Main RAG pipeline execution."""
        try:
            print(f"\n🔍 HR RAG Query: {question}")
            print("=" * 50)
            
            # Setup components
            vector_store, embed_model, index, llm = self.setup_components()
            
            # Step 1: Retrieve
            retrieved_nodes, query_bundle = self.retrieve_documents(index, question, self.retriever_top_k)
            if not retrieved_nodes:
                return "No relevant HR documents found in the database."
            
            # Step 2: Rerank (optional)
            if self.use_reranking:
                final_nodes = self.rerank_documents(retrieved_nodes, query_bundle, llm, self.reranking_top_n)
            else:
                print("🔄 Skipping reranking (disabled)")
                final_nodes = retrieved_nodes[:self.reranking_top_n]  # Use top N without reranking
            
            # Step 3: Generate
            response = self.generate_response(final_nodes, question, llm)
            
            print(f"✅ Generated response: {response[:100]}...")
            return response
            
        except TimeoutError:
            return "The HR search took too long to complete. Please try a simpler question or try again later."
        except ConnectionError:
            return "Unable to connect to the HR database or AI services. Please check system connectivity."
        except Exception as e:
            error_type = type(e).__name__
            if "timed out" in str(e).lower() or "timeout" in str(e).lower():
                return "The HR search timed out. The question might be too complex or the system is busy. Please try again with a simpler question."
            elif "connection" in str(e).lower():
                return "Connection issue with HR database or AI services. Please try again later."
            else:
                return f"HR search encountered an issue: {error_type}. Please rephrase your question and try again."

    def get_vector_store(self):
        """Get PGVectorStore instance with configuration."""
        config = {
            'DB_HOST': os.getenv('DB_HOST', 'localhost'),
            'DB_PORT': int(os.getenv('DB_PORT', 5432)),
            'DB_USER': os.getenv('DB_USER', 'admin'),
            'DB_PASSWORD': os.getenv('DB_PASSWORD', 'admin'),
            'DB_NAME': os.getenv('DB_NAME', 'postgres'),
        }
        
        return PGVectorStore.from_params(
            database=config['DB_NAME'],
            host=config['DB_HOST'],
            password=config['DB_PASSWORD'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            table_name="vectors",
            embed_dim=1024,
            hybrid_search=True,
            text_search_config="english"
        )
    
    def setup_components(self):
        """Initialize RAG components."""
        # Get vector store
        vector_store = self.get_vector_store()
        
        # Setup embedding model
        embed_model = OllamaEmbedding(
            model_name="bge-m3:latest",
            base_url="http://localhost:11434"
        )
        
        # Create index
        index = VectorStoreIndex.from_vector_store(
            vector_store, 
            embed_model=embed_model
        )
        
        # Setup LLM for reranking and generation with timeout
        llm = Ollama(
            model="mistral:7b",
            base_url="http://localhost:11434",
            request_timeout=60.0  # 60 seconds timeout
        )
        
        return vector_store, embed_model, index, llm
    
    def retrieve_documents(self, index, question: str, top_k: int):
        """Step 1: Retrieve relevant documents from HR Bylaws."""
        # Create metadata filter for HR Bylaws
        metadata_filters = MetadataFilters(
            filters=[
                MetadataFilter(
                    key="filename",
                    value="HR Bylaws_2f9c1749.md",
                    operator=FilterOperator.EQ
                )
            ]
        )
        
        # Configure retriever
        retriever = VectorIndexRetriever(
            index=index,
            similarity_top_k=top_k,
            filters=metadata_filters
        )
        
        # Create query bundle and retrieve
        query_bundle = QueryBundle(question)
        retrieved_nodes = retriever.retrieve(query_bundle)
        
        print(f"📄 Retrieved {len(retrieved_nodes)} documents (top_k={top_k})")
        return retrieved_nodes, query_bundle
    
    def rerank_documents(self, retrieved_nodes, query_bundle, llm, top_n: int):
        """Step 2: Rerank documents using LLM."""
        print(f"� Reranking {len(retrieved_nodes)} documents to top {top_n} (this may take 30-60 seconds)...")
        
        if not retrieved_nodes:
            return []
        
        try:
            # Configure reranker
            reranker = LLMRerank(
                top_n=min(top_n, len(retrieved_nodes)),
                llm=llm
            )
            
            # Rerank documents
            reranked_nodes = reranker.postprocess_nodes(retrieved_nodes, query_bundle)
            
            # Print reranking order
            print("✅ Reranking completed:")
            for new_idx, node in enumerate(reranked_nodes):
                # Find original position
                for orig_idx, orig_node in enumerate(retrieved_nodes):
                    if orig_node.node_id == node.node_id:
                        print(f"   {orig_idx} -> {new_idx}")
                        break
            
            return reranked_nodes
            
        except Exception as e:
            print(f"⚠️ Reranking failed, using original order: {str(e)}")
            # Return top documents without reranking if reranking fails
            return retrieved_nodes[:top_n]
    
    def generate_response(self, nodes, question: str, llm):
        """Step 3: Generate natural language response from context."""
        if not nodes:
            return "No relevant information found in HR bylaws."
        
        # Use configurable number of chunks
        chunks_to_use = min(len(nodes), self.max_context_chunks)
        
        # Prepare context from top nodes
        context_parts = []
        for i, node in enumerate(nodes[:chunks_to_use], 1):
            context_parts.append(f"Context {i}:\n{node.text}")
        
        context = "\n\n".join(context_parts)
        
        # Create prompt for response generation
        prompt = f"""Based on the following HR bylaws context, answer the question clearly and accurately.

Context from HR Bylaws:
{context}

Question: {question}

Answer: Provide a clear, direct answer based only on the information in the context. If the context doesn't contain enough information to answer the question, say so."""
        
        print(f"💭 Generating response using {chunks_to_use} context chunks...")
        
        # Generate response
        response = llm.complete(prompt)
        
        return str(response).strip()
    

# Create singleton instance
hr_rag_tool = HRRAGTool()
