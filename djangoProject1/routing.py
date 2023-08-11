from channels.routing import ProtocolTypeRouter, URLRouter
from randNum.routing import websockets

application = ProtocolTypeRouter({
    "websocket": websockets
})
