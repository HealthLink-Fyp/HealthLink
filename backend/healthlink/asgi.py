import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "healthlink.settings.local")
django.setup()

from django.core.asgi import get_asgi_application  # noqa: E402
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa: E402
from channels.security.websocket import AllowedHostsOriginValidator  # noqa: E402
from chat.middleware import JwtAuthMiddleware  # noqa: E402
from chat.routing import websocket_urlpatterns  # noqa: E402

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            JwtAuthMiddleware(URLRouter(websocket_urlpatterns))
        ),
    }
)
