from django.urls import path
from channels.routing import URLRouter
from . import consumers


websockets = URLRouter([
    path(
        'ws', consumers.ChatConsumer.as_asgi(),
    ),
])
