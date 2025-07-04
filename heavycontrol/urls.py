"""
URL configuration for heavycontrol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
    path("admin/", admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('equipamentos/', include('equipamentos.urls')),
    path('atividades/', include('atividade.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('login'), permanent=False))
]
