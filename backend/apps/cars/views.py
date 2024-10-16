from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer

#
# class ListView(GenericAPIView):
#     def get(self, *args, **kwargs):
#         cars = CarModel.objects.all()
#         # cars = cars.filter(price__gt=5000)
#         # cars = cars.filter(price__lt=5000)
#         # cars = cars.filter(price__gte=5000)
#         # cars = cars.filter(price__lte=5000)
#         # cars = cars.filter(year__gt=2014)
#         # cars = cars.filter(year__lt=2014)
#         # cars = cars.filter(year__gte=2014)
#         # cars = cars.filter(year__lte=2014)
#         # cars = cars.filter(model__startswith='A')
#         # cars = cars.filter(model__endswith='I')
#         # cars = cars.filter(model__contains='UD')
#         # cars = cars.order_by('price')
#         # cars = cars.order_by('-year')
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class CarListView(ListAPIView):
    """
        Show all cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    pagination_class = None
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated,)



class CarRetrieveUpdateDestroyView(GenericAPIView):
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        """
            Get car by id
        """
        car = self.get_object()
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        """
            Full update car by id
        """
        data = self.request.data
        car = self.get_object()
        serializer = CarSerializer(car, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        """
            Partial update car by id
        """
        data = self.request.data
        car = self.get_object()
        serializer = CarSerializer(car, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        """
            Delete car by id
        """
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CarAddPhotoView(GenericAPIView):
    """
        Add photos to car by id
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()

    def put(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for index in files:
            serializer = CarPhotoSerializer(data={'photo': files[index]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data, status=status.HTTP_200_OK)
