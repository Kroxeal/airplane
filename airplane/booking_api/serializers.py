from django.db import transaction
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from booking.models import Users, Routes, Temporary, Aircrafts, Seats, Orders, Passports, Airlines
from booking_api.services import TemporaryService, CurrentUser


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class TemporarySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Temporary
        fields = [
            'id',
            'iata_departure',
            'iata_arrival',
            'date_departure',
            'user',
        ]

    def get_user(self, obj):
        return obj.user.username if obj.user else None

    def create(self, validated_data):
        validated_data = TemporaryService.parsing_json_bd(validated_data)

        CurrentUser.set_current_user(self, validated_data)

        instance = Temporary.objects.create(**validated_data)
        return instance


class RouteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'

    def create(self, validated_data):
        instance = Routes.objects.create(**validated_data)
        return instance


class TemporaryAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporary
        fields = '__all__'


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircrafts
        fields = '__all__'

    def create(self, validated_data):
        return Aircrafts.objects.create(**validated_data)


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Orders
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username if obj.user else None


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passports
        fields = '__all__'

    def get_passport(self, obj):
        return obj.passport.passport_number if obj.passport else None


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = '__all__'

    def create(self, validated_data):
        return Airlines.objects.create(**validated_data)


class UsersNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'name',
        ]


class RouteSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer()
    airline = AirlineSerializer()
    user = serializers.SerializerMethodField()
    temporary = serializers.SerializerMethodField()

    class Meta:
        model = Routes
        fields = [
            'id',
            'aircraft',
            'airline',
            'country_departure',
            'country_arrival',
            'city_departure',
            'city_arrival',
            'date_arrival',
            'price',
            'temporary',
            'user',
        ]

    def get_user(self, obj):
        return obj.user.name if obj.user else None

    def get_temporary(self, obj):
        return obj.temporary.iata_arrival if obj.temporary else None

    @transaction.atomic
    def create(self, validated_data):
        aircraft_data = validated_data.pop('aircraft')
        airline_data = validated_data.pop('airline')

        current_user = self.context['request'].user
        user_instance = Users.objects.get(id=current_user.id)
        validated_data['user'] = user_instance

        temporary_instance = Temporary.objects.filter(user_id=current_user.id)
        if temporary_instance:
            validated_data['temporary'] = temporary_instance[::-1][0]

        aircraft_instance, created_aircraft = Aircrafts.objects.get_or_create(**aircraft_data)
        airline_instance, created_airline = Airlines.objects.get_or_create(**airline_data)

        route_instance = Routes.objects.create(
            aircraft=aircraft_instance,
            airline=airline_instance,
            **validated_data,
        )
        return route_instance


class SeatsSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    aircraft = serializers.SerializerMethodField()

    class Meta:
        model = Seats
        fields = [
            'id',
            'seat_number',
            'order',
            'aircraft',
        ]

    def get_order(self, obj):
        return obj.order.date if obj.order else None

    def get_aircraft(self, obj):
        return obj.aircraft.name if obj.aircraft else None

    def get_user(self, obj):
        return obj.user.username if obj.user else None

    @transaction.atomic
    def create(self, validated_data):
        order_data = validated_data.pop('order')

        current_user = self.context['request'].user
        user_instance = Users.objects.get(id=current_user.id)
        validated_data['user'] = user_instance
        order_data['user_id'] = current_user.id

        temporary_instance = Temporary.objects.filter(user_id=current_user.id)
        last_temporary = temporary_instance[::-1][0]
        routes_instanse = Routes.objects.get(temporary_id=last_temporary.id)
        aircraft_instanse = Aircrafts.objects.get(id=routes_instanse.aircraft_id)

        order_data['total_amount'] = routes_instanse.price

        order_instance = Orders.objects.create(**order_data)

        seats_instance = Seats.objects.create(
            order=order_instance,
            seat_number=validated_data['seat_number'],
            aircraft=aircraft_instanse,
        )
        return seats_instance


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Users


class PersonalAccountSerializer(serializers.ModelSerializer):
    passport = PassportSerializer()

    class Meta:
        model = Users
        fields = [
            'id',
            'name',
            'surname',
            'phone',
            'passport',
        ]

    @transaction.atomic
    def update(self, instance, validated_data):
        passport_data = validated_data.pop('passport')

        passport_instance, created_passport = Passports.objects.update_or_create(**passport_data)
        passport_instance.passport_number = validated_data.get('passport_number', passport_instance.passport_number)
        passport_instance.nationality = validated_data.get('nationality', passport_instance.nationality)
        passport_instance.sex = validated_data.get('sex', passport_instance.sex)
        passport_instance.date_of_birth = validated_data.get('date_of_birth', passport_instance.date_of_birth)
        passport_instance.date_of_issue = validated_data.get('date_of_issue', passport_instance.date_of_issue)
        passport_instance.date_of_expire = validated_data.get('date_of_expire', passport_instance.date_of_expire)
        passport_instance.photo = validated_data.get('photo', passport_instance.photo)
        passport_instance.save()

        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.passport_id = passport_instance.id
        instance.save()

        return instance


