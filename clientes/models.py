from django.db import models
from django.urls import reverse

from datetime import datetime


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=70, verbose_name='Nome Completo')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    email = models.EmailField(unique=True, blank=True, verbose_name='E-mail')
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome_cliente

    def get_absolute_url(self):
        return reverse('clientes:dados-cliente', kwargs={'pk': self.pk})
