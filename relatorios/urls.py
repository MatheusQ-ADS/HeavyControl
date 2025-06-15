from django.urls import path
from . import views

urlpatterns = [
    path('filtro_mensal/', views.filtro_relatorio_mensal, name='filtro_relatorio_mensal'),
    path('exportar_excel/<int:mes>/<int:ano>/', views.exportar_excel_mensal, name='exportar_excel_mensal'),
    path('exportar_pdf/<int:mes>/<int:ano>/', views.exportar_pdf_mensal, name='exportar_pdf_mensal'),
]