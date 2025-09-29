"""
RAG Pipeline Service for Government Document Search.
Handles retrieval, reranking, and response generation operations.
"""

import os
from typing import List, Optional, Tuple
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.postprocessor import LLMRerank
from llama_index.core.schema import QueryBundle, NodeWithScore
from llama_index.core.vector_stores import MetadataFilters, MetadataFilter, FilterOperator


class RAGPipelineService:
    """Service for RAG pipeline operations including retrieval, reranking, and generation."""
    
    def __init__(self, retriever_top_k: int = 10, reranking_top_n: int = 3, 
                 use_reranking: bool = True, max_context_chunks: int = 3):
        """
        Initialize RAG pipeline service.
        
        Args:
            retriever_top_k: Number of documents to retrieve initially per document
            reranking_top_n: Number of documents after reranking per document
            use_reranking: Enable/disable reranking step
            max_context_chunks: Maximum chunks to use for response generation per document
        """
        self.retriever_top_k = retriever_top_k
        self.reranking_top_n = reranking_top_n
        self.use_reranking = use_reranking
        self.max_context_chunks = max_context_chunks
    
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
    
    def rerank_documents(self, retrieved_nodes: List[NodeWithScore], query_bundle: QueryBundle, 
                        llm, top_n: int) -> List[NodeWithScore]:
        """Rerank documents using configured LLM."""
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
    
    def generate_response_for_document(self, nodes: List[NodeWithScore], question: str, 
                                     doc_filename: str, llm) -> Optional[str]:
        """Generate response for a specific document."""
        if not nodes:
            return None
        
        chunks_to_use = min(len(nodes), self.max_context_chunks)
        
        context_parts = []
        for i, node in enumerate(nodes[:chunks_to_use], 1):
            context_parts.append(f"Context {i}:\n{node.text}")
        
        context = "\n\n".join(context_parts)
        doc_name = self._format_citation(doc_filename)
        
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
    
    def combine_responses_with_citations(self, question: str, document_responses: List[dict], llm) -> str:
        """Combine multiple document responses with proper citations."""
        if len(document_responses) == 1:
            # Single document response
            doc_info = document_responses[0]
            return f"{doc_info['response']}\n\n**Source:** {self._format_citation(doc_info['document'])}"
        
        # Multiple documents - combine intelligently
        responses_text = "\n\n".join([
            f"**From {self._format_citation(item['document'])}:**\n{item['response']}"
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