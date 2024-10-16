from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, serializers
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]

class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={status.HTTP_201_CREATED: AutoParksModelSerializer()})
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