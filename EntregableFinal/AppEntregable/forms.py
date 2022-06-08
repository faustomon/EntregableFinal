from django import forms
from AppEntregable.models import *
#Formulario de usuario
class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nombre_de_usuario = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50)
    fecha_de_nacimiento = forms.DateField()

class Biblio_form(forms.ModelForm):
    class Meta:
        model = Bibliotecas
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'provincia': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'apertura': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'imagen': forms.URLInput(attrs={'class':'form-control'}),
        }

class Libro_form(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }