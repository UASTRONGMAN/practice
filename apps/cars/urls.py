from django.urls import path
from apps.cars.views import ListCreateView, RetrieveUpdateDestroyView

urlpatterns = [
    path('', ListCreateView.as_view(), name='list_create'),
    path('/<int:pk>', RetrieveUpdateDestroyView.as_view(), name='retrieve_update_delete'),
]