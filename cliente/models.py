from django.db import models

from home.models import Pessoa


class Cliente(Pessoa):
    cpf = models.CharField('CPF', max_length=11, help_text='CPF para pessoa física', blank=True, null=True)
    cnpj = models.CharField('CNPJ', max_length=11, help_text='CNPJ para pessoa jurídica', blank=True, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return super().nome

