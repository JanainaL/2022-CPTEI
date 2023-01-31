from django.db import models
from stdimage import StdImageField

from home.models import Pessoa


class Funcionario(Pessoa):
    cpf = models.CharField('CPF', max_length=11, help_text='Cpf')
    foto = StdImageField('Foto', upload_to='pessoas', variations={'thumbnail': {'width': 100, 'height': 100,
                                                                                'crop': True}}, delete_orphans=True,
                         null=True, blank=True)


    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']

    def __str__(self):
        return super().nome

