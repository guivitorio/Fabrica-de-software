from django.contrib import admin
from .models import Jogo, Loja

class JogosAdmin(admin.ModelAdmin):
    list_display = ('nome','preco')
    
admin.site.register(Jogo, JogosAdmin)

class lojaAdmin(admin.ModelAdmin):
    list_displayy = ('nome','endereco', 'telefone')
    
admin.site.register(Loja, lojaAdmin)


