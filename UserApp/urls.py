from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("", inicio, name="inicio"),   
    path('personas/', personas, name="personas"),
    path('crearpersona', crearPersona, name="crearpersona"),
    path('eliminarPersona/<persona_id>', eliminarPersona, name="eliminarPersona"),
    path('editarPersona/<persona_id>', editarPersona, name="editarPersona"),
    path('login>', login_request, name="login"),
]