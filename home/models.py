from django.db import models
from stdimage import StdImageField

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome Completo')
    fone = models.CharField('Telefone', max_length=15, help_text='Número do telefone')
    endereco = models.CharField('Endereço', max_length=100, help_text='Endereço Completo')
    foto = StdImageField('Foto', upload_to='pessoas', variations={'thumbnail': {'width': 100, 'heigth': 100,
                                                                                'crop': True}}, delete_orphans=True,
                         null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

