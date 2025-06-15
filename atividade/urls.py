from django.urls import path
from . import views

urlpatterns = [
    path('minhas/', views.minhas_atividades, name='minhas_atividades'),
    path('nova/', views.nova_atividade, name='nova_atividade'),
    path('editar/<int:id>/', views.editar_atividade, name='editar_atividade'),
]