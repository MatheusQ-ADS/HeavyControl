from django.db import models
from usuarios.models import Usuario
from equipamentos.models import Equipamento
from local.models import Local

# Create your models here.
class Atividade(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=50)
    horimetro_inicial = models.IntegerField()
    horimetro_final = models.IntegerField()
    horimetro_abastecimento = models.IntegerField()
    litros_abastecimento = models.IntegerField()
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.horimetro_final > self.equipamento.horimetro_atual:
            self.equipamento.horimetro_atual = self.horimetro_final
            self.equipamento.save()

    def __str__(self):
        return f'{self.data} - {self.usuario.username} - {self.equipamento.categoria.nome}'