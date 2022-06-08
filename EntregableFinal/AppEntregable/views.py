from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppEntregable.forms import *
from AppEntregable.models import *
# Create your views here.

#Pestaña de inicio con loader
def inicio(self):
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

#Pestaña de usuario
def usuario(request):
    return render(request, "usuario.html")

#Pestaña de crear usuario con formulario
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

#Pestaña de buscar usuario 
def busqueda_usuario(request):
    return render(request, "busqueda_usuario.html")
#Pestaña con lista de usuarios
def buscar(request):
    if request.GET["nombre_de_usuario"]:
        nombre_de_usuario = request.GET["nombre_de_usuario"]
        nombre = Usuario.objects.filter(nombre_de_usuario = nombre_de_usuario)
        apellido = Usuario.objects.filter(nombre_de_usuario = nombre_de_usuario)

        return render(request, "resultado_de_busqueda.html", {"nombre":nombre})
    else:
        respuesta = "no se encontro ningun usuario"
    return HttpResponse(respuesta)

def bibliotecas(request):
    return render(request,'bibliotecas.html')

def biblio_list(request):
    bibliotecas = Bibliotecas.objects.all()
    context = {'bibliotecas':bibliotecas}
    return render(request,'biblio_list.html', context=context)

def carga_biblio(request):
    if request.method == 'GET':
        form = Biblio_form()
        context = {'form':form}
        return render(request,'carga_biblio.html', context=context)
    else:
        form = Biblio_form(request.POST)
        if form.is_valid():
            nueva_biblio = Bibliotecas.objects.create(
                nombre = form.cleaned_data['nombre'],
                provincia = form.cleaned_data['provincia'],
                localidad = form.cleaned_data['localidad'],
                direccion = form.cleaned_data['direccion'],
                apertura = form.cleaned_data['apertura'],
                link = form.cleaned_data['link'],
                imagen = form.cleaned_data['imagen'],
                )   
            context={'nueva_biblio':nueva_biblio}
        return render(request,'carga_biblio.html', context=context)

def busca_biblio(request):
    biblioteca = Bibliotecas.objects.filter(nombre__icontains = request.GET['search'])
    context = {'biblioteca':biblioteca}
    return render(request,'busca_biblio.html', context=context)
