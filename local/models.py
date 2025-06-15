from django.db import models

# Create your models here.
class Local(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome