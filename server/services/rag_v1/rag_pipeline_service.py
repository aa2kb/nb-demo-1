import os
from typing import List, Optional, Tuple
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.schema import QueryBundle, NodeWithScore
from llama_index.core.vector_stores import MetadataFilters, MetadataFilter, FilterOperator
from phoenix.client import Client


class RAGPipelineService:
    """Service for RAG pipeline operations including retrieval, reranking, and generation."""
    
    def __init__(self, retriever_top_k: int = 10, max_context_chunks: int = 3):
        """
        Initialize RAG pipeline service.
        
        Args:
            retriever_top_k: Number of documents to retrieve initially per document
            max_context_chunks: Maximum chunks to use for response generation per document
        """
        self.retriever_top_k = retriever_top_k
        self.max_context_chunks = max_context_chunks
        
        # Phoenix configuration for response generation
        self.document_processing_prompt_id = os.getenv("DOCUMENT_PROCESSING_PROMPT_ID", "document_processing")
        self.document_answer_prompt_id = os.getenv("DOCUMENT_ANSWER_PROMPT_ID", "document_answer")
        
        # Always initialize Phoenix client
        try:
            self.phoenix_client = Client()
            print("✅ Phoenix client initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize Phoenix client: {str(e)}")
            raise Exception(f"Phoenix client initialization failed: {str(e)}")
    
    def process_single_document(self, index: VectorStoreIndex, question: str, 
                              doc_filename: str, primary_llm, secondary_llm) -> Optional[str]:
        """Process a single document through the RAG pipeline."""
        try:
            # Step 1: Retrieve from specific document
            retrieved_nodes, query_bundle = self.retrieve_documents_from_file(
                index, question, doc_filename, self.retriever_top_k
            )
            
            if not retrieved_nodes:
                print(f"⚠️ No relevant content found in {doc_filename}")
                return None
            
            # Step 2: Sort by similarity score (highest first)
            final_nodes = self.rank_by_similarity(retrieved_nodes)
            
            # Step 3: Generate response
            response = self.generate_response_for_document(final_nodes, question, doc_filename, secondary_llm)
            
            return response
            
        except Exception as e:
            print(f"❌ Failed to process {doc_filename}: {str(e)}")
            return None
    
    def retrieve_documents_from_file(self, index: VectorStoreIndex, question: str, 
                                   filename: str, top_k: int) -> Tuple[List[NodeWithScore], Optional[QueryBundle]]:
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
            print(f"📊 Using top_k: {top_k}")
            
            # Ensure top_k is definitely an integer
            top_k_int = int(top_k)
            
            retriever = VectorIndexRetriever(
                index=index,
                similarity_top_k=top_k_int,  # Force integer type
                filters=metadata_filters
            )
            
            query_bundle = QueryBundle(question)
            retrieved_nodes = retriever.retrieve(query_bundle)
            
            print(f"📄 Retrieved {len(retrieved_nodes)} chunks from {filename}")
            return retrieved_nodes, query_bundle
            
        except Exception as e:
            print(f"❌ Retrieval failed for {filename}: {str(e)}")
            print(f"🔍 Error details: {type(e).__name__}")
            return [], None
    
    def rank_by_similarity(self, retrieved_nodes: List[NodeWithScore]) -> List[NodeWithScore]:
        """Rank documents by similarity score (highest first)."""
        if not retrieved_nodes:
            return []
        
        print(f"📄 Ranking {len(retrieved_nodes)} documents by similarity score...")
        
        # Sort by similarity score in descending order (highest similarity first)
        ranked_nodes = sorted(retrieved_nodes, key=lambda node: node.score if node.score is not None else 0.0, reverse=True)
        
        # Print ranking results
        print("✅ Similarity-based ranking completed:")
        for idx, node in enumerate(ranked_nodes[:20]):  # Show top 20
            score = node.score if node.score is not None else 0.0
            print(f"   Rank {idx + 1}: Score {score:.4f}")
        
        return ranked_nodes
    
    def generate_response_for_document(self, nodes: List[NodeWithScore], question: str, 
                                     doc_filename: str, llm=None) -> Optional[str]:
        """Generate response for a specific document using Phoenix-managed prompts."""
        if not nodes:
            return None
        
        chunks_to_use = min(len(nodes), self.max_context_chunks)
        
        context_parts = []
        for i, node in enumerate(nodes[:chunks_to_use], 1):
            context_parts.append(f"Context {i}:\n{node.text}")
        
        context = "\n\n".join(context_parts)
        doc_name = self._format_citation(doc_filename)
        print(f"📝 Generating response using chunks from {doc_filename}...")
        return self._generate_with_phoenix(context, question, doc_name, doc_filename, llm)
    
    def _generate_with_phoenix(self, context: str, question: str, doc_name: str, doc_filename: str, llm) -> Optional[str]:
        """Generate response using Phoenix-managed prompts."""
        try:
            # Get the prompt from Phoenix
            prompt = self.phoenix_client.prompts.get(prompt_identifier=self.document_processing_prompt_id)
            
            # Format the prompt template with variables
            formatted_result = prompt.format(variables={
                "context": context,
                "question": question,
                "doc_name": doc_name
            })
            
            # Extract the actual prompt text from Phoenix format
            if isinstance(formatted_result, dict) and 'messages' in formatted_result:
                # Phoenix returns OpenAI format, extract the user message content
                prompt_text = formatted_result['messages'][-1]['content']
            else:
                # Fallback if format is different
                prompt_text = str(formatted_result)
            
            # Use the existing LLM with the extracted prompt text
            response = llm.complete(prompt_text)
            return str(response).strip()
            
        except Exception as e:
            print(f"⚠️ Phoenix response generation failed for {doc_filename}: {str(e)}")
            return f"Unable to generate response for {doc_name} due to processing error."
    
    def combine_responses_with_citations(self, question: str, document_responses: List[dict], llm=None) -> str:
        """Combine multiple document responses with proper citations using Phoenix-managed prompts."""
        if len(document_responses) == 1:
            # Single document response
            doc_info = document_responses[0]
            return f"{doc_info['response']}\n\n**Source:** {self._format_citation(doc_info['document'])}"
        
        # Multiple documents - combine intelligently
        responses_text = "\n\n".join([
            f"**From {self._format_citation(item['document'])}:**\n{item['response']}"
            for item in document_responses
        ])
        
        return self._combine_with_phoenix(question, responses_text, document_responses, llm)
    
    def _combine_with_phoenix(self, question: str, responses_text: str, document_responses: List[dict], llm) -> str:
        """Combine responses using Phoenix-managed prompts."""
        try:
            print("🔗 Combining responses from multiple documents using Phoenix...")
            
            # Get the prompt from Phoenix - use separate prompt ID for combining responses
            prompt = self.phoenix_client.prompts.get(prompt_identifier=self.document_answer_prompt_id)
            
            # Format the prompt template with variables
            formatted_result = prompt.format(variables={
                "question": question,
                "responses_text": responses_text,
                "operation": "combine_multiple_responses"
            })
            
            # Extract the actual prompt text from Phoenix format
            if isinstance(formatted_result, dict) and 'messages' in formatted_result:
                # Phoenix returns OpenAI format, extract the user message content
                prompt_text = formatted_result['messages'][-1]['content']
            else:
                # Fallback if format is different
                prompt_text = str(formatted_result)
            
            # Use the existing LLM with the extracted prompt text
            response = llm.complete(prompt_text)
            return str(response).strip()
            
        except Exception as e:
            print(f"⚠️ Phoenix response combination failed: {str(e)}, using simple concatenation")
            # Fallback: simple combination
            combined = f"Based on multiple documents:\n\n{responses_text}"
            sources = "\n".join([f"- {self._format_citation(item['document'])}" for item in document_responses])
            return f"{combined}\n\n**Sources:**\n{sources}"
    
    def _format_citation(self, filename: str) -> str:
        """Format document filename into readable citation."""
        # Remove file extension and hash
        base_name = filename.replace('.md', '').split('_')[0]
        if base_name.endswith(')'):
            # Handle cases like "Procurement Manual (Business Process)"
            return base_name
        return base_name.replace('_', ' ').title()