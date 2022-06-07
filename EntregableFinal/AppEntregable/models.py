from django.db import models

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nombre_de_usuario=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    fecha_de_nacimiento=models.DateField()
    def __str__(self):
        return self.nombre+" "+str(self.apellido)+" "+str(self.nombre_de_usuario)