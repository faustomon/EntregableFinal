from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppEntregable.forms import UsuarioForm
from AppEntregable.models import Usuario
# Create your views here.

def inicio(self):
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def usuario(request):
    return render(request, "usuario.html")

def crear_usuario(request):
    if request.method == "POST":
        miFormulario = UsuarioForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            nombre_de_usuario= informacion["nombre_de_usuario"]
            email= informacion["email"]
            password= informacion["password"]
            fecha_de_nacimiento= informacion["fecha_de_nacimiento"]
            usuario = Usuario (nombre=nombre, apellido=apellido, nombre_de_usuario=nombre_de_usuario, email=email, password=password, fecha_de_nacimiento=fecha_de_nacimiento)
            usuario.save()
            return render(request, "inicio.html")

    else:
        miFormulario = UsuarioForm()
    
    return render(request, "crear_usuario.html", {"miFormulario":miFormulario})

def busqueda_usuario(request):
    return render(request, "busqueda_usuario.html")

def buscar(request):
    if request.GET["nombre_de_usuario"]:
        nombre_de_usuario = request.GET["nombre_de_usuario"]
        nombre = Usuario.objects.filter(nombre_de_usuario = nombre_de_usuario)
        apellido = Usuario.objects.filter(nombre_de_usuario = nombre_de_usuario)

        return render(request, "resultado_de_busqueda.html", {"nombre":nombre})
    else:
        respuesta = "no se encontro ningun usuario"
    return HttpResponse(respuesta)
