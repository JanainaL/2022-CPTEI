# Generated by Django 4.1.1 on 2023-01-25 23:37

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nome'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(blank=True, help_text='CNPJ para pessoa jurídica', max_length=11, null=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(blank=True, help_text='CPF para pessoa física', max_length=11, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='pessoas', variations={'thumbnail': {'crop': True, 'heigth': 100, 'width': 100}}, verbose_name='Foto'),
        ),
    ]
