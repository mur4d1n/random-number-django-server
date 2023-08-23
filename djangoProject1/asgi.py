import os

import django
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from randNum import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject1.settings")

django.setup()

application = ProtocolTypeRouter(
    {"http": get_asgi_application(), "websocket": routing.websockets},
)
