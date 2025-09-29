# Document Detection Service - Phoenix Integration

## Overview
The Document Detection Service now uses **Phoenix-only** approach for intelligent document detection. When Phoenix is disabled, it falls back to keyword-based detection. This eliminates all direct LLM calls and ensures consistent prompt management.

## Architecture

### 🚀 **Phoenix Mode (Recommended)**
- Uses Arize Phoenix for centralized prompt management
- OpenAI API for inference
- Structured variable passing
- Version control for prompts

### 🔄 **Fallback Mode (Default)**
- Keyword-based document detection
- No LLM calls required
- Fast and reliable
- Works without external dependencies

## Environment Variables

### Phoenix Configuration
- `USE_PHOENIX_PROMPTS=true` - Enable Phoenix prompt management (default: false)
- `PHOENIX_DOCUMENT_DETECTION_PROMPT_ID` - Phoenix prompt version ID
- `OPENAI_API_KEY` - Required when using Phoenix

### No LLM Configuration Needed
- No need for `DEFAULT_LLM_PROVIDER` or `GEMINI_API_KEY` for document detection
- Document detection is independent of RAG LLM configuration

## Phoenix Prompt Template

When creating a prompt in Phoenix, use these variables:

```
{{question}} - The user's question
{{documents_list}} - Formatted list of available documents with descriptions
```

### Example Phoenix Prompt Template

```
Given the following user question and available documents, determine which documents are most relevant to answer the question.

User Question: {{question}}

Available Documents:
{{documents_list}}

Instructions:
1. Analyze the question to understand what type of information is needed
2. Select 1-3 most relevant documents that could contain the answer
3. Return ONLY a Python list of document filenames (exact names as shown above)
4. If unsure, include documents that might be related

Example responses:
{{example_responses}}

Your response (only the list):
```

## Code Architecture

The cleaned up service eliminates ALL direct LLM calls:

1. **Phoenix-Only Approach**: When enabled, uses Phoenix with OpenAI for inference
2. **Keyword Fallback**: When disabled, uses fast keyword-based detection
3. **No LLM Dependencies**: Document detection is independent of RAG LLM configuration
4. **Simplified Interface**: No longer requires LLM parameter in method calls

```python
# Simple interface - no LLM required
service.detect_relevant_documents("What are working hours?")

# Phoenix mode: Uses Phoenix + OpenAI
# Fallback mode: Uses keyword detection
```

## Usage Modes

### 1. Phoenix Mode (Recommended for Production)
```bash
export USE_PHOENIX_PROMPTS=true
export PHOENIX_DOCUMENT_DETECTION_PROMPT_ID="your_prompt_version_id"
export OPENAI_API_KEY="your_openai_key"
```

Benefits:
- Centralized prompt management
- Version control for prompts
- A/B testing capabilities
- Performance monitoring
- Easy prompt updates without code changes

### 2. Keyword Fallback Mode (Default)
```bash
export USE_PHOENIX_PROMPTS=false
# No additional configuration needed
```

Benefits:
- No external dependencies
- Fast keyword-based detection
- Reliable fallback mechanism
- Zero configuration

## Fallback Strategy

The service implements a simple but effective fallback strategy:

1. **Primary**: Phoenix prompts (if enabled and configured)
2. **Fallback**: Keyword-based detection using predefined rules
3. **Default**: HR Bylaws document if no keywords match

## Testing

You can test both modes:

```python
# Test Phoenix mode
os.environ["USE_PHOENIX_PROMPTS"] = "true"
service = DocumentDetectionService()
result = service.detect_relevant_documents("What are working hours?", None)

# Test traditional mode  
os.environ["USE_PHOENIX_PROMPTS"] = "false"
service = DocumentDetectionService()
result = service.detect_relevant_documents("What are working hours?", your_llm)
```

## Installation

To use Phoenix integration, install the required packages:

```bash
pip install openai phoenix-client
```