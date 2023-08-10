from django.db import transaction

from rest_framework import viewsets, mixins
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status

from booking.models import Users, Routes, Temporary, Seats, Orders, Passports, Aircrafts
from booking_api.serializers import UsersSerializer, RouteSerializer, TemporarySerializer, \
    RouteDetailSerializer, TemporaryAllSerializer, AircraftSerializer, AirlineSerializer, \
    RouteSerializer, SeatsSerializer, PassportSerializer, PersonalAccountSerializer, OrderSerializer
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
    queryset = Routes.objects.all()
    serializer_class = RouteSerializer

    @transaction.atomic
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
        if not data_all.get('city_arrival'):
            raise APIException(detail="There's no such route :)")
        return Response(data=data_all, status=status.HTTP_200_OK)

    @transaction.atomic
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


class PassportAPIAllViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Passports.objects.all()
    serializer_class = PassportSerializer


class PersonalAccountViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    queryset = Users.objects.all()
    serializer_class = PersonalAccountSerializer