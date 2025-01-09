from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    celular = models.CharField(max_length=15)
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=100)
