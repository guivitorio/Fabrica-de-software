# CRUD Django REST Framework

CRUD é uma sigla para Create, Read, Update e Delete, que são as quatro operações básicas de um sistema de gerenciamento de banco de dados. O Django REST Framework é uma poderosa ferramenta para construir APIs RESTful (Representational State Transfer) em Django.

Este guia tem como objetivo fornecer uma visão geral sobre como implementar operações CRUD em Django REST Framework.

# Requisitos

. Python 3.x
. Django 3.x
. Django REST Framework 3.x

# Configurando o projeto

Primeiramente, crie um projeto Django
  $ django-admin startproject myproject
  
Agora, crie uma aplicação:
  $ cd myproject
  $ python manage.py startapp myapp
  
  Adicione a aplicação myapp ao INSTALLED_APPS no arquivo settings.py do projeto:
  
  ## myproject/settings.py

INSTALLED_APPS = [
    # ...
    'myapp',
    'rest_framework',
    # ...
]

# Criando o modelo

Crie um modelo simples para armazenar dados de uma entidade. Neste exemplo, criaremos um modelo chamado Product.

## myapp/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

Não se esqueça de rodar as migrações para criar a tabela no banco de dados:

$ python manage.py makemigrations
$ python manage.py migrate

# Criando o Serializador

O próximo passo é criar um serializador que converte o modelo em formato JSON e vice-versa. Em outras palavras, o serializador define como os dados serão serializados e desserializados.

# myapp/serializers.py

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')
# Criando as Views

Em seguida, criaremos as views que fornecerão as operações CRUD.

## myapp/views.py

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    A classe ProductViewSet herda da classe ModelViewSet, que fornece as operações CRUD básicas para o modelo Product.
    
    # Configurando as URLs
    
    Finalmente, precisamos configurar as URLs para acessar as views. Isso pode ser feito através do arquivo urls.py do aplicativo.
    
    # myapp/urls.py

  from django.urls import path, include
  from rest_framework import routers
  from .views import ProductViewSet

  router = routers.DefaultRouter()
  router.register(r'products', ProductViewSet)

  urlpatterns = [
      path('', include(router.urls)),
  ]
Isso irá mapear as seguintes URLs:

 ![image](https://user-images.githubusercontent.com/90806903/229326356-ac432ed4-591f-40e4-a428-66116aeffefd.png)

