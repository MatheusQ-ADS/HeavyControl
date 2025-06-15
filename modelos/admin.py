from django.contrib import admin
from .models import Modelo

# Register your models here.
@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'fabricante']