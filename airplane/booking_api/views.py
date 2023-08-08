from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import F
from django.urls import reverse

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
import requests.exceptions
import requests
import os

from rest_framework.views import APIView

from booking.models import Users, Routes, Temporary, Seats
from booking_api.serializers import UsersSerializer, RouteSerializer, TemporarySerializer, \
    RouteDetailSerializer, TemporaryAllSerializer, AircraftSerializer, AirlineSerializer, \
    RouteSerializer, SeatsSerializer
from booking_api.logic import decoding_city_to_iata
from booking_api.services import TemporaryService


class AllUsersAPIView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class RoutesViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    # permission_classes = [
    #     IsAdminUser,
    # ]
    # queryset = Temporary.objects.all()
    # serializer_class = TemporaryAllSerializer
    queryset = Routes.objects.all()
    serializer_class = RouteSerializer

    # def get_serializer_class(self):
    #     if self.request.method == 'get':
    #         return TemporaryAllSerializer
    #     else:
    #         return RouteDetailSerializer
    #
    # @action(detail=True, methods=['get'])
    # def save_data_to_db(self, request, pk=None) -> Response:
    #     instance = Temporary.objects.get(id=pk)
    #
    #     data_all = TemporaryService.response_from_api(instance=instance)
    #     print(data_all)
    #
    #     return Response(data=data_all, status=status.HTTP_200_OK)

        # if request.method == 'get':
        #     return Response(data=data_all, status=status.HTTP_200_OK)
        # elif request.method == 'post':
        #     serializer = self.get_serializer(data=data_all)
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save()
        #     return Response({'message': 'Данные успешно сохранены.'}, status=status.HTTP_201_CREATED)
        # else:
        #     return Response({'message': 'Метод не поддерживается.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        data = request.data

        aircraft_serializer = AircraftSerializer(data=data)
        airline_serializer = AirlineSerializer(data=data)
        route_serializer = RouteSerializer(data=data)

        if all([aircraft_serializer.is_valid(), airline_serializer.is_valid(), route_serializer.is_valid()]):
            aircraft_instance = aircraft_serializer.save()
            airline_instance = airline_serializer.save()
            route_instance = route_serializer.save()
            return Response({
                'aircraft': AircraftSerializer(aircraft_instance).data,
                'airline': AirlineSerializer(airline_instance).data,
                'route': RouteSerializer(route_instance).data,
            }, status=status.HTTP_201_CREATED)
        return Response({
            'aircraft_errors': aircraft_serializer.errors,
            'airline_errors': airline_serializer.errors,
            'route_errors': route_serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class TemporaryViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Temporary.objects.all()
    serializer_class = TemporarySerializer


class RoutesDetailViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Routes.objects.all()
    serializer_class = RouteSerializer


class SeatsViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer


class TemporaryAPIViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Routes.objects.all()
    serializer_class = RouteSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Temporary.objects.get(id=pk)
        data_all = TemporaryService.response_from_api(instance=instance)
        return Response(data=data_all, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data

        aircraft_serializer = AircraftSerializer(data=data)
        airline_serializer = AirlineSerializer(data=data)
        route_serializer = RouteSerializer(data=data)

        if all([aircraft_serializer.is_valid(), airline_serializer.is_valid(), route_serializer.is_valid()]):
            aircraft_instance = aircraft_serializer.save()
            airline_instance = airline_serializer.save()
            route_instance = route_serializer.save()
            return Response({
                'aircraft': AircraftSerializer(aircraft_instance).data,
                'airline': AirlineSerializer(airline_instance).data,
                'route': RouteSerializer(route_instance).data,
            }, status=status.HTTP_201_CREATED)
        return Response({
            'aircraft_errors': aircraft_serializer.errors,
            'airline_errors': airline_serializer.errors,
            'route_errors': route_serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class TemporaryAPIAllViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Temporary.objects.all()
    serializer_class = TemporaryAllSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Temporary.objects.get(id=pk)
        data = TemporaryService.response_from_api_all_data(instance=instance)
        return Response(data=data, status=status.HTTP_200_OK)






