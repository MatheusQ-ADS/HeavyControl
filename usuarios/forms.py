from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Usuario

class CustomUsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'cargo')
    
class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'cargo')

class CPFLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='CPF',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu CPF'
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )