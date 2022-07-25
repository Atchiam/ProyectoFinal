from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from UserApp.models import Avatar



class Edit_user(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    avatar = forms.ImageField(label= "ingresa tu nuevo avatar")
    class Meta:
        
        model = User
        fields = ['email', 'first_name', 'last_name']

class AvatarForm(forms.Form):
    
    imagen = forms.ImageField(label="imagen", required=False)