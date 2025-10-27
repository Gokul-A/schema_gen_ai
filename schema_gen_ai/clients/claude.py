import os
from typing import Optional

from anthropic import Anthropic

def call_llm(prompt: str, api_key: Optional[str] = None, model: Optional[str] = None) -> str:
    if api_key is None:
        api_key = os.getenv('ANTHROPIC_API_KEY')
    if api_key is None:
        raise ValueError("Anthropic API key is required. Set ANTHROPIC_API_KEY environment variable or pass as argument.")
    if model is None:
        model = 'claude-3-5-sonnet-20240620'

    client = Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response.content.strip()