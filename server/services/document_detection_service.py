"""
Document Detection Service for Government Document Search.
Handles intelligent detection of relevant documents based on user queries.
"""

from typing import List, Dict
import ast


class DocumentDetectionService:
    """Service for detecting relevant documents based on user queries."""
    
    def __init__(self):
        """Initialize document detection service with document descriptions."""
        self.available_documents = [
            "Abu Dhabi Procurement Standards_0ef9c4a0.md",
            "HR Bylaws_2f9c1749.md", 
            "Inforamation Security_8ac2fee2.md",
            "Procurement Manual (Ariba Aligned)_f679b7db.md",
            "Procurement Manual (Business Process)_66d86f21.md"
        ]
        
        self.document_descriptions = {
            "Abu Dhabi Procurement Standards_0ef9c4a0.md": "Abu Dhabi procurement standards, guidelines, and regulations",
            "HR Bylaws_2f9c1749.md": "Human resources bylaws, employment regulations, and HR policies", 
            "Inforamation Security_8ac2fee2.md": "Information security policies, data protection, and cybersecurity guidelines",
            "Procurement Manual (Ariba Aligned)_f679b7db.md": "Ariba-aligned procurement processes and manual",
            "Procurement Manual (Business Process)_66d86f21.md": "Business process procurement manual and procedures"
        }
    
    def detect_relevant_documents(self, question: str, llm) -> List[str]:
        """Detect which documents are relevant for the user query."""
        documents_list = "\n".join([
            f"- {filename}: {description}" 
            for filename, description in self.document_descriptions.items()
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
            
            # Default fallback based on keywords
            return self._fallback_document_detection(question)
                
        except Exception as e:
            print(f"⚠️ Document detection failed: {str(e)}, using fallback detection")
            return self._fallback_document_detection(question)
    
    def _fallback_document_detection(self, question: str) -> List[str]:
        """Fallback document detection based on keywords."""
        question_lower = question.lower()
        
        if any(keyword in question_lower for keyword in ['hr', 'human', 'employee', 'work', 'job', 'staff']):
            return ["HR Bylaws_2f9c1749.md"]
        elif any(keyword in question_lower for keyword in ['procurement', 'purchase', 'buy', 'vendor', 'supplier']):
            return ["Abu Dhabi Procurement Standards_0ef9c4a0.md", "Procurement Manual (Business Process)_66d86f21.md"]
        elif any(keyword in question_lower for keyword in ['security', 'data', 'information', 'cyber']):
            return ["Inforamation Security_8ac2fee2.md"]
        else:
            # Default to HR if unclear
            return ["HR Bylaws_2f9c1749.md"]
    
    def format_citation(self, filename: str) -> str:
        """Format document filename into readable citation."""
        # Remove file extension and hash
        base_name = filename.replace('.md', '').split('_')[0]
        if base_name.endswith(')'):
            # Handle cases like "Procurement Manual (Business Process)"
            return base_name
        return base_name.replace('_', ' ').title()