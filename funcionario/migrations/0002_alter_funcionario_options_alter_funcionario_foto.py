# Generated by Django 4.1.1 on 2023-01-25 23:37

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'ordering': ['nome'], 'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='pessoas', variations={'thumbnail': {'crop': True, 'height': 100, 'width': 100}}, verbose_name='Foto'),
        ),
    ]
