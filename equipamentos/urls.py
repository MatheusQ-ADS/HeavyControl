from django.urls import path
from . import views

urlpatterns = [
    path('meus/', views.minha_lista_equipamentos, name='minha_lista_equipamentos'),
]