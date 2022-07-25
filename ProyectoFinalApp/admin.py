from django.contrib import admin

from .models import *
# Register your models here.


class BlogCardAdmin (admin.ModelAdmin):
    list_display = ("título", "subtítulo", "texto", "imagen","autor","fecha")



admin.site.register( BlogCard, BlogCardAdmin)
