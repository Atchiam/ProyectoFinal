
from django.urls import path
from .views import *
from UserApp.urls import *


urlpatterns = [
    path("", inicio, name= "inicio"),
    path("about", about, name= "about"),
    path("blog", blog, name="blog"),
    path("nuevo-blog", nuevo_blog, name= "nuevo_blog"),
    path("ver-blog/<blog_id>", ver_blog, name= "ver_blog"),
    path("editar-blog/<blog_id>", editar_blog, name= "editar_blog"),
    path("borrar-blog/<blog_id>", borrar_blog, name= "borrar_blog"),
    
    #path("", inicio, name="inicio"),   
    path('login>', login_request, name="login"),
    path('register', registrate_request, name="register"),
    path('logout', logout_request, name="logout"),
    
    path('personas/', personas, name="personas"),
        path('crearpersona', crearPersona, name="crearpersona"),
        path('eliminarPersona/<persona_id>', eliminarPersona, name="eliminarPersona"),
        path('editarPersona/<persona_id>', editarPersona, name="editarPersona"),

]
