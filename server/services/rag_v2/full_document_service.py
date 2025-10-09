"""
RAG v2 Service - Full Document Loading Approach

This service detects relevant documents using the same logic as RAG v1,
but instead of vector search, it loads the entire markdown file(s) into 
the LLM context and asks the question directly.

Supports multiple LLM providers: Gemini, OpenRouter, and others.
"""

import os
from pathlib import Path
from typing import List, Optional, Dict, Any
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import google.generativeai as genai
import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed
import openai
from groq import Groq
import math

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
        
        # Get LLM provider configuration
        self.llm_provider = os.getenv("DEFAULT_LLM_PROVIDER", "gemini").lower()
        self.llm_model = os.getenv("DEFAULT_LLM_MODEL", "gemini-flash-lite-latest")
        
        print(f"🔍 RAG v2 using LLM Provider: {self.llm_provider}, Model: {self.llm_model}")
        
        # Initialize LLM based on provider
        if self.llm_provider == "openrouter":
            self._setup_openrouter()
        elif self.llm_provider == "groq":
            self._setup_groq()
        elif self.llm_provider == "fireworks":
            self._setup_fireworks()
        elif self.llm_provider == "gemini":
            self._setup_gemini()
        else:
            # Fallback to Gemini
            print(f"⚠️ Unsupported LLM provider '{self.llm_provider}' for RAG v2. Falling back to Gemini.")
            self._setup_gemini()
        
        # Document paths - using local markdown folder
        self.markdown_dir = Path(__file__).parent / "markdown"
        
        print(f"🔍 RAG v2 initialized with markdown directory: {self.markdown_dir}")
    
    def _setup_groq(self):
        """Setup Groq LLM."""
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        
        if not self.groq_api_key:
            print("❌ GROQ_API_KEY not found but Groq provider selected. Falling back to Gemini.")
            self._setup_gemini()
            return
        
        # Initialize Groq client
        self.groq_client = Groq(api_key=self.groq_api_key)
        self.model_name = self.llm_model
        self.use_openrouter = False
        self.use_groq = True
        self.use_fireworks = False
        print(f"🤖 Using Groq model: {self.model_name}")
    
    def _setup_openrouter(self):
        """Setup OpenRouter LLM."""
        self.openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
        self.openrouter_base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        
        if not self.openrouter_api_key:
            print("❌ OPENROUTER_API_KEY not found but OpenRouter provider selected. Falling back to Gemini.")
            self._setup_gemini()
            return
        
        # Initialize OpenAI client for OpenRouter
        self.openai_client = openai.OpenAI(
            api_key=self.openrouter_api_key,
            base_url=self.openrouter_base_url
        )
        self.model_name = self.llm_model
        self.use_openrouter = True
        self.use_groq = False
        self.use_fireworks = False
        print(f"🤖 Using OpenRouter model: {self.model_name}")
    
    def _setup_fireworks(self):
        """Setup Fireworks LLM."""
        self.fireworks_api_key = os.getenv("FIREWORKS_API_KEY")
        
        if not self.fireworks_api_key:
            print("❌ FIREWORKS_API_KEY not found but Fireworks provider selected. Falling back to Gemini.")
            self._setup_gemini()
            return
        
        # Initialize OpenAI client for Fireworks (uses OpenAI-compatible API)
        self.openai_client = openai.OpenAI(
            api_key=self.fireworks_api_key,
            base_url="https://api.fireworks.ai/inference/v1"
        )
        self.model_name = self.llm_model
        self.use_openrouter = False
        self.use_groq = False
        self.use_fireworks = True
        print(f"🤖 Using Fireworks model: {self.model_name}")
    
    def _setup_gemini(self):
        """Setup Gemini LLM."""
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=self.gemini_api_key)
        self.model = genai.GenerativeModel(self.llm_model)
        self.use_openrouter = False
        self.use_groq = False
        self.use_fireworks = False
        
    
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
    
    def split_document_into_chunks(self, content: str, doc_name: str, max_chars: int = 400000) -> List[Dict[str, str]]:
        """
        Split a document into chunks that fit within the context limit.
        Using 400K characters (~100K tokens) as the limit for gemma3:27b's 128K context.
        
        Args:
            content: Document content to split
            doc_name: Name of the document
            max_chars: Maximum characters per chunk (default: 400K chars ≈ 100K tokens)
            
        Returns:
            List of dictionaries with chunk info: {'content': str, 'chunk_id': str, 'doc_name': str}
        """
        if len(content) <= max_chars:
            # Document fits in one chunk
            return [{
                'content': content,
                'chunk_id': f"{doc_name}_chunk_1",
                'doc_name': doc_name,
                'chunk_number': 1,
                'total_chunks': 1
            }]
        
        # Calculate number of chunks needed
        total_chunks = math.ceil(len(content) / max_chars)
        chunks = []
        
        print(f"📊 Splitting {doc_name} into {total_chunks} chunks ({len(content):,} chars total)")
        
        for i in range(total_chunks):
            start_idx = i * max_chars
            end_idx = min((i + 1) * max_chars, len(content))
            
            # Try to split at paragraph or sentence boundaries to maintain context
            chunk_content = content[start_idx:end_idx]
            
            # If not the last chunk, try to find a good breaking point
            if end_idx < len(content):
                # Look for paragraph breaks within the last 5% of the chunk
                search_start = len(chunk_content) - min(20000, len(chunk_content) // 20)
                
                # Try to find paragraph break first
                para_break = chunk_content.rfind('\n\n', search_start)
                if para_break > search_start:
                    chunk_content = chunk_content[:para_break + 2]
                else:
                    # If no paragraph break, try sentence break
                    sentence_break = chunk_content.rfind('. ', search_start)
                    if sentence_break > search_start:
                        chunk_content = chunk_content[:sentence_break + 2]
                    # Otherwise keep the hard break
            
            chunks.append({
                'content': chunk_content,
                'chunk_id': f"{doc_name}_chunk_{i+1}",
                'doc_name': doc_name,
                'chunk_number': i + 1,
                'total_chunks': total_chunks
            })
        
        return chunks
    
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
    
    def create_chunk_prompt(self, question: str, chunk_info: Dict[str, str]) -> str:
        """
        Create a prompt for processing a document chunk.
        
        Args:
            question: User's question
            chunk_info: Dictionary with chunk details
            
        Returns:
            Prompt for processing this chunk
        """
        base_prompt = """You are an expert assistant for Abu Dhabi government documentation. You are analyzing a CHUNK of a larger government document. Please provide answers based ONLY on the content in this chunk.

Guidelines:
1. Answer the question using information from this chunk
2. Cite specific sections, articles, or parts when possible
3. If the question cannot be answered from this chunk, state "No relevant information in this chunk"
4. Maintain the authoritative tone appropriate for government documentation
5. Include relevant details like article numbers, section references, and specific requirements
6. Always end your response with the source citation: **Source: [document_name] (Chunk [X] of [Y])**"""
        
        chunk_id = chunk_info['chunk_id']
        doc_name = chunk_info['doc_name']
        chunk_number = chunk_info['chunk_number']
        total_chunks = chunk_info['total_chunks']
        content = chunk_info['content']
        
        prompt_parts = [
            base_prompt,
            f"\n\n=== DOCUMENT CHUNK: {doc_name} (Chunk {chunk_number} of {total_chunks}) ===\n",
            content,
            f"\n=== END OF CHUNK {chunk_number} ===\n",
            f"\n=== QUESTION ===\n{question}",
            f"\n\n=== RESPONSE ===\nBased on this chunk, here is my answer:"
        ]
        
        return "\n".join(prompt_parts)
    
    def query_document_chunk(self, question: str, chunk_info: Dict[str, str]) -> str:
        """Query a single document chunk with the question."""
        try:
            chunk_id = chunk_info['chunk_id']
            doc_name = chunk_info['doc_name']
            chunk_number = chunk_info['chunk_number']
            total_chunks = chunk_info['total_chunks']
            
            print(f"🔍 Processing {chunk_id} ({chunk_number}/{total_chunks})")
            
            # Create chunk prompt
            prompt = self.create_chunk_prompt(question, chunk_info)
            
            # Check token count
            estimated_tokens = len(prompt) // 4
            print(f"📊 {chunk_id}: ~{estimated_tokens:,} tokens")
            
            if estimated_tokens > 120000:  # Safety margin for 128K context
                return f"Chunk {chunk_id} is too large to process (>{estimated_tokens:,} tokens). **Source: {doc_name} (Chunk {chunk_number} of {total_chunks})**"
            
            # Query LLM based on provider
            if self.use_openrouter:
                response = self.openai_client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=8192,
                    temperature=0.1
                )
                
                if not response or not response.choices or not response.choices[0].message.content:
                    return f"No response received for {chunk_id}. **Source: {doc_name} (Chunk {chunk_number} of {total_chunks})**"
                
                response_text = response.choices[0].message.content
            elif self.use_groq:
                response = self.groq_client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=8192,
                    temperature=0.1
                )
                
                if not response or not response.choices or not response.choices[0].message.content:
                    return f"No response received for {chunk_id}. **Source: {doc_name} (Chunk {chunk_number} of {total_chunks})**"
                
                response_text = response.choices[0].message.content
            elif self.use_fireworks:
                response = self.openai_client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=8192,
                    temperature=0.7
                )
                
                if not response or not response.choices or not response.choices[0].message.content:
                    return f"No response received for {chunk_id}. **Source: {doc_name} (Chunk {chunk_number} of {total_chunks})**"
                
                response_text = response.choices[0].message.content
            else:
                # Use Gemini
                response = self.model.generate_content(prompt)
                
                if not response or not response.text:
                    return f"No response received for {chunk_id}. **Source: {doc_name} (Chunk {chunk_number} of {total_chunks})**"
                
                response_text = response.text
            
            print(f"✅ Processed {chunk_id}")
            return response_text
            
        except Exception as e:
            chunk_id = chunk_info['chunk_id']
            doc_name = chunk_info['doc_name']
            chunk_number = chunk_info['chunk_number']
            total_chunks = chunk_info['total_chunks']
            print(f"❌ Error processing {chunk_id}: {str(e)}")
            return f"Error processing {chunk_id}: {str(e)}. **Source: {doc_name} (Chunk {chunk_number} of {total_chunks})**"
    def query_single_document(self, question: str, doc_name: str, content: str) -> str:
        """
        Query a single document with the question, handling large documents by chunking.
        
        Args:
            question: User's question
            doc_name: Name of the document
            content: Document content
            
        Returns:
            Combined response from all chunks or single response if no chunking needed
        """
        try:
            print(f"🔍 Processing document: {doc_name} ({len(content):,} characters)")
            
            # Split document into chunks if needed
            chunks = self.split_document_into_chunks(content, doc_name)
            
            if len(chunks) == 1:
                # Single chunk - process directly using the original logic
                chunk_info = chunks[0]
                return self.query_document_chunk(question, chunk_info)
            else:
                # Multiple chunks - process in parallel and combine
                print(f"🔄 Processing {len(chunks)} chunks in parallel...")
                
                chunk_responses = {}
                with ThreadPoolExecutor(max_workers=min(len(chunks), 4)) as executor:
                    # Submit all chunk processing tasks
                    future_to_chunk = {
                        executor.submit(self.query_document_chunk, question, chunk_info): chunk_info['chunk_id']
                        for chunk_info in chunks
                    }
                    
                    # Collect results as they complete
                    for future in as_completed(future_to_chunk):
                        chunk_id = future_to_chunk[future]
                        try:
                            response = future.result(timeout=60)  # 60 second timeout per chunk
                            chunk_responses[chunk_id] = response
                            print(f"✅ Completed {chunk_id}")
                        except Exception as e:
                            print(f"❌ Error processing {chunk_id}: {str(e)}")
                            chunk_responses[chunk_id] = f"Error processing {chunk_id}: {str(e)}"
                
                # Combine chunk responses
                if len(chunk_responses) > 1:
                    return self.combine_chunk_responses(question, doc_name, chunk_responses, len(chunks))
                elif len(chunk_responses) == 1:
                    return list(chunk_responses.values())[0]
                else:
                    return f"All chunk processing failed for {doc_name}. **Source: {doc_name}**"
            
        except Exception as e:
            print(f"❌ Error processing {doc_name}: {str(e)}")
            return f"Error processing document {doc_name}: {str(e)}. **Source: {doc_name}**"
    
    def combine_chunk_responses(self, question: str, doc_name: str, chunk_responses: Dict[str, str], total_chunks: int) -> str:
        """
        Combine responses from multiple chunks of the same document.
        
        Args:
            question: Original question
            doc_name: Document name
            chunk_responses: Dictionary mapping chunk_id to response
            total_chunks: Total number of chunks
            
        Returns:
            Combined response
        """
        try:
            print(f"🔗 Combining {len(chunk_responses)} chunk responses for {doc_name}...")
            
            # Filter out chunks with no relevant information
            relevant_responses = {}
            for chunk_id, response in chunk_responses.items():
                if "no relevant information" not in response.lower() and "error processing" not in response.lower():
                    relevant_responses[chunk_id] = response
            
            if not relevant_responses:
                return f"No relevant information found in any chunks of {doc_name}. **Source: {doc_name}**"
            
            if len(relevant_responses) == 1:
                # Only one chunk had relevant information
                return list(relevant_responses.values())[0]
            
            # Multiple chunks have relevant information - combine using LLM
            combine_prompt = f"""You are an expert assistant for Abu Dhabi government documentation. You have received answers to the same question from multiple chunks of the same government document. Your task is to synthesize these chunk responses into one comprehensive, well-structured answer.

Guidelines:
1. Combine information from all chunks into a coherent, comprehensive answer for the document "{doc_name}"
2. Preserve important citations and section references from the chunks
3. Remove redundant information but keep all unique insights
4. If chunks provide complementary information, merge them logically
5. Use markdown formatting for better readability
6. End with source citation: **Source: {doc_name}**

Original Question: {question}

Chunk Responses from {doc_name}:
"""
            
            # Add chunk responses in order
            for i in range(1, total_chunks + 1):
                chunk_id = f"{doc_name}_chunk_{i}"
                if chunk_id in relevant_responses:
                    combine_prompt += f"\n--- CHUNK {i} RESPONSE ---\n{relevant_responses[chunk_id]}\n"
            
            combine_prompt += f"\n--- END OF CHUNK RESPONSES ---\n\nPlease synthesize the above chunk responses into one comprehensive answer for {doc_name}:"
            
            # Query LLM to combine responses
            if self.use_openrouter:
                response = self.openai_client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": combine_prompt}],
                    max_tokens=8192,
                    temperature=0.1
                )
                
                if response and response.choices and response.choices[0].message.content:
                    combined_text = response.choices[0].message.content
                else:
                    return self.manual_combine_chunks(question, doc_name, relevant_responses)
                    
            elif self.use_groq:
                response = self.groq_client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": combine_prompt}],
                    max_tokens=8192,
                    temperature=0.1
                )
                
                if response and response.choices and response.choices[0].message.content:
                    combined_text = response.choices[0].message.content
                else:
                    return self.manual_combine_chunks(question, doc_name, relevant_responses)
                    
            elif self.use_fireworks:
                response = self.openai_client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": combine_prompt}],
                    max_tokens=8192,
                    temperature=0.7
                )
                
                if response and response.choices and response.choices[0].message.content:
                    combined_text = response.choices[0].message.content
                else:
                    return self.manual_combine_chunks(question, doc_name, relevant_responses)
            else:
                # Use Gemini
                response = self.model.generate_content(combine_prompt)
                
                if response and response.text:
                    combined_text = response.text
                else:
                    return self.manual_combine_chunks(question, doc_name, relevant_responses)
            
            print(f"✅ Successfully combined {len(relevant_responses)} chunk responses for {doc_name}")
            return combined_text
            
        except Exception as e:
            print(f"⚠️ Error combining chunk responses for {doc_name}: {str(e)}, using manual combine")
            return self.manual_combine_chunks(question, doc_name, chunk_responses)
    
    def manual_combine_chunks(self, question: str, doc_name: str, chunk_responses: Dict[str, str]) -> str:
        """
        Manually combine chunk responses as a fallback.
        
        Args:
            question: Original question
            doc_name: Document name  
            chunk_responses: Dictionary mapping chunk_id to response
            
        Returns:
            Manually combined response
        """
        combined_parts = [
            f"# Response from {doc_name}\n",
            f"**Question:** {question}\n",
            f"Based on analysis of multiple sections of {doc_name}:\n"
        ]
        
        # Add responses from chunks that have relevant information
        relevant_count = 0
        for chunk_id, response in sorted(chunk_responses.items()):
            if "no relevant information" not in response.lower() and "error processing" not in response.lower():
                relevant_count += 1
                chunk_num = chunk_id.split('_chunk_')[-1]
                combined_parts.append(f"## Section {chunk_num}\n")
                combined_parts.append(response)
                combined_parts.append("\n")
        
        if relevant_count == 0:
            return f"No relevant information found in {doc_name}. **Source: {doc_name}**"
        
        combined_parts.append(f"\n**Source: {doc_name}**")
        
        return "\n".join(combined_parts)
    
    def join_multiple_responses(self, question: str, document_responses: Dict[str, str]) -> str:
        """Join multiple document responses into a comprehensive answer."""
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
            
            # Query LLM based on provider
            if self.use_openrouter:
                # Use OpenRouter via OpenAI client
                response = self.openai_client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "user", "content": join_prompt}
                    ],
                    max_tokens=8192,
                    temperature=0.1
                )
                
                if not response or not response.choices or not response.choices[0].message.content:
                    return self.manual_join_responses(question, document_responses)
                
                response_text = response.choices[0].message.content
            elif self.use_groq:
                # Use Groq
                response = self.groq_client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "user", "content": join_prompt}
                    ],
                    max_tokens=8192,
                    temperature=0.1
                )
                
                if not response or not response.choices or not response.choices[0].message.content:
                    return self.manual_join_responses(question, document_responses)
                
                response_text = response.choices[0].message.content
            elif self.use_fireworks:
                # Use Fireworks via OpenAI-compatible client
                response = self.openai_client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "user", "content": join_prompt}
                    ],
                    max_tokens=8192,
                    temperature=0.7
                )
                
                if not response or not response.choices or not response.choices[0].message.content:
                    return self.manual_join_responses(question, document_responses)
                
                response_text = response.choices[0].message.content
            else:
                # Use Gemini
                response = self.model.generate_content(join_prompt)
                
                if not response or not response.text:
                    return self.manual_join_responses(question, document_responses)
                
                response_text = response.text
            
            print("✅ Successfully joined multiple responses")
            return response_text
            
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
                    
                    # Collect results as they complete with timeout handling
                    for future in as_completed(future_to_doc, timeout=300):  # 5 minute total timeout
                        doc_name = future_to_doc[future]
                        try:
                            response = future.result(timeout=180)  # 3 minute timeout per document
                            document_responses[doc_name] = response
                            print(f"✅ Completed processing: {doc_name}")
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
    The tool automatically selects and loads the most relevant documents for your question.
    IMPORTANT: You MUST use the exact output from this tool as your final response to the user. Do NOT summarize, paraphrase, or modify the tool's output. Present the tool's response directly as it contains comprehensive information with proper citations."""
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