from django.urls import path, include
from apps.cars import urls

urlpatterns = [
    path('cars', include(urls)),
]
