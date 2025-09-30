from crewai.tools import BaseTool
from typing import Type, ClassVar
from pydantic import BaseModel, Field

from .document_detection_service import DocumentDetectionService
from .rag_pipeline_service import RAGPipelineService
from .llm_configuration_service import LLMConfigurationService
from .database_service import DatabaseService


class GovernmentQueryInput(BaseModel):
    """Input schema for government document search tool."""
    question: str = Field(..., description="Question about government policies, procedures, HR, procurement, or security regulations")


class GovernmentDocumentTool(BaseTool):
    """
    Modular Government Document Search Tool.
    
    This tool provides comprehensive search across Abu Dhabi government documents
    including HR bylaws, procurement standards, information security policies,
    and related regulations. It uses a modular architecture with separate services
    for different responsibilities.
    """
    
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
    
    # Configuration
    retriever_top_k: ClassVar[int] = 30          # Number of documents to retrieve initially per document
    use_reranking: ClassVar[bool] = True          # Enable/disable reranking step
    reranking_top_n: ClassVar[int] = 30            # Number of documents after reranking per document
    max_context_chunks: ClassVar[int] = 10         # Maximum chunks to use for response generation per document
    
    def _get_services(self):
        """Get service instances (lazy initialization)."""
        if not hasattr(self, '_services_initialized'):
            self._document_detection = DocumentDetectionService()
            self._rag_pipeline = RAGPipelineService(
                retriever_top_k=self.retriever_top_k,
                reranking_top_n=self.reranking_top_n,
                use_reranking=self.use_reranking,
                max_context_chunks=self.max_context_chunks
            )
            self._llm_config = LLMConfigurationService()
            self._database = DatabaseService()
            self._services_initialized = True
        
        return self._document_detection, self._rag_pipeline, self._llm_config, self._database
    
    def _run(self, question: str) -> str:
        """Main RAG pipeline execution with multi-document processing."""
        try:
            print(f"\n🔍 Government Document Query: {question}")
            print("=" * 50)
            
            # Get services
            document_detection, rag_pipeline, llm_config, database = self._get_services()
            
            # Step 0: Setup components
            print("🔧 Setting up RAG components...")
            vector_store, embed_model, index = database.setup_components()
            primary_llm, secondary_llm = llm_config.setup_llms()
            print("✅ Components setup completed")
            
            # Step 1: Detect relevant documents
            print("🎯 Detecting relevant documents for query...")
            relevant_documents = document_detection.detect_relevant_documents(question, primary_llm)
            print(f"📋 Selected documents: {relevant_documents}")
            
            if not relevant_documents:
                return "No relevant documents found for your query. Please try rephrasing your question."
            
            # Step 2: Process each document in parallel (simulated)
            print("🔄 Processing documents in parallel...")
            document_responses = []
            
            for doc_filename in relevant_documents:
                print(f"\n Processing: {doc_filename}")
                doc_response = rag_pipeline.process_single_document(
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
            final_response = rag_pipeline.combine_responses_with_citations(
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


# Create singleton instance
rag_document_tool = GovernmentDocumentTool()