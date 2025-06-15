
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class CustomUsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'cargo')
    
class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'cargo')