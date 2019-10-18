"""
Definition of models.
"""

from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    """ Modelo base para la aplicacion """
    added = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)
    is_enabled = models.BooleanField(default = True)

    class Meta:
        abstract = True


class Persona(BaseModel):
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    fecha_nacimiento = models.DateField("Fecha de nacimiento")


    def __str__(self):
        return self.nombre + " " + self.apellido
