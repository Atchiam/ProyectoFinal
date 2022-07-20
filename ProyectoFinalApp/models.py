from django.db import models
from django.db.models import Model

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


class Comida (models.Model):
    tipo = models.CharField (max_length= 30)
    tamaño = models.CharField (max_length= 30)
    nombre = models.CharField (max_length=30)
    peso = models.IntegerField(default="peso")
    precio = models.IntegerField(default="precio")

class Pipeta (models.Model):
    tipo = models.CharField (max_length= 30)
    nombre = models.CharField (max_length=30)
    peso = models.IntegerField(default="peso")
    precio = models.IntegerField(default="precio")

class Collar (models.Model):
    largo = models.IntegerField(default="largo") 
    color = models.CharField (max_length=30, default="color")
    precio = models.IntegerField(default="precio")
    class Meta:
        verbose_name_plural = "Collares"

class BlogCard (models.Model):
    título = models.CharField (max_length= 30)
    subtítulo = models.CharField (max_length= 30)
    texto = models.CharField (max_length=1000)
    imagen = models.CharField (max_length=1000)
    autor = models.CharField (max_length= 30) 
    fecha = models.DateField (auto_now = True)