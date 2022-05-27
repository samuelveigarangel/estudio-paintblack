from django.contrib import admin
from .models import Servico


@admin.register(Servico)
class Servico(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'funcionario', 'lista_servico', 'valor_servico', 'data_servico']
    list_display_links = ['cliente']
    search_fields = ['id', 'cliente__nome_cliente']
    list_per_page = 10