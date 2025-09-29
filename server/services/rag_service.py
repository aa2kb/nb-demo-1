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
from typing import Type, ClassVar, List
from pydantic import BaseModel, Field

class GovernmentQueryInput(BaseModel):
    """Input schema for government document search tool."""
    question: str = Field(..., description="Question about government policies, procedures, HR, procurement, or security regulations")


class GovernmentDocumentTool(BaseTool):
    name: str = "government_document_search"
    description: str = """Search Abu Dhabi government documents including HR bylaws, procurement standards, information security policies, and related regulations to get complete answers.
    This tool provides comprehensive information from multiple government documentation sources.
    Use this tool ONCE per question - it returns complete, detailed answers with proper citations.
    Do not call this tool multiple times for the same question.
    The tool intelligently selects and searches relevant documents including:
    - HR bylaws, employment regulations, and human resources policies
    - Abu Dhabi procurement standards and guidelines
    - Procurement manuals and business processes
    - Information security policies and data protection guidelines
    Responses include citations showing which documents provided the information."""
    args_schema: Type[BaseModel] = GovernmentQueryInput
    
    # Simple cache to prevent redundant calls
    _cache: dict = {}
    
    # === RAG CONFIGURATION CONTROLS ===
    # Document detection settings
    available_documents: ClassVar[List[str]] = [
        "Abu Dhabi Procurement Standards_0ef9c4a0.md",
        "HR Bylaws_2f9c1749.md", 
        "Inforamation Security_8ac2fee2.md",
        "Procurement Manual (Ariba Aligned)_f679b7db.md",
        "Procurement Manual (Business Process)_66d86f21.md"
    ]
    
    # Retrieval settings
    retriever_top_k: ClassVar[int] = 10          # Number of documents to retrieve initially per document
    
    # Reranking settings  
    use_reranking: ClassVar[bool] = True          # Enable/disable reranking step (using Gemini Flash)
    reranking_top_n: ClassVar[int] = 3            # Number of documents after reranking per document

    # Generation settings
    max_context_chunks: ClassVar[int] = 3         # Maximum chunks to use for response generation per document
    
    def _run(self, question: str) -> str:
        """Main RAG pipeline execution with multi-document processing."""
        try:
            print(f"\n🔍 Government Document Query: {question}")
            print("=" * 50)
            
            # Step 0: Setup components
            print("🔧 Setting up RAG components...")
            vector_store, embed_model, index, primary_llm, secondary_llm = self.setup_components()
            print("✅ Components setup completed")
            
            # Step 1: Detect relevant documents
            print("🎯 Detecting relevant documents for query...")
            relevant_documents = self.detect_relevant_documents(question, primary_llm)
            print(f"📋 Selected documents: {relevant_documents}")
            
            if not relevant_documents:
                return "No relevant documents found for your query. Please try rephrasing your question."
            
            # Step 2: Process each document in parallel (simulated)
            print("🔄 Processing documents in parallel...")
            document_responses = []
            
            for doc_filename in relevant_documents:
                print(f"\n� Processing: {doc_filename}")
                doc_response = self.process_single_document(
                    index, question, doc_filename, primary_llm, secondary_llm
                )
                if doc_response:
                    document_responses.append({
                        "document": doc_filename,
                        "response": doc_response
                    })
            
            if not document_responses:
                return "No relevant information found in the selected documents."
            
            # Step 3: Combine responses with citations
            print("� Combining responses and adding citations...")
            final_response = self.combine_responses_with_citations(
                question, document_responses, primary_llm
            )
            
            print(f"✅ Generated final response with citations")
            return final_response
            
        except TimeoutError as e:
            print(f"⏰ Timeout error details: {str(e)}")
            return "The government document search took too long to complete. Please try a simpler question or try again later."
        except ConnectionError as e:
            print(f"🔌 Connection error details: {str(e)}")
            return "Unable to connect to the government database or AI services. Please check system connectivity."
        except Exception as e:
            error_type = type(e).__name__
            error_msg = str(e)
            print(f"❌ Detailed error - Type: {error_type}, Message: {error_msg}")
            
            if "timed out" in error_msg.lower() or "timeout" in error_msg.lower():
                return "The government document search timed out. The question might be too complex or the system is busy. Please try again with a simpler question."
            elif "connection" in error_msg.lower():
                return "Connection issue with government database or AI services. Please try again later."
            elif "not found" in error_msg.lower() or error_type == "NotFound":
                return f"Government document search encountered a lookup issue: {error_msg}. This might be due to missing documents or configuration. Please check if government documents are properly loaded."
            else:
                return f"Government document search encountered an issue: {error_type}: {error_msg}. Please rephrase your question and try again."

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
    
    def detect_relevant_documents(self, question: str, llm) -> list:
        """Step 1: Detect which documents are relevant for the user query."""
        document_descriptions = {
            "Abu Dhabi Procurement Standards_0ef9c4a0.md": "Abu Dhabi procurement standards, guidelines, and regulations",
            "HR Bylaws_2f9c1749.md": "Human resources bylaws, employment regulations, and HR policies", 
            "Inforamation Security_8ac2fee2.md": "Information security policies, data protection, and cybersecurity guidelines",
            "Procurement Manual (Ariba Aligned)_f679b7db.md": "Ariba-aligned procurement processes and manual",
            "Procurement Manual (Business Process)_66d86f21.md": "Business process procurement manual and procedures"
        }
        
        documents_list = "\n".join([
            f"- {filename}: {description}" 
            for filename, description in document_descriptions.items()
        ])
        
        prompt = f"""Given the following user question and available documents, determine which documents are most relevant to answer the question.

User Question: {question}

Available Documents:
{documents_list}

Instructions:
1. Analyze the question to understand what type of information is needed
2. Select 1-3 most relevant documents that could contain the answer
3. Return ONLY a Python list of document filenames (exact names as shown above)
4. If unsure, include documents that might be related

Example responses:
["HR Bylaws_2f9c1749.md"]
["Abu Dhabi Procurement Standards_0ef9c4a0.md", "Procurement Manual (Business Process)_66d86f21.md"]

Your response (only the list):"""

        try:
            print("🤖 Analyzing question to detect relevant documents...")
            response = llm.complete(prompt)
            response_text = str(response).strip()
            
            # Parse the response to extract document list
            import ast
            try:
                # Try to parse as Python list
                relevant_docs = ast.literal_eval(response_text)
                if isinstance(relevant_docs, list):
                    # Validate that all documents exist in our available documents
                    valid_docs = [doc for doc in relevant_docs if doc in self.available_documents]
                    print(f"✅ Detected {len(valid_docs)} relevant documents: {valid_docs}")
                    return valid_docs
            except:
                # Fallback: extract document names from response
                relevant_docs = []
                for doc in self.available_documents:
                    if doc in response_text:
                        relevant_docs.append(doc)
                
                if relevant_docs:
                    print(f"✅ Detected {len(relevant_docs)} relevant documents (fallback): {relevant_docs}")
                    return relevant_docs
            
            # Default fallback: use HR Bylaws for HR-related questions
            if any(keyword in question.lower() for keyword in ['hr', 'human', 'employee', 'work', 'job', 'staff']):
                return ["HR Bylaws_2f9c1749.md"]
            elif any(keyword in question.lower() for keyword in ['procurement', 'purchase', 'buy', 'vendor', 'supplier']):
                return ["Abu Dhabi Procurement Standards_0ef9c4a0.md", "Procurement Manual (Business Process)_66d86f21.md"]
            elif any(keyword in question.lower() for keyword in ['security', 'data', 'information', 'cyber']):
                return ["Inforamation Security_8ac2fee2.md"]
            else:
                # Default to HR if unclear
                return ["HR Bylaws_2f9c1749.md"]
                
        except Exception as e:
            print(f"⚠️ Document detection failed: {str(e)}, using default HR document")
            return ["HR Bylaws_2f9c1749.md"]
    
    def process_single_document(self, index, question: str, doc_filename: str, primary_llm, secondary_llm) -> str:
        """Process a single document through the RAG pipeline."""
        try:
            # Step 1: Retrieve from specific document
            retrieved_nodes, query_bundle = self.retrieve_documents_from_file(
                index, question, doc_filename, self.retriever_top_k
            )
            
            if not retrieved_nodes:
                print(f"⚠️ No relevant content found in {doc_filename}")
                return None
            
            # Step 2: Rerank if enabled
            if self.use_reranking:
                final_nodes = self.rerank_documents(retrieved_nodes, query_bundle, primary_llm, self.reranking_top_n)
            else:
                final_nodes = retrieved_nodes[:self.reranking_top_n]
            
            # Step 3: Generate response
            response = self.generate_response_for_document(final_nodes, question, doc_filename, secondary_llm)
            
            return response
            
        except Exception as e:
            print(f"❌ Failed to process {doc_filename}: {str(e)}")
            return None
    
    def combine_responses_with_citations(self, question: str, document_responses: list, llm) -> str:
        """Step 3: Combine multiple document responses with proper citations."""
        if len(document_responses) == 1:
            # Single document response
            doc_info = document_responses[0]
            return f"{doc_info['response']}\n\n**Source:** {self.format_citation(doc_info['document'])}"
        
        # Multiple documents - combine intelligently
        responses_text = "\n\n".join([
            f"**From {self.format_citation(item['document'])}:**\n{item['response']}"
            for item in document_responses
        ])
        
        prompt = f"""You are tasked with combining multiple responses from different documents into a single, coherent answer.

Original Question: {question}

Multiple Document Responses:
{responses_text}

Instructions:
1. Create a comprehensive answer that combines information from all sources
2. Maintain accuracy - don't make up information not in the sources
3. When information conflicts, note the differences
4. Include proper citations for each piece of information
5. Structure the response clearly with markdown formatting
6. End with a "Sources" section listing all referenced documents

Provide a well-structured, comprehensive response with proper citations:"""

        try:
            print("🔗 Combining responses from multiple documents...")
            combined_response = llm.complete(prompt)
            return str(combined_response).strip()
        except Exception as e:
            print(f"⚠️ Failed to combine responses: {str(e)}, using simple concatenation")
            # Fallback: simple combination
            combined = f"Based on multiple documents:\n\n{responses_text}"
            sources = "\n".join([f"- {self.format_citation(item['document'])}" for item in document_responses])
            return f"{combined}\n\n**Sources:**\n{sources}"
    
    def format_citation(self, filename: str) -> str:
        """Format document filename into readable citation."""
        # Remove file extension and hash
        base_name = filename.replace('.md', '').split('_')[0]
        if base_name.endswith(')'):
            # Handle cases like "Procurement Manual (Business Process)"
            return base_name
        return base_name.replace('_', ' ').title()
    
    def retrieve_documents_from_file(self, index, question: str, filename: str, top_k: int):
        """Retrieve documents from a specific file."""
        try:
            metadata_filters = MetadataFilters(
                filters=[
                    MetadataFilter(
                        key="filename",
                        value=filename,
                        operator=FilterOperator.EQ
                    )
                ]
            )
            
            print(f"🔍 Searching in: {filename}")
            
            retriever = VectorIndexRetriever(
                index=index,
                similarity_top_k=top_k,
                filters=metadata_filters
            )
            
            query_bundle = QueryBundle(question)
            retrieved_nodes = retriever.retrieve(query_bundle)
            
            print(f"📄 Retrieved {len(retrieved_nodes)} chunks from {filename}")
            return retrieved_nodes, query_bundle
            
        except Exception as e:
            print(f"❌ Retrieval failed for {filename}: {str(e)}")
            return [], None
    
    def generate_response_for_document(self, nodes, question: str, doc_filename: str, llm) -> str:
        """Generate response for a specific document."""
        if not nodes:
            return None
        
        chunks_to_use = min(len(nodes), self.max_context_chunks)
        
        context_parts = []
        for i, node in enumerate(nodes[:chunks_to_use], 1):
            context_parts.append(f"Context {i}:\n{node.text}")
        
        context = "\n\n".join(context_parts)
        doc_name = self.format_citation(doc_filename)
        
        prompt = f"""Based on the following context from {doc_name}, answer the question clearly and accurately.

Context from {doc_name}:
{context}

Question: {question}

Answer: Provide a clear, direct answer based only on the information in the context. If the context doesn't contain enough information to answer the question, say so. Focus on information specific to this document."""
        
        try:
            response = llm.complete(prompt)
            return str(response).strip()
        except Exception as e:
            print(f"⚠️ Response generation failed for {doc_filename}: {str(e)}")
            return None
    
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
government_document_tool = GovernmentDocumentTool()
