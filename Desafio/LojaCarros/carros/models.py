from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=255)

class Carros(models.Model):
    modelo_veiculo = models.CharField(max_length=255)
    ano = models.IntegerField()
    