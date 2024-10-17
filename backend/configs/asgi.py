import os
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

from configs.routes import websocket_urlpatterns
from core_app.middleware.auth_socket_middleware import AuthSocketMiddleware
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthSocketMiddleware(URLRouter(websocket_urlpatterns))
})