from django.contrib import admin
from .models import Atividade

# Register your models here.
@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['data', 'usuario', 'equipamento', 'local', 'descricao', 'horimetro_inicial', 'horimetro_final']
    list_filter = ['data', 'usuario', 'equipamento']