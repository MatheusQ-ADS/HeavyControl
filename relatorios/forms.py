from django import forms

class FiltroRelatorioMensalForm(forms.Form):
    mes = forms.IntegerField(label='Mês', min_value=1, max_value=12)
    ano = forms.IntegerField(label='Ano', min_value=2025, max_value=2100)