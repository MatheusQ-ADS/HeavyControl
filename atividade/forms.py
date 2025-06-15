from django import forms
from .models import Atividade
from equipamentos.models import Equipamento

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = [
            'data',
            'descricao',
            'horimetro_inicial',
            'horimetro_final',
            'horimetro_abastecimento',
            'litros_abastecimento',
            'equipamento',
            'local',
        ]
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user and not user.is_staff:
            self.fields['equipamento'].queryset = Equipamento.objects.filter(usuario=user)