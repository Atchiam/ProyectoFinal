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
    return render (request, r"ProyectoFinalApp\agregar.html",{})