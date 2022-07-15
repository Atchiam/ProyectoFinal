from django.contrib import admin

from .models import *
# Register your models here.

class CursoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'comision','fecha','duracion')
    #search_fields = ('nombre', 'comision','fecha','duracion')

class EventoAdmin (admin.ModelAdmin):
    list_display = ('nombre', 'descripcion','fecha','duracion')
    #search_fields = ('nombre', 'descripcion','fecha','duracion')

class ComidaAdmin (admin.ModelAdmin):
    list_display = ("tipo","tamaño","nombre","peso","precio")

class PipetaAdmin (admin.ModelAdmin):
    list_display = ("tipo","nombre","peso","precio")

class CollarAdmin (admin.ModelAdmin):
    list_display = ("largo", "color", "precio")

class BlogCardAdmin (admin.ModelAdmin):
    list_display = ("título", "subtítulo", "texto", "imagen","autor","fecha")



admin.site.register( Curso, CursoAdmin)
admin.site.register( Evento, EventoAdmin)
admin.site.register( Comida, ComidaAdmin)
admin.site.register( Pipeta, PipetaAdmin)
admin.site.register( Collar, CollarAdmin)
admin.site.register( BlogCard, BlogCardAdmin)
