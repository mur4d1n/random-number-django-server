from channels.routing import ProtocolTypeRouter, URLRouter
from randNum.routing import websockets
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(websockets)
        )
    )
})
