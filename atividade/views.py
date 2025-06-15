from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Atividade
from .forms import AtividadeForm

# Create your views here.
@login_required
def minhas_atividades(request):
    atividades = Atividade.objects.filter(usuario=request.user)
    return render(request, 'atividades/minha_lista.html', {'atividades': atividades})

@login_required
def nova_atividade(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.usuario = request.user
            if atividade.equipamento in request.user.equipamentos.all():
                atividade.save()
                return redirect('minhas_atividades')
            else:
                form.add_error('equipamento', 'Você só pode criar atividades para os seus equipamentos.')
    else:
        form = AtividadeForm()
        form.fields['equipamento'].queryset = request.user.equipamentos.all()
    return render(request, 'atividades/form.html', {'form': form})

@login_required
def editar_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id, usuario=request.user)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.usuario = request.user
            if atividade.equipamento in request.user.equipamentos.all():
                atividade.save()
                return redirect('minhas_atividades')
            else:
                form.add_error('equipamentos', 'Você só pode alterar atividades dos seus equipamentos.')
    else:
        form = AtividadeForm(instance=atividade)
        form.fields['equipamento'].queryset = request.user.equipamentos.all()
    return render(request, 'atividades/form.html', {'form': form})