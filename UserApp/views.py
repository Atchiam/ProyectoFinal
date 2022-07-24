from requests import request

from UserApp.models import Persona
from django.shortcuts import redirect, render
from .models import *
from .forms import *

from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

"""
def inicio (request):
    return render (request, "", {} )
"""
def personas(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            personas = Persona.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()

            return render(request,"UserApp/personas",{"personas":personas, "search":True, "busqueda":search})

    personas = Persona.objects.all()

    return render(request,"UserApp/personas",{"personas":personas})

def crearPersona(request):
    
    # post
    if request.method == "POST":
        
        formulario = PersonaFormulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            persona = persona(nombre=info["nombre"],apellido=info["apellido"],email=info["email"])
            persona.save()

            return redirect("personas")

        return render(request,"UserApp/formulario_persona",{"form":formulario})

    # get
    formulario = PersonaFormulario()
    return render(request,"UserApp/formulario_persona",{"form":formulario})

def eliminarPersona(request,persona_id):

    persona = Persona.objects.get(id=persona_id)
    persona.delete()
    return redirect("personas")

def editarPersona(request,persona_id):

    persona = persona.objects.get(id=persona_id)

    if request.method == "POST":

        formulario = PersonaFormulario(request.POST)

        if formulario.is_valid():
            
            info_persona = formulario.cleaned_data
            
            persona.nombre = info_persona["nombre"]
            persona.apellido = info_persona["apellido"]
            persona.email = info_persona["email"]
            persona.nacimiento = info_persona["nacimiento"]
            persona.save()

            return redirect("personas")

    # get
    formulario = PersonaFormulario(initial={"nombre":persona.nombre, "apellido":persona.apellido, "email": persona.email})
    
    return render(request,"UserApp/formulario_persona",{"form":formulario})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("personas")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"UserApp/login",{"form":form})

def registrate_request(request):

    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # es la primer contraseña, no la confirmacion

            form.save() # registramos el usuario
            # iniciamos la sesion
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")

        return render(request,"UserApp/registrate.html",{"form":form})

    # form = UserCreationForm()
    form = UserCreationForm()

    return render(request,"UserApp/registrate.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("personas")