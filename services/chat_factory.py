from services.openai_service import chat_gpt
from services.anthropic_service import chat_anthropic

def chat_factory(client):
    if (client or '').lower() == 'anthropic':
        return chat_anthropic
    else:
        return chat_gpt
