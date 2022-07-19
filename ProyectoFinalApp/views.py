from django.shortcuts import redirect, render
from .models import *

from .forms import *

from django.db.models import Q

# Create your views here.

def inicio (request):
    return render (request, "ProyectoFinalApp\main.html", {} )

def cursos (request):
    cursos = Curso.objects.all()
    ctx={'cursos':cursos}
    return render (request, "ProyectoFinalApp\cursos.html", ctx  )

def eventos (request):
    eventos = Evento.objects.all()
    ctx1={'eventos':eventos}
    return render (request, "ProyectoFinalApp\eventos.html", ctx1  )

def agregar (request):
    
    
#get
    if request.method =="GET":
        return render (request, r"ProyectoFinalApp\agregar.html",{})
#post
    elif request.method == "POST":
        
        print(request)
        # info_formulario = request.POST
        
        # curso = Curso(info_formulario["nombre"], info_formulario["comision"])
        # curso.save()
        return render (request, "ProyectoFinalApp\main.html", {} )

def agregar_pipeta (request):
#post
    if request.method == "POST":

        formulario = NuevoPipeta(request.POST)
        
        if formulario.is_valid():
            
            info_pipeta = formulario.cleaned_data
            
            pipeta = Pipeta(tipo = info_pipeta["tipo"], nombre = info_pipeta["nombre"], peso = int(info_pipeta["peso"]), precio = int(info_pipeta["precio"]))
            pipeta.save()
            return redirect ("inicio")
        
        else:
            return redirect ("agregar_pipeta")
    
    else: #get y otros
        formulariovacio= NuevoPipeta()
        
        return render (request, r"ProyectoFinalApp\agregar_pipeta.html", {"form": formulariovacio})

def agregar_collar (request):
#post
    if request.method == "POST":
        
        formulario = NuevoCollar(request.POST)
        
        if formulario.is_valid():
            
            info_formulario = request.POST

            collar = Collar(largo = int(info_formulario["largo"]), color= info_formulario["color"],precio = int(info_formulario["precio"]))
            collar.save()
            return redirect ("inicio")
        
        else:
            return redirect ("agregar_collar")
    
    else: #get y otros
        formulariovacio = NuevoCollar()
        
        return render (request, r"ProyectoFinalApp\agregar_collar.html",{"form": formulariovacio})

def agregar_comida (request):
#post
    if request.method == "POST":
        formulario = NuevoComida(request.POST)
        if formulario.is_valid():
        
            info_formulario = request.POST
            
            comida = Comida(tipo = info_formulario["tipo"], tamaño = info_formulario["tamaño"],nombre = info_formulario["nombre"],peso = int(info_formulario["peso"]),precio = int(info_formulario["precio"]))
            comida.save()
            return redirect ("inicio")
    
    else: #get y otros
        formulariovacio = NuevoComida()
        
        return render (request, r"ProyectoFinalApp\agregar_comida.html",{"form": formulariovacio})

def catalogo(request):
    
    if request.method == "POST":
        #nombre = Comida.objects.all()
        nombre = request.POST["nombre"]
        comidas = Comida.objects.filter(  
            Q(nombre__icontains = nombre) |
            Q(tipo__icontains = nombre)   |
            Q(precio__icontains = nombre) |
            Q(peso__icontains = nombre)   |
            Q(tamaño__icontains = nombre)
        )
        return render(request, "ProyectoFinalApp/catalogo.html",{"comidas":comidas})
    else: # get y otros
        comidas = [] # Curso.objects.all()
    
        return render(request, "ProyectoFinalApp/catalogo.html",{"comidas":comidas})

def blog (request):
    
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
        return render(request, "ProyectoFinalApp/blog.html",{"blogs":blogs})
    else: # get y otros
        blogs = BlogCard.objects.all()
        return render(request, "ProyectoFinalApp/blog.html",{"blogs":blogs})


def nuevo_blog(request):
    if request.method == "POST":
        formulario = NuevoBlogCard(request.POST)
        if formulario.is_valid():
        
            info_formulario = request.POST
            
            nuevoblog = BlogCard(título = info_formulario["título"], subtítulo = info_formulario["subtítulo"],texto = info_formulario["texto"],imagen = (info_formulario["imagen"]),autor = (info_formulario["autor"]))
            nuevoblog.save()
            
            return redirect ("inicio")
        
        else:
            return redirect ("catalogo")
    
    else: #get y otros
        formulariovacio = NuevoBlogCard()
        
        return render (request, r"ProyectoFinalApp\nuevo_blog.html",{"form": formulariovacio})


def ver_blog (request, blog_id):
    
    blog = BlogCard.objects.get(id=blog_id)
    
    return render (request, r"ProyectoFinalApp\ver_blog.html", {"blog" : blog}  )



def borrar_blog (request, blog_id):
    
    blog = BlogCard.objects.get(id=blog_id)
    
    blog.delete()
    
    return redirect ("blog")



def editar_blog(request , blog_id):
    
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
            blog.autor = info_formulario["autor"]
            
            blog.save()
            
            return redirect ("inicio")
        
        else:
            return redirect ("catalogo")
        
    #En caso que no sea post
    else:
        miFormulario=NuevoBlogCard(initial={"título": blog.título, "subtítulo": blog.subtítulo, "texto": blog.texto,"imagen": blog.imagen,"autor": blog.autor})
    #Voy al html que me permite editar
    return render(request,"ProyectoFinalApp/editar_blog.html",{"form":miFormulario})