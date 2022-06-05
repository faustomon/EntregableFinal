from django.urls import path
from AppEntregable import views
from AppEntregable.views import *
urlpatterns = [
    path("", inicio, name="Inicio"),
] 