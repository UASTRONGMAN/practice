from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from apps.auth import urls as auth
from apps.auto_parks import urls as auto_park
from apps.cars import urls as cars
from apps.users import urls as users

urlpatterns = [
    path('cars', include(cars)),
    path('auto_parks', include(auto_park)),
    path('users', include(users)),
    path('auth', include(auth)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)