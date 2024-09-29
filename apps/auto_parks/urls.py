from django.urls import path
from apps.auto_parks.views import AutoParkListCreateApiView, AutoParkAddCarView

urlpatterns = [
    path('', AutoParkListCreateApiView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='add_cars'),
]