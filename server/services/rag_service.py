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
    name: str = "HR RAG Search"
    description: str = "Search HR bylaws and policies to answer HR-related questions using retrieval, reranking, and generation"
    args_schema: Type[BaseModel] = HRQueryInput
    
    def _run(self, question: str) -> str:
        """Main RAG pipeline execution."""
        try:
            print(f"\n🔍 HR RAG Query: {question}")
            print("=" * 50)
            
            # Setup components
            vector_store, embed_model, index, llm = self.setup_components()
            
            # Step 1: Retrieve
            retrieved_nodes, query_bundle = self.retrieve_documents(index, question)
            if not retrieved_nodes:
                return "No relevant HR documents found."
            
            # Step 2: Rerank
            reranked_nodes = self.rerank_documents(retrieved_nodes, query_bundle, llm)
            
            # Step 3: Generate
            response = self.generate_response(reranked_nodes, question, llm)
            
            print(f"✅ Generated response: {response[:100]}...")
            return response
            
        except Exception as e:
            error_msg = f"HR RAG pipeline failed: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg

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
        
        # Setup LLM for reranking and generation
        llm = Ollama(
            model="mistral:7b",
            base_url="http://localhost:11434"
        )
        
        return vector_store, embed_model, index, llm
    
    def retrieve_documents(self, index, question: str, top_k: int = 10):
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
        
        print(f"📄 Retrieved {len(retrieved_nodes)} documents")
        return retrieved_nodes, query_bundle
    
    def rerank_documents(self, retrieved_nodes, query_bundle, llm, top_n: int = 5):
        """Step 2: Rerank documents using LLM."""
        print(f"📄 Reranking {len(retrieved_nodes)} documents (This takes some time)")
        
        if not retrieved_nodes:
            return []
        
        # Configure reranker
        reranker = LLMRerank(
            top_n=min(top_n, len(retrieved_nodes)),
            llm=llm
        )
        
        # Rerank documents
        reranked_nodes = reranker.postprocess_nodes(retrieved_nodes, query_bundle)
        
        # Print reranking order
        print("🔄 Reranking results:")
        for new_idx, node in enumerate(reranked_nodes):
            # Find original position
            for orig_idx, orig_node in enumerate(retrieved_nodes):
                if orig_node.node_id == node.node_id:
                    print(f"   {orig_idx} -> {new_idx}")
                    break
        
        return reranked_nodes
    
    def generate_response(self, reranked_nodes, question: str, llm):
        """Step 3: Generate natural language response from context."""
        if not reranked_nodes:
            return "No relevant information found in HR bylaws."
        
        # Prepare context from top reranked nodes
        context_parts = []
        for i, node in enumerate(reranked_nodes[:3], 1):  # Use top 3
            context_parts.append(f"Context {i}:\n{node.text}")
        
        context = "\n\n".join(context_parts)
        
        # Create prompt for response generation
        prompt = f"""Based on the following HR bylaws context, answer the question clearly and accurately.

Context from HR Bylaws:
{context}

Question: {question}

Answer: Provide a clear, direct answer based only on the information in the context. If the context doesn't contain enough information to answer the question, say so."""
        
        # Generate response
        response = llm.complete(prompt)
        
        return str(response).strip()
    

# Create singleton instance
hr_rag_tool = HRRAGTool()
