"""
RAG v2 Service - Full Document Loading Approach

This service detects relevant documents using the same logic as RAG v1,
but instead of vector search, it loads the entire markdown file(s) into 
the LLM context and asks the question directly.

Uses gemini-flash-lite-latest for processing.
"""

import os
from pathlib import Path
from typing import List, Optional, Dict, Any
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import google.generativeai as genai
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Import document detection from v1
from ..rag_v1.document_detection_service import DocumentDetectionService


class FullDocumentQueryInput(BaseModel):
    """Input schema for full document RAG tool."""
    question: str = Field(..., description="Question about government policies, procedures, HR, procurement, or security regulations")


class FullDocumentRAGService:
    """
    RAG v2 Service that loads entire documents instead of using vector search.
    
    Process:
    1. Use document detection to find relevant documents
    2. Load the full markdown content of those documents
    3. Send the question + full document(s) to Gemini Flash Lite
    4. Return the response with source attribution
    """
    
    def __init__(self):
        """Initialize the full document RAG service."""
        # Initialize document detection (reuse from v1)
        self.document_detector = DocumentDetectionService()
        
        # Initialize Gemini
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=self.gemini_api_key)
        self.model = genai.GenerativeModel('gemini-flash-lite-latest')
        
        # Document paths - using Mistral OCR processed files for best efficiency
        self.markdown_dir = Path(__file__).parent.parent.parent.parent / "ingestion" / "markdown-by-mistral"
        
        print(f"🔍 RAG v2 initialized with markdown directory: {self.markdown_dir}")
        print(f"🤖 Using Gemini model: gemini-flash-lite-latest")
    
    def detect_relevant_documents_v2(self, question: str) -> List[str]:
        """
        Simplified document detection for RAG v2 with clean filenames.
        """
        question_lower = question.lower()
        
        # Check for security-related terms first (more specific)
        if any(keyword in question_lower for keyword in ['security', 'data protection', 'information security', 'cyber', 'cybersecurity']):
            return ["Inforamation Security.md"]  # Note: keeping original typo in filename
        elif any(keyword in question_lower for keyword in ['hr', 'human', 'employee', 'work', 'job', 'staff', 'bylaw']):
            return ["HR Bylaws.md"]
        elif any(keyword in question_lower for keyword in ['procurement', 'purchase', 'buy', 'vendor', 'supplier', 'standard']):
            return ["Abu Dhabi Procurement Standards.md", "Procurement Manual (Business Process).md"]
        elif any(keyword in question_lower for keyword in ['ariba', 'manual', 'aligned']):
            return ["Procurement Manual (Ariba Aligned).md"]
        else:
            # Default to procurement standards if unclear
            return ["Abu Dhabi Procurement Standards.md"]
    
    def load_document_content(self, document_names: List[str]) -> Dict[str, str]:
        """
        Load the full content of the specified documents.
        
        Args:
            document_names: List of document names to load (should include .md extension)
            
        Returns:
            Dictionary mapping document names to their content
        """
        document_contents = {}
        
        for doc_name in document_names:
            # For RAG v2, we expect clean filenames directly
            file_path = self.markdown_dir / doc_name
            
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    document_contents[doc_name] = content
                    print(f"📄 Loaded document: {file_path.name} ({len(content):,} characters)")
                except Exception as e:
                    print(f"⚠️  Error loading {file_path}: {e}")
            else:
                print(f"❌ Document not found: {doc_name}")
        
        return document_contents
    
    def create_full_context_prompt(self, question: str, document_contents: Dict[str, str]) -> str:
        """
        Create a comprehensive prompt with the question and full document content(s).
        
        Args:
            question: User's question
            document_contents: Dictionary of document names to their content
            
        Returns:
            Complete prompt for the LLM
        """
        # Use static base prompt for RAG v2
        base_prompt = """You are an expert assistant for Abu Dhabi government documentation. You have access to the complete text of relevant government documents. Please provide comprehensive, accurate answers based on the provided documents.

Guidelines:
1. Answer the question thoroughly using information from the provided documents
2. Cite specific sections, articles, or parts of the documents when possible
3. If information spans multiple documents, synthesize the information appropriately
4. If the question cannot be answered from the provided documents, state this clearly
5. Maintain the authoritative tone appropriate for government documentation
6. Include relevant details like article numbers, section references, and specific requirements"""
        
        # Build the complete prompt
        prompt_parts = [base_prompt]
        
        # Add document contents
        prompt_parts.append("\n\n=== RELEVANT DOCUMENTS ===\n")
        
        for doc_name, content in document_contents.items():
            prompt_parts.append(f"\n--- DOCUMENT: {doc_name} ---\n")
            prompt_parts.append(content)
            prompt_parts.append(f"\n--- END OF {doc_name} ---\n")
        
        # Add the question
        prompt_parts.append(f"\n\n=== QUESTION ===\n{question}")
        prompt_parts.append(f"\n\n=== RESPONSE ===\nBased on the above documents, here is my comprehensive answer:")
        
        return "\n".join(prompt_parts)
    
    def create_single_document_prompt(self, question: str, doc_name: str, content: str) -> str:
        """
        Create a prompt for processing a single document.
        
        Args:
            question: User's question
            doc_name: Name of the document
            content: Document content
            
        Returns:
            Prompt for processing this single document
        """
        base_prompt = """You are an expert assistant for Abu Dhabi government documentation. You have access to one specific government document. Please provide a comprehensive answer based ONLY on the provided document.

Guidelines:
1. Answer the question thoroughly using information from the provided document
2. Cite specific sections, articles, or parts of the document when possible
3. If the question cannot be answered from this document, state this clearly
4. Maintain the authoritative tone appropriate for government documentation
5. Include relevant details like article numbers, section references, and specific requirements
6. Always end your response with the source citation in this format: **Source: [document_name]**"""
        
        prompt_parts = [
            base_prompt,
            f"\n\n=== DOCUMENT: {doc_name} ===\n",
            content,
            f"\n=== END OF {doc_name} ===\n",
            f"\n=== QUESTION ===\n{question}",
            f"\n\n=== RESPONSE ===\nBased on the above document, here is my answer:"
        ]
        
        return "\n".join(prompt_parts)
    
    def query_single_document(self, question: str, doc_name: str, content: str) -> str:
        """
        Query a single document with the question.
        
        Args:
            question: User's question
            doc_name: Document name
            content: Document content
            
        Returns:
            Response from processing this single document
        """
        try:
            print(f"🔍 Processing document: {doc_name}")
            
            # Create single document prompt
            prompt = self.create_single_document_prompt(question, doc_name, content)
            
            # Check token count
            estimated_tokens = len(prompt) // 4
            print(f"📊 Document {doc_name}: ~{estimated_tokens:,} tokens")
            
            if estimated_tokens > 900000:
                return f"Document {doc_name} is too large to process (>{estimated_tokens:,} tokens). **Source: {doc_name}**"
            
            # Query Gemini
            response = self.model.generate_content(prompt)
            
            if not response or not response.text:
                return f"No response received for document {doc_name}. **Source: {doc_name}**"
            
            print(f"✅ Processed document: {doc_name}")
            return response.text
            
        except Exception as e:
            print(f"❌ Error processing {doc_name}: {str(e)}")
            return f"Error processing document {doc_name}: {str(e)}. **Source: {doc_name}**"
    
    def join_multiple_responses(self, question: str, document_responses: Dict[str, str]) -> str:
        """
        Join multiple document responses into a comprehensive answer.
        
        Args:
            question: Original question
            document_responses: Dictionary mapping document names to their responses
            
        Returns:
            Combined response with preserved citations
        """
        try:
            print("🔗 Joining multiple document responses...")
            
            join_prompt = """You are an expert assistant for Abu Dhabi government documentation. You have received answers to the same question from multiple government documents. Your task is to synthesize these answers into one comprehensive, well-structured response.

Guidelines:
1. Combine information from all documents into a coherent, comprehensive answer
2. Preserve ALL citations and source attributions from the individual responses
3. If documents provide different perspectives, present them clearly
4. If documents contradict each other, note the discrepancies
5. Organize the information logically with clear sections
6. Use markdown formatting for better readability
7. At the end, list all sources that contributed to the answer

Individual Document Responses:
"""
            
            # Add individual responses
            for doc_name, response in document_responses.items():
                join_prompt += f"\n--- RESPONSE FROM {doc_name} ---\n{response}\n"
            
            join_prompt += f"\n--- END OF INDIVIDUAL RESPONSES ---\n\n"
            join_prompt += f"Original Question: {question}\n\n"
            join_prompt += "Please synthesize the above responses into one comprehensive answer, preserving all citations and organizing the information logically:"
            
            # Query Gemini to join responses
            response = self.model.generate_content(join_prompt)
            
            if not response or not response.text:
                # Fallback: manually join responses
                return self.manual_join_responses(question, document_responses)
            
            print("✅ Successfully joined multiple responses")
            return response.text
            
        except Exception as e:
            print(f"⚠️ Error joining responses: {str(e)}, using manual join")
            return self.manual_join_responses(question, document_responses)
    
    def manual_join_responses(self, question: str, document_responses: Dict[str, str]) -> str:
        """
        Manually join responses as a fallback method.
        
        Args:
            question: Original question
            document_responses: Dictionary mapping document names to their responses
            
        Returns:
            Manually combined response
        """
        combined_parts = [
            f"# Response to: {question}\n",
            "Based on multiple Abu Dhabi government documents, here is the comprehensive information:\n"
        ]
        
        for i, (doc_name, response) in enumerate(document_responses.items(), 1):
            combined_parts.append(f"## Information from {doc_name}\n")
            combined_parts.append(response)
            combined_parts.append("\n")
        
        # Extract all sources
        all_sources = list(document_responses.keys())
        combined_parts.append(f"\n**Sources:** {', '.join(all_sources)}")
        
        return "\n".join(combined_parts)
    
    def query_with_full_documents(self, question: str) -> str:
        """
        Process a query by loading full documents and asking Gemini.
        For multiple documents, processes them in parallel and joins results.
        
        Args:
            question: User's question
            
        Returns:
            LLM response with source attribution
        """
        try:
            print(f"🔍 Processing question: {question}")
            
            # Step 1: Detect relevant documents using v2 simplified logic
            print("📋 Detecting relevant documents...")
            relevant_docs = self.detect_relevant_documents_v2(question)
            
            if not relevant_docs:
                return "I couldn't identify any relevant documents for your question. Please try rephrasing your question or ask about Abu Dhabi government policies, HR regulations, procurement standards, or information security."
            
            print(f"📄 Found {len(relevant_docs)} relevant document(s): {', '.join(relevant_docs)}")
            
            # Step 2: Load full document content
            print("📖 Loading full document content...")
            document_contents = self.load_document_content(relevant_docs)
            
            if not document_contents:
                return "I found relevant documents but couldn't load their content. Please try again or contact support."
            
            # Step 3: Process documents - single vs multiple approach
            if len(document_contents) == 1:
                # Single document - process directly
                doc_name, content = list(document_contents.items())[0]
                print(f"� Processing single document: {doc_name}")
                return self.query_single_document(question, doc_name, content)
            
            else:
                # Multiple documents - process in parallel and join
                print(f"🔄 Processing {len(document_contents)} documents in parallel...")
                
                # Process documents in parallel using ThreadPoolExecutor
                document_responses = {}
                with ThreadPoolExecutor(max_workers=min(len(document_contents), 3)) as executor:
                    # Submit all document processing tasks
                    future_to_doc = {
                        executor.submit(self.query_single_document, question, doc_name, content): doc_name
                        for doc_name, content in document_contents.items()
                    }
                    
                    # Collect results as they complete
                    for future in future_to_doc:
                        doc_name = future_to_doc[future]
                        try:
                            response = future.result()
                            document_responses[doc_name] = response
                        except Exception as e:
                            print(f"❌ Error processing {doc_name}: {str(e)}")
                            document_responses[doc_name] = f"Error processing {doc_name}: {str(e)}. **Source: {doc_name}**"
                
                # Step 4: Join responses from multiple documents
                if len(document_responses) > 1:
                    return self.join_multiple_responses(question, document_responses)
                elif len(document_responses) == 1:
                    # Only one document processed successfully
                    return list(document_responses.values())[0]
                else:
                    return "All document processing failed. Please try again or contact support."
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Error in full document query: {error_msg}")
            
            # Handle specific error types
            if "quota" in error_msg.lower() or "limit" in error_msg.lower():
                return "The AI service is currently at capacity. Please try again in a moment."
            elif "content" in error_msg.lower() and "too long" in error_msg.lower():
                return "The document content is too large for processing. This approach works best with shorter documents."
            else:
                return f"An error occurred while processing your question: {error_msg}. Please try again or rephrase your question."


