from django.urls import path, include
from apps.cars import urls
from apps.auto_parks import urls as auto_park

urlpatterns = [
    path('cars', include(urls)),
    path('auto_parks', include(auto_park)),
]
