from typing import Dict, Any
import json

from rest_framework import serializers

from booking.models import Users, Routes, Temporary


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'

    def create(self, validated_data):
        instance = Routes.objects.create(**validated_data)
        return instance


class TemporarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporary
        fields = '__all__'

    def create(self, validated_data):
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

        instance = Temporary.objects.create(**validated_data)
        return instance

