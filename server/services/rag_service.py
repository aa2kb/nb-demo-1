import os
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.postprocessor import LLMRerank
from llama_index.core.schema import QueryBundle
from llama_index.core.vector_stores import MetadataFilters, MetadataFilter, FilterOperator
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.llms.gemini import Gemini
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class HRQueryInput(BaseModel):
    """Input schema for HR RAG tool."""
    question: str = Field(..., description="HR-related question to search for")


class HRRAGTool(BaseTool):
    name: str = "hr_rag_search"
    description: str = """Search HR bylaws, policies, and employment regulations to get complete answers.
    This tool provides comprehensive information from HR documentation.
    Use this tool ONCE per question - it returns complete, detailed answers.
    Do not call this tool multiple times for the same question.
    The tool searches employee policies, procedures, bylaws, and HR regulations."""
    args_schema: Type[BaseModel] = HRQueryInput
    
    # Simple cache to prevent redundant calls
    _cache: dict = {}
    
    # === RAG CONFIGURATION CONTROLS ===
    # Retrieval settings
    retriever_top_k: int = 15          # Number of documents to retrieve initially
    
    # Reranking settings  
    use_reranking: bool = True          # Enable/disable reranking step (using Gemini Flash)
    reranking_top_n: int = 5            # Number of documents after reranking

    # Generation settings
    max_context_chunks: int = 5        # Maximum chunks to use for response generation
    
    def _run(self, question: str) -> str:
        """Main RAG pipeline execution."""
        try:
            print(f"\n🔍 HR RAG Query: {question}")
            print("=" * 50)
            
            # Step 0: Debug setup
            print("🔧 Setting up RAG components...")
            vector_store, embed_model, index, primary_llm, secondary_llm = self.setup_components()
            print("✅ Components setup completed")
            
            # Step 1: Retrieve
            print("📡 Starting document retrieval...")
            retrieved_nodes, query_bundle = self.retrieve_documents(index, question, self.retriever_top_k)
            if not retrieved_nodes:
                return "No relevant HR documents found in the database."
            
            # Step 2: Rerank (optional) - Use primary LLM for reranking
            if self.use_reranking:
                print("🔄 Starting document reranking...")
                final_nodes = self.rerank_documents(retrieved_nodes, query_bundle, primary_llm, self.reranking_top_n)
            else:
                print("🔄 Skipping reranking (disabled)")
                final_nodes = retrieved_nodes[:self.reranking_top_n]  # Use top N without reranking
            
            # Step 3: Generate - Use secondary LLM for generation
            print("💭 Starting response generation...")
            response = self.generate_response(final_nodes, question, primary_llm, secondary_llm)
            
            print(f"✅ Generated response: {response[:100]}...")
            return response
            
        except TimeoutError as e:
            print(f"⏰ Timeout error details: {str(e)}")
            return "The HR search took too long to complete. Please try a simpler question or try again later."
        except ConnectionError as e:
            print(f"🔌 Connection error details: {str(e)}")
            return "Unable to connect to the HR database or AI services. Please check system connectivity."
        except Exception as e:
            error_type = type(e).__name__
            error_msg = str(e)
            print(f"❌ Detailed error - Type: {error_type}, Message: {error_msg}")
            
            if "timed out" in error_msg.lower() or "timeout" in error_msg.lower():
                return "The HR search timed out. The question might be too complex or the system is busy. Please try again with a simpler question."
            elif "connection" in error_msg.lower():
                return "Connection issue with HR database or AI services. Please try again later."
            elif "not found" in error_msg.lower() or error_type == "NotFound":
                return f"HR search encountered a lookup issue: {error_msg}. This might be due to missing documents or configuration. Please check if HR documents are properly loaded."
            else:
                return f"HR search encountered an issue: {error_type}: {error_msg}. Please rephrase your question and try again."

    def get_vector_store(self):
        """Get PGVectorStore instance with configuration."""
        config = {
            'DB_HOST': os.getenv('DB_HOST', 'localhost'),
            'DB_PORT': int(os.getenv('DB_PORT', 5432)),
            'DB_USER': os.getenv('DB_USER', 'admin'),
            'DB_PASSWORD': os.getenv('DB_PASSWORD', 'admin'),
            'DB_NAME': os.getenv('DB_NAME', 'postgres'),
        }
        
        print(f"🗄️ Connecting to database: {config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}")
        
        try:
            vector_store = PGVectorStore.from_params(
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
            print("✅ Database connection successful")
            return vector_store
        except Exception as e:
            print(f"❌ Database connection failed: {type(e).__name__}: {str(e)}")
            raise
    
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
        
        # Get LLM configuration from environment
        llm_provider = os.getenv("DEFAULT_LLM_PROVIDER", "ollama").lower()
        llm_model = os.getenv("DEFAULT_LLM_MODEL", "mistral:7b")
        
        print(f"🤖 Using LLM Provider: {llm_provider}, Model: {llm_model}")
        
        # Setup LLMs based on provider
        if llm_provider == "gemini":
            gemini_api_key = os.getenv("GEMINI_API_KEY")
            if not gemini_api_key:
                print("❌ GEMINI_API_KEY not found but Gemini provider selected. Falling back to Ollama.")
                llm_provider = "ollama"
                llm_model = "mistral:7b"
            else:
                print("✅ Configuring Gemini Flash for both reranking and generation")
                try:
                    primary_llm = Gemini(
                        model=llm_model,
                        api_key=gemini_api_key,
                        temperature=0.1,
                        max_tokens=8192
                    )
                    secondary_llm = primary_llm  # Use same LLM for both operations
                    print("✅ Gemini LLMs initialized successfully")
                except Exception as e:
                    print(f"⚠️ Gemini initialization failed: {str(e)}")
                    print("🔄 Falling back to Ollama")
                    llm_provider = "ollama"
                    llm_model = "mistral:7b"
        
        # Fallback to Ollama or explicit Ollama configuration
        if llm_provider == "ollama":
            print("✅ Configuring Ollama for both reranking and generation")
            primary_llm = Ollama(
                model=llm_model,
                base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                request_timeout=60.0
            )
            secondary_llm = primary_llm  # Use same LLM for both operations
        
        return vector_store, embed_model, index, primary_llm, secondary_llm
    
    def retrieve_documents(self, index, question: str, top_k: int):
        """Step 1: Retrieve relevant documents from HR Bylaws."""
        try:
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
            
            print(f"🔍 Searching for documents with filename: HR Bylaws_2f9c1749.md")
            
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
            
            if len(retrieved_nodes) == 0:
                print("⚠️ No documents found - checking if any documents exist in the database...")
                # Try without filter to see if there are any documents at all
                no_filter_retriever = VectorIndexRetriever(
                    index=index,
                    similarity_top_k=top_k
                )
                all_docs = no_filter_retriever.retrieve(query_bundle)
                print(f"📊 Total documents in database (no filter): {len(all_docs)}")
                
                if len(all_docs) > 0:
                    print("📝 Available filenames in database:")
                    filenames = set()
                    for doc in all_docs[:5]:  # Show first 5
                        if hasattr(doc, 'metadata') and 'filename' in doc.metadata:
                            filenames.add(doc.metadata['filename'])
                    for filename in sorted(filenames):
                        print(f"   - {filename}")
            
            return retrieved_nodes, query_bundle
            
        except Exception as e:
            print(f"❌ Document retrieval failed: {type(e).__name__}: {str(e)}")
            raise
    
    def rerank_documents(self, retrieved_nodes, query_bundle, llm, top_n: int):
        """Step 2: Rerank documents using configured LLM."""
        llm_provider = os.getenv("DEFAULT_LLM_PROVIDER", "ollama").lower()
        llm_model = os.getenv("DEFAULT_LLM_MODEL", "mistral:7b")
        print(f"📄 Reranking {len(retrieved_nodes)} documents to top {top_n} using {llm_provider} ({llm_model})...")
        
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
    
    def generate_response(self, nodes, question: str, primary_llm, secondary_llm):
        """Step 3: Generate natural language response from context using configured LLM."""
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
        
        # Use secondary LLM for generation (could be same as primary)
        llm_provider = os.getenv("DEFAULT_LLM_PROVIDER", "ollama").lower()
        llm_model = os.getenv("DEFAULT_LLM_MODEL", "mistral:7b")
        
        try:
            print(f"💭 Generating response using {llm_provider} ({llm_model}) with {chunks_to_use} context chunks...")
            response = secondary_llm.complete(prompt)
            print(f"✅ Response generated successfully with {llm_provider}")
            return str(response).strip()
        except Exception as e:
            print(f"⚠️ Generation failed with {llm_provider}: {str(e)}")
            # If we're using Gemini and it fails, try Ollama as fallback
            if llm_provider == "gemini":
                print("🔄 Falling back to Ollama for generation")
                try:
                    fallback_llm = Ollama(
                        model="mistral:7b",
                        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                        request_timeout=60.0
                    )
                    response = fallback_llm.complete(prompt)
                    print("✅ Response generated successfully with Ollama (fallback)")
                    return str(response).strip()
                except Exception as fallback_e:
                    print(f"❌ Fallback also failed: {str(fallback_e)}")
                    return "Failed to generate response due to LLM issues. Please try again later."
            else:
                return "Failed to generate response due to LLM issues. Please try again later."
    

# Create singleton instance
hr_rag_tool = HRRAGTool()
