from django.contrib import admin
from .models import Local

# Register your models here.
@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ['nome']