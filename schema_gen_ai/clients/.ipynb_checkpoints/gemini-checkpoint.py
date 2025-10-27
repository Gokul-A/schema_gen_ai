import os
from typing import Optional

from google import genai

def call_llm(prompt: str, api_key: Optional[str] = None, model: Optional[str] = None) -> str:
    if api_key is None:
        api_key = os.getenv('GOOGLE_API_KEY')
    if api_key is None:
        raise ValueError("Google API key is required. Set GOOGLE_API_KEY environment variable or pass as argument.")
    if model is None:
        model = 'gemini-2.0-flash-001'

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model, 
        contents=prompt,
    )
    return response.text.strip()

