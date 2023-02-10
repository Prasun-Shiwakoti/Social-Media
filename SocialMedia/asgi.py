"""
ASGI config for SocialMedia project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import MainWebsite.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialMedia.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            MainWebsite.routing.websocket_urlpatterns
        )
    ),
})

