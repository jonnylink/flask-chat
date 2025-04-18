from flask import Blueprint, request, jsonify
from services.chat_factory import chat_factory

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message') if data else None
        client = request.args.get('client')

        if not message:
            return 'Message `message` is required in the POST body', 400

        chat_client = chat_factory(client)
        response = chat_client(message)

        return jsonify(response)
    except Exception as error:
        print('Error interacting with API:', str(error))
        return jsonify({'error': 'Failed to fetch response.'}), 500
