# Generated by Django 4.0.4 on 2022-05-31 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_funcionario', models.CharField(max_length=70)),
                ('cargo_funcionario', models.CharField(max_length=30)),
            ],
        ),
    ]