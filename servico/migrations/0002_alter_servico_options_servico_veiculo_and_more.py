# Generated by Django 4.1.1 on 2023-01-25 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_options_alter_cliente_cnpj_and_more'),
        ('veiculo', '0003_alter_veiculo_options'),
        ('funcionario', '0002_alter_funcionario_options_alter_funcionario_foto'),
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servico',
            options={'ordering': ['horario'], 'verbose_name': 'Servico', 'verbose_name_plural': 'Serviços'},
        ),
        migrations.AddField(
            model_name='servico',
            name='veiculo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='veiculo.veiculo', verbose_name='Placa do veículo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servico',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario', verbose_name='Funcionário'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='horario',
            field=models.DateTimeField(verbose_name='Horário'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='situacao',
            field=models.CharField(choices=[('A', 'Agendado'), ('R', 'Realizado'), ('C', 'Cancelado')], default='A', max_length=15, verbose_name='Situação'),
        ),
    ]
