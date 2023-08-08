import requests
import json

from airplane import settings
from booking.models import Users


class TemporaryService:

    @staticmethod
    def response_from_api(instance):
        year = instance.date_departure.year
        month = instance.date_departure.month
        day = instance.date_departure.day
        iata_departure = instance.iata_departure
        iata_arrival = instance.iata_arrival

        response = requests.get(
            # url=f"{os.environ.get('url_road')}/{iata_departure}/{iata_arrival}/{status_arrival_departure}/{year}/{month}/{day}",
            # url=f"{https://api.flightstats.com /flex/schedules/rest/v1/{format}/from/{departureAirportCode}/to/{arrivalAirportCode}/departing/{год}/{месяц}/{день}",
            # url=f'https://api.flightstats.com/flex/schedules/rest/v1/json/from/{iata_departure}/to/{iata_arrival}/departing/{year}/{month}/{day}',
            url=f'https://api.flightstats.com/flex/flightstatus/rest/v2/json/airport/status/{iata_departure}/dep/{year}/{month}/{day}/12',
            params={
                'appKey': settings.API_KEY,
                'appId': settings.API_ID,
            })
        data = response.json()

        data_all = dict()
        flight_statuses = data['flightStatuses']
        airplane = ''
        airlinestr = ''
        for flight_status in flight_statuses:
            if flight_status['departureAirportFsCode'] == iata_departure and \
                    flight_status['arrivalAirportFsCode'] == iata_arrival:
                data_all['dateUtc_departure'] = flight_status['departureDate']['dateUtc']
                data_all['dateUtc_arrival'] = flight_status['arrivalDate']['dateUtc']
                data_all['date_arrival'] = flight_status['arrivalDate']['dateUtc'][:10]
                airplane += flight_status['flightEquipment']['scheduledEquipmentIataCode']
                airlinestr += flight_status['carrierFsCode']

        airports = data['appendix']['airports']

        for airport in airports:
            if airport['iata'] == iata_departure:
                data_all['airport_departure'] = airport['name']
                data_all['country_departure'] = airport['countryName']
                data_all['city_departure'] = airport['city']
            if airport['iata'] == iata_arrival:
                data_all['airport_arrival'] = airport['name']
                data_all['country_arrival'] = airport['countryName']
                data_all['city_arrival'] = airport['city']

        equipments = data['appendix']['equipments']

        for equipment in equipments:
            if equipment['iata'] == airplane:
                data_all['aircraft'] = equipment['name']
                data_all['iata_aircraft'] = equipment['iata']

        airlines = data['appendix']['airlines']

        for airline in airlines:
            if airline['iata'] == airlinestr:
                data_all['airlines'] = airline['name']
                data_all['iata_airline'] = airline['iata']

        return data_all

    @staticmethod
    def response_from_api_all_data(instance):
        year = instance.date_departure.year
        month = instance.date_departure.month
        day = instance.date_departure.day
        iata_departure = instance.iata_departure
        iata_arrival = instance.iata_arrival

        response = requests.get(
            # url=f"{os.environ.get('url_road')}/{iata_departure}/{iata_arrival}/{status_arrival_departure}/{year}/{month}/{day}",
            # url=f"{https://api.flightstats.com /flex/schedules/rest/v1/{format}/from/{departureAirportCode}/to/{arrivalAirportCode}/departing/{год}/{месяц}/{день}",
            # url=f'https://api.flightstats.com/flex/schedules/rest/v1/json/from/{iata_departure}/to/{iata_arrival}/departing/{year}/{month}/{day}',
            url=f'https://api.flightstats.com/flex/flightstatus/rest/v2/json/airport/status/{iata_departure}/dep/{year}/{month}/{day}/12',
            params={
                'appKey': settings.API_KEY,
                'appId': settings.API_ID,
            })
        data = response.json()
        return data

    @staticmethod
    def parsing_json_bd(validated_data):
        with open('D:\Project_EuzAir/airplane/airports.json', 'r') as f:
            data = json.load(f)

        for airport_code, airport_info in data.items():
            if airport_info['iata'] and airport_info['state'] and airport_info['city'] == validated_data.get(
                'iata_departure',
            ):
                validated_data['iata_departure'] = airport_info['iata']
            if airport_info['iata'] and airport_info['state'] and airport_info['city'] == validated_data.get(
                    'iata_arrival',
            ):
                validated_data['iata_arrival'] = airport_info['iata']
        return validated_data


class CurrentUser:
    @staticmethod
    def set_current_user(self, validated_data):
        current_user = self.context['request'].user
        user_instance = Users.objects.get(id=current_user.id)
        validated_data['user'] = user_instance
        return validated_data



