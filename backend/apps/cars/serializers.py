from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'body_type' , 'price', 'year', 'created_at', 'updated_at')
