from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Persona (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    nacimiento= models.DateField()


class Avatar (models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField (upload_to="avatar/", blank=True, null=True, default= "/media/avatar/generica.jpg" )