import os
import requests

def query_weather(zip_code):
    api_key = os.getenv('WEATHER_API_KEY')

    if not api_key:
       raise Exception("API key not found. Please set the WEATHER_API_KEY environment variable.")

    try:
        response = requests.get(
            'https://api.weatherapi.com/v1/forecast.json',
            params={
                'key': api_key,
                'q': zip_code,
                'days': 1,
                'aqi': 'no',
                'alerts': 'no',
            }
        )
        response.raise_for_status()
        data = response.json()
        day = data['forecast']['forecastday'][0]['day']

        return {
            'minTemp': f"{day['mintemp_f']}\u00b0 F",
            'maxTemp': f"{day['maxtemp_f']}\u00b0 F",
            'maxWind': f"{day['maxwind_mph']}mph",
            'summary': day['condition']['text'],
            'willRain': bool(day.get('daily_will_it_rain', 0)),
            'willSnow': bool(day.get('daily_will_it_snow', 0)),
        }
    except Exception as e:
        print(f'Error fetching weather data: {e}')
        raise
