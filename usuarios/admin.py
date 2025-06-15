from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import CustomUsuarioChangeForm, CustomUsuarioCreationForm

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreationForm
    form = CustomUsuarioChangeForm
    model = Usuario
    
    list_display = ('username', 'email', 'cpf', 'cargo', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'cargo')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações pessoais', {'fields': ('email', 'cpf', 'cargo')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'cpf', 'cargo', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    search_fields = ('username', 'email', 'cpf')
    ordering = ('username',)