# Generated by Django 4.0.4 on 2022-05-31 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_funcionario'),
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='funcionario',
        ),
        migrations.AddField(
            model_name='servico',
            name='refferring_funcionario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='clientes.funcionario', verbose_name='Funcionário'),
            preserve_default=False,
        ),
    ]
