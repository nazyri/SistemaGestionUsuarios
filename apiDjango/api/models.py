from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    clave = models.CharField(max_length=15)


    def __str__(self):
        return self.nombre