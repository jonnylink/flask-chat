# Chat Wrapper
A super simple Python Flask server wrapper for OpenAI's ChatGPT and Anthropic's Claude APIs for Fun™

By default, ChatGPT is used.

## Setup
1. Clone the repository.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file by copying the `.env.example` file and updating the values.
5. Run the Flask server:
   ```bash
   python app.py
   ```

## Requirements
1. ChatGPT API key
2. Anthropic API key (if using the Anthropic client)
3. Weather.com API key (if using the /what-to-wear route)

## Routes
To use Anthropic's Claude, add a query param `?client=anthropic`

### health
To see if the server is running as expected:
Send a GET request to `/health`

### Generic chat
To write open-ended prompts:
Send a POST request to `/chat` with a JSON body:
```json
{"message": "Tell me a funny joke."}
```

### What to wear
To get advice on what to wear today:
Send a GET request to `/what-to-wear?zip=YOUR-ZIP-CODE`

### Zen koan
To get a zen koan:
Send a GET request to `/koan`

### Magical realism
To read a short piece of sort of ok magical realism:
Send a GET request to `/magic`
