from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre