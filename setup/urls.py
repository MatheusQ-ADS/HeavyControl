
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('HeavyControl/', admin.site.urls),
    path('', admin.site.urls),
]
