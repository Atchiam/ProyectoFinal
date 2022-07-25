
from django.urls import path
from .views import *



urlpatterns = [
    path("", inicio, name= "inicio"),
    path("about", about, name= "about"),
    path("blog", blog, name="blog"),
    path("nuevo-blog", nuevo_blog, name= "nuevo_blog"),
    path("ver-blog/<blog_id>", ver_blog, name= "ver_blog"),
    path("editar-blog/<blog_id>", editar_blog, name= "editar_blog"),
    path("borrar-blog/<blog_id>", borrar_blog, name= "borrar_blog"),
]
