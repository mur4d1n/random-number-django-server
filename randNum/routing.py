from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.generic.websocket import AsyncWebsocketConsumer
from . import consumers


websockets = URLRouter([
    path(
        'ws', consumers.ChatConsumer.as_asgi(),
    ),
])
