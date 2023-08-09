from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from booking.models import Users, Routes, Aircrafts, Airlines, Temporary


class PersonalAccountViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "name": "Denis",
            "surname": "Klimkov",
            "phone": "+375444567849",
            "passport": {
                "passport_number": "AB9537515",
                "nationality": "USA",
                "sex": "male",
                "date_of_birth": "1990-01-01",
                "date_of_issue": "2020-01-01",
                "date_of_expire": "2030-01-01",
                "photo": None
            }
        }

    def test_retrieve_user(self):
        user = Users.objects.create(name='Denis', surname='Klimkov', phone='+375444567849')
        response = self.client.get(f'/booking_api/account/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Denis')

    def test_update_user(self):
        user = Users.objects.create(name='Denis', surname='Klimkov', phone='+375444567849')
        updated_data = {
            "name": "Denis",
            "surname": "Klimkov",
            "phone": "+375444561777",
            "passport": {
                "passport_number": "AB1234567",
                "nationality": "Belarus",
                "sex": "female",
                "date_of_birth": "1992-01-01",
                "date_of_issue": "2022-01-01",
                "date_of_expire": "2032-01-01",
                "photo": None
            }
        }
        response = self.client.patch(f'/booking_api/account/{user.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Denis')
        self.assertEqual(response.data['phone'], '+375444561777')
        self.assertEqual(response.data['passport']['passport_number'], 'AB1234567')

    def test_list_users(self):
        first_data = {
            "username": "den",
            "name": "Denis",
            "surname": "Klimkov",
            "phone": "+375444561777",

        }
        second_data = {
            "username": "joe",
            "name": "Joe",
            "surname": "Klimkov",
            "phone": "+375444561777",
            }
        Users.objects.create(**first_data)
        Users.objects.create(**second_data)
        response = self.client.get('/booking_api/account/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class RoutesViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Users.objects.create(username='testuser', name='Test', surname='User', phone='+123456789')
        self.temporary_data = {
            "iata_departure": "MSQ",
            "iata_arrival": "WSD",
            "date_departure": "2023-07-22",
            "user": self.user,
        }
        self.temporary = Temporary.objects.create(**self.temporary_data)

    def test_create_route(self):
        aircraft_data = {
            "name": "Boeing 717",
            "iata_aircraft": "733",
            "amount": 106
        }
        airline_data = {
            "name": "Belavia",
            "iata_airline": "B2"
        }
        route_data = {
            "aircraft": aircraft_data,
            "airline": airline_data,
            "temporary": self.temporary.id,
            "country_departure": "Belarus",
            "country_arrival": "Poland",
            "city_departure": "MSQ",
            "city_arrival": "Wroclaw",
            "date_arrival": "2023-07-23",
            "price": "953.00",
        }
        self.client.force_authenticate(self.user)
        response = self.client.post('/booking_api/routes_detail/', route_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Routes.objects.count(), 1)
        self.assertEqual(Aircrafts.objects.count(), 1)
        self.assertEqual(Airlines.objects.count(), 1)

        route_instance = Routes.objects.first()
        aircraft_instance = Aircrafts.objects.first()
        airline_instance = Airlines.objects.first()

        self.assertEqual(route_instance.aircraft, aircraft_instance)
        self.assertEqual(route_instance.airline, airline_instance)
        self.assertEqual(route_instance.country_departure, "Belarus")
        self.assertEqual(route_instance.country_arrival, "Poland")
        self.assertEqual(route_instance.city_departure, "MSQ")
        self.assertEqual(route_instance.city_arrival, "Wroclaw")
        self.assertEqual(route_instance.date_arrival.strftime("%Y-%m-%d"), "2023-07-23")
        self.assertEqual(str(route_instance.price), "953.00")

    def tearDown(self):
        self.user.delete()
