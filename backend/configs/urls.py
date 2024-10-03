from django.urls import include, path

from apps.auto_parks import urls as auto_park
from apps.cars import urls as cars
from apps.users import urls as users

urlpatterns = [
    path('cars', include(cars)),
    path('auto_parks', include(auto_park)),
    path('users', include(users)),
]
