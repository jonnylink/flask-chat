from flask import Blueprint, jsonify, request
from services.chat_factory import chat_factory

magic_bp = Blueprint('magic', __name__)

@magic_bp.route('/magic', methods=['GET'])
def magic():
    try:
        client = request.args.get('client')
        message = 'Write a short piece of magical realism that is 200 words or less.'
        chat_client = chat_factory(client)
        response = chat_client(message)

        return jsonify(response)
    except Exception as error:
        print(f'Error interacting with API: {error}')
    return jsonify({'error': 'Failed to fetch response.'}), 500
