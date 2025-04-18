from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def get_home():
    try:
        return jsonify({
            'message': 'Things are working. Check out the readme.md for more information.',
            'status': 'success'
        }), 200
    except Exception as error:
        return jsonify({'error': str(error)}), 500
