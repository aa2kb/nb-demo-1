from typing import List, Dict
import ast
import os
from phoenix.client import Client


class DocumentDetectionService:
    """Service for detecting relevant documents based on user queries."""
    
    def __init__(self):
        """Initialize document detection service with document descriptions."""


        self.available_documents = [
            "Abu Dhabi Procurement Standards.md",
            "HR Bylaws.md", 
            "Information Security.md",
            "Procurement Manual (Ariba Aligned).md",
            "Procurement Manual (Business Process).md"
        ]
        

        self.document_descriptions = {
            "Abu Dhabi Procurement Standards.md": "Defines the core procurement standards and governance principles for Abu Dhabi entities — outlining delivery and payment terms, intellectual property ownership, and exception code usage in purchase orders.",
            "HR Bylaws.md": "Establishes the human resources framework for Abu Dhabi government employees — covering employment regulations, disciplinary actions, penalties, and overall HR governance structure.",
            "Information Security.md": "Outlines cybersecurity, data protection, and information assurance requirements — detailing risk-based controls, credential management, and criteria for defining critical entities.",
            "Procurement Manual (Ariba Aligned).md": "Describes SAP Ariba–aligned procurement procedures — explaining team roles, supplier registration, sourcing event structures, and digital procurement workflows.",
            "Procurement Manual (Business Process).md": "Provides comprehensive business process guidelines for procurement — differentiating sourcing methods, supplier qualification, and the use of competitive bidding models like reverse auctions."
        }

        
        # Phoenix configuration
        self.phoenix_prompt_id = os.getenv("DOCUMENT_DETECTION_ID", "document_detection")
        
        # Always initialize Phoenix client
        try:
            self.phoenix_client = Client()
            print("✅ Phoenix client initialized successfully for document detection")
        except Exception as e:
            print(f"❌ Failed to initialize Phoenix client: {str(e)}")
            raise Exception(f"Phoenix client initialization failed: {str(e)}")
    
    def _get_prompt_variables(self, question: str) -> dict:
        """Get standardized prompt variables for both Phoenix and traditional LLM approaches."""
        documents_list = "\n".join([
            f"- {filename}: {description}" 
            for filename, description in self.document_descriptions.items()
        ])
        
        return {
            "question": question,
            "documents_list": documents_list,
            "example_responses": '["HR Bylaws.md"]\n["Abu Dhabi Procurement Standards.md", "Procurement Manual (Business Process).md"]'
        }
    
    def detect_relevant_documents(self, question: str, llm) -> List[str]:
        """Detect which documents are relevant for the user query using Phoenix-managed prompts."""
        return self._detect_with_phoenix(question, llm)
    
    def _detect_with_phoenix(self, question: str, llm) -> List[str]:
        """Use Phoenix-managed prompts for document detection."""
        try:
            print("🤖 Analyzing question to detect relevant documents...")
            
            # Get standardized variables
            variables = self._get_prompt_variables(question)
            
            # Get the prompt from Phoenix
            prompt = self.phoenix_client.prompts.get(prompt_identifier=self.phoenix_prompt_id)
            
            # Format the prompt template with variables
            formatted_result = prompt.format(variables=variables)
            
            # Extract the actual prompt text from Phoenix format
            if isinstance(formatted_result, dict) and 'messages' in formatted_result:
                # Phoenix returns standard format, extract the user message content
                prompt_text = formatted_result['messages'][-1]['content']
            else:
                # Fallback if format is different
                prompt_text = str(formatted_result)
            
            # Use the existing LLM with the extracted prompt text
            response = llm.complete(prompt_text)
            response_text = str(response).strip()
            
            parsed_docs = self._parse_response(response_text)
            
            # If parsing succeeded, return results; otherwise use fallback
            return parsed_docs if parsed_docs else self._fallback_document_detection(question)
                
        except Exception as e:
            print(f"⚠️ Phoenix document detection failed: {str(e)}, using fallback detection")
            return self._fallback_document_detection(question)
    
    def _parse_response(self, response_text: str) -> List[str]:
        """Parse LLM response to extract document list."""
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
        
        # If parsing fails, return empty list to trigger fallback
        return []
    
    def _fallback_document_detection(self, question: str) -> List[str]:
        """Fallback document detection based on keywords."""
        question_lower = question.lower()
        
        if any(keyword in question_lower for keyword in ['hr', 'human', 'employee', 'work', 'job', 'staff']):
            return ["HR Bylaws.md"]
        elif any(keyword in question_lower for keyword in ['procurement', 'purchase', 'buy', 'vendor', 'supplier']):
            return ["Abu Dhabi Procurement Standards_0ef9c4a0.md", "Procurement Manual (Business Process)_66d86f21.md"]
        elif any(keyword in question_lower for keyword in ['security', 'data', 'information', 'cyber']):
            return ["Inforamation Security.md"]
        else:
            # Default to HR if unclear
            return ["HR Bylaws.md"]
    
    def format_citation(self, filename: str) -> str:
        """Format document filename into readable citation."""
        # Remove file extension and hash
        base_name = filename.replace('.md', '').split('_')[0]
        if base_name.endswith(')'):
            # Handle cases like "Procurement Manual (Business Process)"
            return base_name
        return base_name.replace('_', ' ').title()