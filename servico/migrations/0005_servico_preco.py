# Generated by Django 4.1.1 on 2023-01-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0004_remove_servico_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=1, help_text='Preço do serviço', max_digits=5, verbose_name='Preço'),
            preserve_default=False,
        ),
    ]