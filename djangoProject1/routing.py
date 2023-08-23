from channels.routing import ProtocolTypeRouter
from randNum.routing import websockets

application = ProtocolTypeRouter({"websocket": websockets})
