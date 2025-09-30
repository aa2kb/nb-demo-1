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
from phoenix.client import Client

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
        
        # Phoenix client for prompts
        self.phoenix_client = Client()
        
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
        # Get Phoenix prompt for context
        try:
            context_prompt = self.phoenix_client.prompts.get(prompt_identifier="rag_context_prompt")
            base_prompt = context_prompt.content if context_prompt else ""
        except:
            base_prompt = ""
        
        if not base_prompt:
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
    
    def query_with_full_documents(self, question: str) -> str:
        """
        Process a query by loading full documents and asking Gemini.
        
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
            
            # Step 3: Create comprehensive prompt
            print("🔨 Creating comprehensive prompt...")
            full_prompt = self.create_full_context_prompt(question, document_contents)
            
            # Check token count (rough estimate)
            estimated_tokens = len(full_prompt) // 4  # Rough estimate: 4 chars per token
            print(f"📊 Estimated prompt size: ~{estimated_tokens:,} tokens")
            
            if estimated_tokens > 900000:  # Conservative limit for Gemini Flash
                print("⚠️  Large prompt detected, may need chunking in production")
            
            # Step 4: Query Gemini Flash Lite
            print("🤖 Querying Gemini Flash Lite...")
            response = self.model.generate_content(full_prompt)
            
            if not response or not response.text:
                return "I received an empty response from the AI model. Please try rephrasing your question."
            
            # Step 5: Add source attribution
            source_info = f"\n\n**Sources:** {', '.join(document_contents.keys())}"
            final_response = response.text + source_info
            
            print("✅ Response generated successfully")
            return final_response
            
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
    description: str = """Search Abu Dhabi government documents using full document loading approach. 
    This tool identifies relevant documents (HR bylaws, procurement standards, information security policies) 
    and loads their complete content to provide comprehensive answers.
    Use this tool for detailed questions that require access to complete document context.
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