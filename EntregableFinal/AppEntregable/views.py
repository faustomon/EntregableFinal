from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def inicio(self):
    plantilla = loader.get_template("inicio.html/")
    documento = plantilla.render()
    return HttpResponse(documento)