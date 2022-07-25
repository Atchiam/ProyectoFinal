
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from UserApp.models import *

from .forms import *

from django.db.models import Q


# Create your views here.

def inicio (request):
    
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user_id = request.user.id)
            url = avatar.imagen.url
            
        except:
            url = "/media/avatar/generica.jpg"
            
        return render(request,"ProyectoFinalApp\main.html",{"url":url})
    
    return render (request, "ProyectoFinalApp\main.html", {} )

def about (request):
    
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user_id = request.user.id)
            url = avatar.imagen.url
            
        except:
            url = "/media/avatar/generica.jpg"
            
        return render(request,r"ProyectoFinalApp\about.html",{"url":url})
    
    return render (request, r"ProyectoFinalApp\about.html", {} )

def blog (request):
    
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user_id = request.user.id)
            url = avatar.imagen.url
            
        except:
            url = "/media/avatar/generica.jpg"
    else:
        url = ""
    
    if request.method == "POST":
        #nombre = Comida.objects.all()
        nombre = request.POST["nombre"]
        blogs = BlogCard.objects.filter(  
            Q(título__icontains = nombre)   |
            Q(subtítulo__icontains = nombre)|
            Q(texto__icontains = nombre)    |
            Q(imagen__icontains = nombre)   |
            Q(autor__icontains = nombre)    |
            Q(fecha__icontains = nombre)
        )
        return render(request, "ProyectoFinalApp/blog.html",{"blogs":blogs, "url":url})
    else: # get y otros
        blogs = BlogCard.objects.all()
        return render(request, "ProyectoFinalApp/blog.html",{"blogs":blogs, "url":url})

@login_required
def nuevo_blog(request):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user_id = request.user.id)
            url = avatar.imagen.url
            
        except:
            url = "/media/avatar/generica.jpg"
    else:
        url = ""

    if request.method == "POST":
        formulario = NuevoBlogCard(request.POST)
        if formulario.is_valid():
        
            info_formulario = request.POST
            user_formulario = request.user
            nuevoblog = BlogCard(
                        título = info_formulario["título"], 
                        subtítulo = info_formulario["subtítulo"],
                        texto = info_formulario["texto"],
                        imagen = (info_formulario["imagen"]),
                        autor = user_formulario.username ,
                        )
            nuevoblog.save()
            
            return redirect ("blog")
        
        else:
            return redirect ("blog")
    
    else: #get y otros
        formulariovacio = NuevoBlogCard()
        
        return render (request, r"ProyectoFinalApp\nuevo_blog.html",{"form": formulariovacio, "url":url})


def ver_blog (request, blog_id):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user_id = request.user.id)
            url = avatar.imagen.url
            
        except:
            url = "/media/avatar/generica.jpg"
    else:
        url = ""
    
    blog = BlogCard.objects.get(id=blog_id)
    
    return render (request, r"ProyectoFinalApp\ver_blog.html", {"blog" : blog, "url" : url}  )


@login_required
def borrar_blog (request, blog_id):
    
    usercard = str(BlogCard.objects.get(id=blog_id).autor)
    
    userrequest = str(request.user)
    
    if(usercard == userrequest) :
        blog = BlogCard.objects.get(id=blog_id)
        
        blog.delete()
        
        return redirect("blog")
    else:
        return redirect("blog")


@login_required
def editar_blog(request , blog_id):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user_id = request.user.id)
            url = avatar.imagen.url
            
        except:
            url = "/media/avatar/generica.jpg"

    usercard = str(BlogCard.objects.get(id=blog_id).autor)
    
    userrequest = str(request.user)
    
    if(usercard == userrequest):
        blog = BlogCard.objects.get(id = blog_id)
        #Si es metodo POST hago lo mismo que el agregar
        if request.method =='POST':
            
            formulario = NuevoBlogCard(request.POST)
            
            if formulario.is_valid():
            
                info_formulario = formulario.cleaned_data
                
                blog.título= info_formulario["título"]
                blog.subtítulo = info_formulario["subtítulo"]
                blog.texto = info_formulario["texto"]
                blog.imagen = info_formulario["imagen"]
                
                blog.save()
                
                return redirect ("blog")
            
            else:
                return redirect ("blog")
            
        #En caso que no sea post
        else:
            miFormulario=NuevoBlogCard(initial={"título": blog.título, "subtítulo": blog.subtítulo, "texto": blog.texto,"imagen": blog.imagen,"autor": blog.autor})
        #Voy al html que me permite editar
        return render(request,"ProyectoFinalApp/editar_blog.html",{"form":miFormulario, "url":url})
    else:
        return redirect("blog")