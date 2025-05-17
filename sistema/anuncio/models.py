from django.db import models
from django.utils import timezone
from veiculo.models import *

class Anuncio(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    diaria = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
