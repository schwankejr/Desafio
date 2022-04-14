from importlib.resources import path

from django.urls import re_path
from .API.viewsets import GetUsuario, RegisterUsuario



urlpatterns = [
    re_path(r'usuario/buscar/(?P<id>[\w-]+)/?$', GetUsuario.as_view()),
    re_path(r'usuario/registro/', RegisterUsuario.as_view())
]