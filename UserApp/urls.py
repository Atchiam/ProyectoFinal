from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path("registro-usuario", registro_user, name= "registro_user"),
    path("login", login_user, name= "login"),
    path("logout", LogoutView.as_view (template_name="ProyectoFinalApp/logout.html"), name = "logout" ),
    path("Editar-user", editar_user, name= "editar_user"),
    path('agregar-avatar', agregar_avatar, name="agregar_avatar"),
    path("ver-usuario", ver_user, name= "ver_user" ),
    
]