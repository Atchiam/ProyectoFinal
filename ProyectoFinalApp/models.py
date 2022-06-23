from django.db import models
from django.forms import DurationField

# Create your models here.
class Curso (models.Model):
    nombre = models.CharField(max_length=30)
    comision= models.IntegerField
    fecha= models.DateField()
    duracion= models.DurationField()
    class Meta:
        verbose_name_plural = "Cursos"

class Evento (models.Model):
    nombre =models.CharField(max_length=60)
    descripcion= models.CharField (max_length=300)
    fecha= models.DateField()
    duracion= models.DurationField()