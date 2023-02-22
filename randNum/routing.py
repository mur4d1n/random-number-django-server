from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.generic.websocket import AsyncWebsocketConsumer


websockets = URLRouter([
    path(
        'ws', AsyncWebsocketConsumer.as_asgi(),
        name="num-listener",
    ),
])
