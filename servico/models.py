from django.db import models
from users.models import User
from django.urls import reverse

from clientes.models import Cliente, Funcionario


class Servico(models.Model):

    choices_services = [('1', 'Tatuagem'), ('2', 'Corte de Cabelo')]

    refferring_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, verbose_name='Funcionário')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lista_servico = models.CharField(max_length=1, choices=choices_services, blank=False, null=False, verbose_name='Lista de serviços')
    valor_servico = models.DecimalField(default='', max_digits=7, decimal_places=2, verbose_name='Valor do serviço')
    data_servico = models.DateTimeField(null=False, verbose_name='Data do serviço')
    marcar_servico = models.BooleanField(default=True)
    modo_pagamento = models.BooleanField(default=False, verbose_name='Cartão de crédito')

    def get_absolute_url(self):
        return reverse('clientes:dados-cliente', kwargs={'pk': self.cliente_id})
