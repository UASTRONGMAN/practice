from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class ListCreateView(GenericAPIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        # cars = cars.filter(price__gt=5000)
        # cars = cars.filter(price__lt=5000)
        # cars = cars.filter(price__gte=5000)
        # cars = cars.filter(price__lte=5000)
        # cars = cars.filter(year__gt=2014)
        # cars = cars.filter(year__lt=2014)
        # cars = cars.filter(year__gte=2014)
        # cars = cars.filter(year__lte=2014)
        # cars = cars.filter(model__startswith='A')
        # cars = cars.filter(model__endswith='I')
        # cars = cars.filter(model__contains='UD')
        # cars = cars.order_by('price')
        # cars = cars.order_by('-year')
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyView(GenericAPIView):
    queryset = CarModel.objects.all()

    def get(self, *args, **kwargs):
        car = self.get_object()
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        car = self.get_object()
        serializer = CarSerializer(car, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        car = self.get_object()
        serializer = CarSerializer(car, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)