from django.urls import path
from AppEntregable import views
from AppEntregable.views import *
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("usuario/", usuario, name="Usuario"),
    path("busquedaUsuario/", busqueda_usuario, name="Busqueda_Usuario"),
    path("buscar/", buscar, name="Buscar"),
    path("crearUsuario/", crear_usuario, name="Crear_Usuario"),
    path('bibliotecas/', bibliotecas, name='bibliotecas'),
    path('biblio_list/', biblio_list, name='biblio_list'),
    path('carga_biblio/', carga_biblio, name='carga_biblio'),
    path('busca_biblio/', busca_biblio, name='busca_biblio'),
] 