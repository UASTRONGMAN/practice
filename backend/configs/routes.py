from django.urls import path
from channels.routing import URLRouter
from apps.chat.routes import websocket_urlpatterns as chat_routing
from apps.cars.routes import websocket_urlpatterns as cars_routing

websocket_urlpatterns = [
    path('api/chat/', URLRouter(chat_routing)),
    path('api/cars/', URLRouter(cars_routing)),
]