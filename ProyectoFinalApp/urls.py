from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("", inicio, name="inicio"),
    path("cursos", cursos, name="cursos"),
    path("eventos",eventos, name= "eventos"),
    path("agregar", agregar, name= "agregar"),
    path("agregar_collar", agregar_collar , name= "agregar_collar"),
    path("agregar_comida", agregar_comida , name= "agregar_comida"),
    path("agregar_pipeta", agregar_pipeta , name= "agregar_pipeta"),
    path("catalogo", catalogo, name="catalogo"),
    path("blog", blog, name="blog"),
    path("nuevo-blog", nuevo_blog, name= "nuevo_blog"),
    path("ver-blog/<blog_id>", ver_blog, name= "ver_blog"),
    path("editar-blog/<blog_id>", editar_blog, name= "editar_blog"),
    path("borrar-blog/<blog_id>", borrar_blog, name= "borrar_blog"),
    
]
