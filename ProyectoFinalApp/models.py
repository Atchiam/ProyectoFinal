from django.db import models
from django.db.models import Model

# Create your models here.

class BlogCard (models.Model):
    título = models.CharField (max_length= 30)
    subtítulo = models.CharField (max_length= 30)
    texto = models.CharField (max_length=2000)
    imagen = models.CharField (max_length=1000)
    autor = models.CharField (max_length= 30) 
    fecha = models.DateField (auto_now = True)