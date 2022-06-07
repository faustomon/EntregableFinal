from django import forms
#Formulario de usuario
class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nombre_de_usuario = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50)
    fecha_de_nacimiento = forms.DateField()