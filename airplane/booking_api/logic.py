import os
import json

city = 'Minsk'


def decoding_city_to_iata(city: str) -> str:
    with open(os.environ.get('airports_file'), 'r') as f:
        data = json.load(f)

    for airport_code, airport_info in data.items():
        if airport_info['iata'] and airport_info['state'] and airport_info['city'] == city:
            return (airport_info['iata'])


