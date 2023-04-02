from rest_framework import viewsets
from carros.api import serializers
from carros import models

class CarrosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.CarrosSerializer
    queryset = models.Carros.objects.all()

class ClientesViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()