from schema_gen_ai import generate_schema

def test_all_providers():
    description = "Extract name, age, and phone number from a person's bio there can be multiple phone numbers so add them in a list format."
    providers = ["openai", "claude", "gemini"]
    # providers = ["openai"]

    api_keys = {
        "openai": "open_ai_key",
        "claude": "your_claude_api_key",
        "gemini": "your_gemini_api_key"
    }

    for provider in providers:
        print(f"\nTesting provider: {provider}")
        try:
            schema_code = generate_schema(
                description=description,
                provider=provider,
                api_key=api_keys.get(provider),
            )
            print(f"Generated schema for {provider}:\n{schema_code}")
        except Exception as e:
            print(f"Error with {provider}: {str(e)}")

if __name__ == "__main__":
    test_all_providers()