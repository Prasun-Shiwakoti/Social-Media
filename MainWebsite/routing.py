from django.urls import re_path, path

from . import Consumers

websocket_urlpatterns = [
    path("ws/messages/<str:un>/", Consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/messages/(?P<room_name>)/$', Consumers.ChatConsumer.as_asgi()),
]