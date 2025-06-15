from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    cargo = models.CharField(max_length=25)

    def __str__(self):
        return self.username