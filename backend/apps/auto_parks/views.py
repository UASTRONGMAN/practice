from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParksModelSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateApiView(ListCreateAPIView):
    """
    get:
        Show all auto parks
    post:
        Create a new auto park
    """
    serializer_class = AutoParksModelSerializer
    queryset = AutoParkModel.objects.all()

class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        """
            Add car to the auto park
        """
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)
        parks_model_serializer = AutoParksModelSerializer(auto_park)
        return Response(parks_model_serializer.data, status=status.HTTP_201_CREATED)