from django.shortcuts import render
from .models import *

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

        info_formulario = request.POST
        
        pipeta = Pipeta(tipo = info_formulario["tipo"], nombre = info_formulario["nombre"], peso = int(info_formulario["peso"]), precio = int(info_formulario["precio"]))
        pipeta.save()
        return render (request, r"ProyectoFinalApp\agregar.html",{})
    
    else: #get y otros
        return render (request, r"ProyectoFinalApp\agregar_pipeta.html",{})

def agregar_collar (request):
#post
    if request.method == "POST":

        info_formulario = request.POST
        
        collar = Collar(largo = int(info_formulario["largo"]), color= info_formulario["color"],precio = int(info_formulario["precio"]))
        collar.save()
        return render (request, r"ProyectoFinalApp\agregar.html",{})
    
    else: #get y otros
        return render (request, r"ProyectoFinalApp\agregar_collar.html",{})

def agregar_comida (request):
#post
    if request.method == "POST":

        info_formulario = request.POST
        
        comida = Comida(tipo = info_formulario["tipo"], tamaño = info_formulario["tamaño"],nombre = info_formulario["nombre"],peso = int(info_formulario["peso"]),precio = int(info_formulario["precio"]))
        comida.save()
        return render (request, r"ProyectoFinalApp\agregar.html",{})
    
    else: #get y otros
        return render (request, r"ProyectoFinalApp\agregar_comida.html",{})
