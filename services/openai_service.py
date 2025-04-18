import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_gpt(message):
    model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
    response = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content
