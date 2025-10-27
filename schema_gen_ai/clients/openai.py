import os
from typing import Optional

from openai import OpenAI

def call_llm(prompt: str, api_key: Optional[str] = None, model: Optional[str] = None) -> str:
    if api_key is None:
        api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass as argument.")
    if model is None:
        model = 'gpt-4o'

    client = OpenAI(api_key=api_key)
    
    response = client.responses.create(
        model=model,
        input= prompt,
        temperature=0.5,
    )
    return response.output_text.strip()