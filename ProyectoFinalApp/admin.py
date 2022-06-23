from django.contrib import admin

from .models import *
# Register your models here.

class CursoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'comision','fecha','duracion')
    #search_fields = ('nombre', 'comision','fecha','duracion')

class EventoAdmin (admin.ModelAdmin):
    list_display = ('nombre', 'descripcion','fecha','duracion')
    #search_fields = ('nombre', 'descripcion','fecha','duracion')

admin.site.register( Curso, CursoAdmin)
admin.site.register( Evento, EventoAdmin)