from django.db import models
from categorias.models import Categoria
from modelos.models import Modelo
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Equipamento(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    numero_serie = models.CharField(max_length=20, unique=True)
    horimetro_atual = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(99999)])
    horimetro_manutencao = models.IntegerField(default=0)
    data_manutencao = models.DateField(blank=True,null=True)
    usuario = models.ManyToManyField('usuarios.Usuario', related_name='equipamentos')

    def __str__(self):
        return f'{self.categoria.nome} - {self.numero_serie}'