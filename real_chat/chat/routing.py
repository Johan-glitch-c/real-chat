from django.urls import path
from .consumers import ChatCosumer


websocket_urlpatterns = [
    path('ws/chat/', ChatCosumer.as_asgi())
]