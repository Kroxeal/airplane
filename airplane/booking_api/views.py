from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import requests.exceptions
import requests
import os

from booking.models import Users, Routes, Temporary
from booking_api.serializers import UsersSerializer, RoutesSerializer, TemporarySerializer
from booking_api.logic import decoding_city_to_iata


class AllUsersAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class RoutesAPIViewController(
    generics.ListAPIView,
    generics.CreateAPIView,
):
    serializer_class = RoutesSerializer



    def get(self, request):
        iata_departure = Temporary.objects.all()
        status_arrival_departure = 'dep'
        year = '2023'
        month = '07'
        day = '20'
        screen_hours = '12'
        try:
            response = requests.get(
                url=f"{os.environ.get('url_road')}/{iata_departure}/{status_arrival_departure}/{year}/{month}/{day}/{screen_hours}",
                params={
                    'appKey': settings.API_KEY,
                    'appId': settings.API_ID,
                })
            data = response.json()
            return Response(data)
        except requests.exceptions.RequestException as e:
            return HttpResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TemporaryAPIViewController(
    generics.ListAPIView,
    generics.CreateAPIView,
):
    serializer_class = TemporarySerializer

    def get_queryset(self):
        return Temporary.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = TemporarySerializer(queryset, many=True)
        return Response(serializer.data)

