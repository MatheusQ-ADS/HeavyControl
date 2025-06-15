from django import forms
from datetime import datetime

class FiltroRelatorioMensalForm(forms.Form):
    MES_CHOICES = [(i,i) for i in range(1,13)]
    ANO_CHOICES = [(i,i) for i in range(2025, datetime.now().year + 5)]

    mes = forms.ChoiceField(choices=MES_CHOICES, label='Mês', widget=forms.Select(
        attrs={'class': 'form-select'}
    ))
    ano = forms.ChoiceField(choices=ANO_CHOICES, label='Ano', widget=forms.Select(
        attrs={'class': 'form-select'}
    ))