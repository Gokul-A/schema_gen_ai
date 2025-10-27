from typing import Optional

def generate_schema(
    description: str,
    provider: str,
    api_key: Optional[str] = None,
    model: Optional[str] = None
) -> str:
    """
    Generate a Pydantic schema using the specified LLM provider.

    :param description: The description of what to extract.
    :param provider: The LLM provider ('openai', 'claude', 'gemini').
    :param api_key: Optional API key; falls back to environment variable.
    :param model: Optional model name; uses default if not provided.
    :return: The generated Pydantic schema as a string (Python code).
    """
    prompt = f"""Create a Pydantic response schema using BaseModel for extracting the following information from text or LLM output. 
    The schema should define fields for the key elements based on this description: {description}.

    Important:
    - Import from pydantic import BaseModel
    - Define a class that inherits from BaseModel
    - Use appropriate types (str, int, list, etc.)
    - Add field descriptions if helpful
    - Output ONLY the Python code, no explanations or additional text.
    """

    if provider == 'openai':
        from .clients.openai import call_llm
    elif provider == 'claude':
        from .clients.claude import call_llm
    elif provider == 'gemini':
        from .clients.gemini import call_llm
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    response = call_llm(prompt, api_key, model)
    return response