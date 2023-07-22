from pyairports.airports import Airports

import json

# city = 'Minsk'
# airports = Airports()
# airport = airports.find(city=city)
# print(airport[0]['iata'])

city = 'Minsk'


def decoding_city_to_iata(city: str) -> str:
    with open('D:\Project_EuzAir/airplane/airports.json', 'r') as f:
        data = json.load(f)

    for airport_code, airport_info in data.items():
        if airport_info['iata'] and airport_info['state'] and airport_info['city'] == city:
            return (airport_info['iata'])


