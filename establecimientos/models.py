from django.db import models
from django.contrib.auth.models import User
from recetas.models import Receta

# MODELS EXTABLECIMIENTOS

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    usuarios = models.ManyToManyField(User, through='Asignacion')
    recetas = models.ManyToManyField(Receta)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} en {self.establecimiento.nombre} como {self.rol.nombre}"