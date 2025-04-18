import anthropic
import os

def chat_anthropic(message, max_tokens=1024):
    """
    Sends a message to the Anthropic API and returns the response content.
    Args:
        message (str): The user's message.
        model (str, optional): The model to use. Defaults to env or 'claude-3-5-haiku-20241022'.
        max_tokens (int, optional): Max tokens for the response. Defaults to 1024.
    Returns:
        str: The response content from Anthropic.
    Raises:
        Exception: If API key is missing or API call fails.
    """

    api_key = os.getenv('ANTHROPIC_API_KEY')
    model = os.getenv('ANTHROPIC_MODEL', 'claude-3-5-haiku-20241022')

    if not api_key:
        raise Exception("API key not found. Please set the ANTHROPIC_API_KEY environment variable.")

    if not message or not isinstance(message, str):
        raise ValueError("Message must be a non-empty string.")

    try:
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[{'role': 'user', 'content': message}],
        )

        return response.content[0].text
    except Exception as error:
        print(f'Error communicating with Anthropic API: {error}')
        raise
