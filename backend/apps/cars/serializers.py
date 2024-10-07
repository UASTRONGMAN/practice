from rest_framework import serializers

from apps.cars.models import CarModel, CarPhotoModel


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo',)
        extra_kwargs = {
            'photo': {
                'required': True
            }
        }


class CarSerializer(serializers.ModelSerializer):
    photos = CarPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'body_type' , 'price', 'year', 'photos', 'created_at', 'updated_at')
