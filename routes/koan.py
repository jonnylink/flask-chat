from flask import Blueprint, jsonify, request
from services.chat_factory import chat_factory

koan_bp = Blueprint('koan', __name__)

@koan_bp.route('/koan', methods=['GET'])
def koan():
    try:
        client = request.args.get('client')
        message = 'Tell me another zen koan. Do not include any additional commentary.'
        chat_client = chat_factory(client)
        response = chat_client(message)

        return jsonify(response)
    except Exception as error:
        print(f'Error interacting with API: {error}')
        return jsonify({'error': 'Failed to fetch response.'}), 500
