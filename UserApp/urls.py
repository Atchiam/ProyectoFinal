from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    #path("", inicio, name="inicio"),   
    path('login>', login_request, name="login"),
    path('register', registrate_request, name="register"),
    path('logout', logout_request, name="logout"),
    
    path('personas/', personas, name="personas"),
        path('crearpersona', crearPersona, name="crearpersona"),
        path('eliminarPersona/<persona_id>', eliminarPersona, name="eliminarPersona"),
        path('editarPersona/<persona_id>', editarPersona, name="editarPersona"),
]