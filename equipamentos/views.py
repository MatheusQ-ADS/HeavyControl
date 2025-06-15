from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def minha_lista_equipamentos(request):
    equipamentos = request.user.equipamentos.all()
    return render(request, 'equipamentos/minha_lista.html', {'equipamentos': equipamentos})