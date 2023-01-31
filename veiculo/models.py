from django.db import models

class Veiculo(models.Model):
    modelo = models.CharField('Modelo', max_length=10, help_text='Modelo do Veículo')
    placa = models.CharField('Placa', max_length=10, help_text='Placa do Veículo')
    cor = models.CharField('Cor', max_length=10, help_text='Cor do Veículo')
    qtdPneu = models.DecimalField('Quantidade de Pneus', max_digits=1, decimal_places=0, help_text='Quantidade de Pneus')


    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['modelo']

    def __str__(self):
        return f"{self.placa} {self.modelo} {self.cor}"
