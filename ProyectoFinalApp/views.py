from django.shortcuts import redirect, render
from .models import *

from .forms import *

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
