from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("", inicio, name="inicio"),
    path("leerPersona",leerPersona, name="leerPersona"),
    
    
    
    path('persona/', persona, name="persona"),
    path('leerPersona/', leerPersona, name="leerPersona"),
    path('eliminarPersona/<persona_id>', eliminarPersona, name="eliminarPersona"),
    path('editarPersona/<persona_id>', editarPersona, name="editarPersona"),
]