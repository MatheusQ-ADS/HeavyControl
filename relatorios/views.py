from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from atividade.models import Atividade
from .forms import FiltroRelatorioMensalForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.utils.timezone import now
import openpyxl

# Create your views here.
@login_required
def filtro_relatorio_mensal(request):
    atividades = []
    if request.method == 'POST':
        form = FiltroRelatorioMensalForm(request.POST)
        if form.is_valid():
            mes = int(form.cleaned_data['mes'])
            ano = int(form.cleaned_data['ano'])
            atividades = Atividade.objects.filter(
                usuario=request.user,
                data__year=ano,
                data__month=mes,
                equipamento__in=request.user.equipamentos.all()
            ).order_by('data')
    else:
        form = FiltroRelatorioMensalForm()
    return render(request, 'relatorios/filtro_relatorio_mensal.html', {'form': form, 'atividades': atividades})

@login_required
def exportar_excel_mensal(request, mes, ano):
    atividades = Atividade.objects.filter(
        usuario=request.user,
        data__year=ano,
        data__month=mes,
        equipamento__in=request.user.equipamentos.all()
    )

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Relatório Mensal'
    ws.append(['Data', 'Equipamento', 'Descrição', 'Horímetro Inicial', 'Horímetro Final', 'Local'])
    for a in atividades:
        ws.append([
            a.data.strftime('%d/%m/%Y'),
            str(a.equipamento),
            a.descricao,
            int(a.horimetro_inicial),
            int(a.horimetro_final),
            a.local.nome,
        ])
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=relatorio_{mes}_{ano}.xlsx'
    wb.save(response)
    return response

@login_required
def exportar_pdf_mensal(request, mes, ano):
    atividades = Atividade.objects.filter(
        usuario=request.user,
        data__year=ano,
        data__month=mes,
        equipamento__in=request.user.equipamentos.all()
    )
    html_string = render_to_string('relatorios/relatorio_pdf_mensal.html', {
        'atividades': atividades,
        'mes': mes,
        'ano': ano,
        'usuario': request.user,
        'data_geracao': now(),
    })
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=relatorio_{mes}_{ano}.pdf'
    return response