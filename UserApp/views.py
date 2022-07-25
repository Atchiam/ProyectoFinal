
from django.shortcuts import redirect, render
from .models import *
from .forms import *

from django.db.models import Q

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def registro_user(request):

    # post
    if request.method == "POST":
        
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            
            username= formulario.cleaned_data['username']
            formulario.save()
            
            return redirect("login")
        else:
            return redirect("login")

    else:
        formu = UserCreationForm()
        return render(request,"ProyectoFinalApp/registro_user.html",{ "form" : formu})


def login_user(request):

    
    if request.method =="POST":
        form= AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user=authenticate(username=usuario,password=contra)
            
            if user is not None:
                
                login(request,user)
                
                return redirect("blog")
            
            else:
                return redirect("login")
        else:
            return redirect("registro_user")
    
    else:
        form = AuthenticationForm()
        
        return render (request,r"ProyectoFinalApp/login.html",{"form":form})


@login_required
def editar_user(request):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user_id = request.user.id)
            url = avatar.imagen.url
            
        except:
            url = "/media/avatar/generica.jpg"
    else:
        url = ""

    user = request.user
    try:
        avatar = Avatar.objects.get(user = user)
    except:
        avatar= Avatar(user = user)
        avatar.save()

    if request.method == "POST":

        formulario = Edit_user(request.POST, request.FILES)

        if formulario.is_valid():
            
            info_user = formulario.cleaned_data
            
            user.email = info_user["email"]
            user.first_name = info_user["first_name"]
            user.last_name = info_user["last_name"]
            
            user.save()
            
            if info_user["avatar"] != None:
                avatar.imagen = info_user["avatar"]
                avatar.save()
                return redirect("inicio")

            return redirect("inicio")

    else:
        formulario = Edit_user(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name, "avatar":user.avatar })
        
    return render(request,"ProyectoFinalApp/editar_user.html",{"form":formulario, "usuario":user, "url": url})

@login_required
def agregar_avatar(request):
    
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user_id = request.user.id)
            url = avatar.imagen.url
            
        except:
            url = "/media/avatar/generica.jpg"
    else:
        url = ""
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            u = User.objects.get(username = request.user) # usuario con el que estamos loggueados
            
            print (u)
            
            avatar = Avatar(user=u, imagen=form.cleaned_data["imagen"])

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            avatar.save()

            return redirect("inicio")

    else:
        form = AvatarForm()
    
    return render(request,r"ProyectoFinalApp/agregar_avatar.html",{"form":form, "url": url})

@login_required
def ver_user (request):
    
    if request.user.is_authenticated:
        usuario= User.objects.get(username = request.user)
        try:
            avatar = Avatar.objects.get(user_id = request.user.id)
            url = avatar.imagen.url
            
        except:
            url = "/media/avatar/generica.jpg"
    
    
    return render(request, r"ProyectoFinalApp\ver_user.html",{"url":url, "user": usuario})
    

