from django.urls import path
from AppEntregable import views
from AppEntregable.views import *
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("usuario/", usuario, name="Usuario"),
    path("busquedaUsuario/", busqueda_usuario, name="Busqueda_Usuario"),
    path("buscar/", buscar, name="Buscar"),
    path("crearUsuario/", crear_usuario, name="Crear_Usuario"),
] 