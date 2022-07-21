from django.contrib import admin
from .models import *

class PersonaAdmin (admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "nacimiento")

admin.site.register( Persona, PersonaAdmin)