class FullDocumentTool(BaseTool):
    """
    CrewAI tool for full document RAG approach.
    
    This tool detects relevant documents and loads their complete content
    into the LLM context instead of using vector search.
    """
    
    name: str = "full_document_search"
    description: str = """FALLBACK TOOL: Use this ONLY if government_document_search fails to get data, as this is compute heavy and takes time.
    This tool should only be used if the primary government_document_search tool returns "No relevant information found".
    Search Abu Dhabi government documents using full document loading approach which is more comprehensive but slower.
    This tool identifies relevant documents (HR bylaws, procurement standards, information security policies) 
    and loads their complete content to provide comprehensive answers when vector search fails.
    WARNING: This tool processes entire documents (50k-150k tokens) and takes significantly more time and compute resources.
    Only use this tool as a last resort when the faster government_document_search tool cannot find relevant information.
    The tool automatically selects and loads the most relevant documents for your question."""
    args_schema: type[BaseModel] = FullDocumentQueryInput
    
    def __init__(self):
        super().__init__()
        self._rag_service = None
    
    @property
    def rag_service(self):
        if self._rag_service is None:
            self._rag_service = FullDocumentRAGService()
        return self._rag_service
    
    def _run(self, question: str) -> str:
        """Execute the full document search."""
        return self.rag_service.query_with_full_documents(question)


# Create singleton instance for use in CrewAI
full_document_tool = FullDocumentTool()