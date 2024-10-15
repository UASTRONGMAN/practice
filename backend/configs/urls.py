from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from apps.auth import urls as auth
from apps.auto_parks import urls as auto_park
from apps.cars import urls as cars
from apps.users import urls as users

schema_view = get_schema_view(
      openapi.Info(
         title="Auto parks",
         default_version='v1',
         description="Auto parks api",
         contact=openapi.Contact(email="contact@snippets.local"),
      ),
      public=True,
      permission_classes=(AllowAny,),
   )

urlpatterns = [
    path('api/cars', include(cars)),
    path('api/auto_parks', include(auto_park)),
    path('api/users', include(users)),
    path('api/auth', include(auth)),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)