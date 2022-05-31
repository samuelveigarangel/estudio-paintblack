from django.contrib import admin
from .models import Cliente, Funcionario

@admin.register(Cliente)
class Clientes(admin.ModelAdmin):
    list_display = ['id', 'nome_cliente', 'telefone']
    list_display_links = ['nome_cliente']
    list_per_page = 10

@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    list_display = ['nome_funcionario',]

