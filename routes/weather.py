from flask import Blueprint, jsonify, request
from services.weather_service import query_weather
from services.chat_factory import chat_factory

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/what-to-wear', methods=['GET'])
def what_to_wear():
    client = request.args.get('client')
    zip_code = request.args.get('zip')

    if not zip_code:
        return jsonify({'error': 'Zip code parameter `zip` is required'}), 400

    weather_details = query_weather(zip_code)
    message = (
        f"The weather forecast for today for zip code {zip_code} "
        f"is that it will be {weather_details['summary']} "
        f"with a high of {weather_details['maxTemp']} and a low of {weather_details['minTemp']}. "
        f"The wind will be {weather_details['maxWind']}. "
        f"It will {'rain' if weather_details['willRain'] else 'not rain'} and "
        f"{'snow' if weather_details['willSnow'] else 'not snow'}. "
        "Please suggest what kind of clothes I should wear today—don't mention shoes. "
        "Be brief, using 75 words or less. Include the day's high."
    )

    chat_client = chat_factory(client)
    if not chat_client:
        return jsonify({'error': 'Invalid or missing chat client'}), 400
    try:
        response = chat_client(message)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(response)
