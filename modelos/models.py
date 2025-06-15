from django.db import models
from fabricantes.models import Fabricante

# Create your models here.
class Modelo(models.Model):
    nome = models.CharField(max_length=25)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.fabricante.nome}'