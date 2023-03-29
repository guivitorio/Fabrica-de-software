from rest_framework import viewsets
from serializer import JogoSerialiazer
from .models import Loja
from .models import Jogo

class JogoViewSet(viewset.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewset.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = JogoSerializer