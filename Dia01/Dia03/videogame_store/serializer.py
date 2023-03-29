from rest_framework import serializers
from .models import Jogo , Loja


class JogoSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = ['nome', 'preco']

class LojaSerializer(serializers.ModelSerializer):
    model = Loja
    fields = 'nome', 'endereco', 'telefone'
