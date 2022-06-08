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
    path("textos/", textos, name="textos"),
    path("hansel-gretel/", hanselYGretel, name="hansel_gretel"),
    path("gato-con-botas/", gatoConBotas, name="gato_con_botas"),
    path("tres-cerditos/", tresCerditos, name="tres_cerditos"),
    path("crear_libro/", crear_libro, name="crear_libro"),
    path("busqueda_libro/", busqueda_libro, name="busqueda_libro"),
    path("buscar_libro/", buscar_libro, name="buscar_libro"),
] 