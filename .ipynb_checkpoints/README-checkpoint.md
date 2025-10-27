# LLM Schema Generator

A Python library that generates Pydantic response schemas based on user descriptions using various LLM providers (OpenAI, Anthropic Claude, Google Gemini).

## Installation

Install from PyPI:

pip install llm-schema-generator


# Example: Using OpenAI

from llm_schema_generator import generate_schema

schema_code = generate_schema(
    description="Extract name, age, and occupation from a person's bio",
    provider="openai",
    api_key="your_openai_api_key",  # Or set OPENAI_API_KEY env var
    model="gpt-4o-mini"  # Optional
)

print(schema_code)


# Example: Using gemini

from llm_schema_generator import generate_schema

schema_code = generate_schema(
    description="Extract name, age, and occupation from a person's bio",
    provider="gemini",
    api_key="your_gemini_api_key",  # Or set GOOGLE_API_KEY env var
    model="gemini-2.5-flash"  # Optional
)

print(schema_code)


# Example: Using OpenAI

from llm_schema_generator import generate_schema

schema_code = generate_schema(
    description="Extract name, age, and occupation from a person's bio",
    provider="claude",
    api_key="your_claude_api_key",  # Or set ANTHROPIC_API_KEY env var
    model="claude-sonnet-4-5-20250929"  # Optional
)

print(schema_code)