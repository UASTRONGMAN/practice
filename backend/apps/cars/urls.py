from django.urls import path

from apps.cars.views import CarAddPhotoView, ListView, RetrieveUpdateDestroyView

urlpatterns = [
    path('', ListView.as_view(), name='list_view'),
    path('/<int:pk>', RetrieveUpdateDestroyView.as_view(), name='retrieve_update_delete'),
    path('/<int:pk>/photos', CarAddPhotoView.as_view(), name='car_add_photo'),
]