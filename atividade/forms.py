from django import forms
from .models import Atividade
from equipamentos.models import Equipamento

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        exclude = ['usuario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'horimetro_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'horimetro_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'horimetro_abastecimento': forms.NumberInput(attrs={'class': 'form-control'}),
            'litros_abastecimento': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'equipamento': forms.Select(attrs={'class': 'form-select'}),
            'local': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user and not user.is_staff:
            self.fields['equipamento'].queryset = Equipamento.objects.filter(usuario=user)