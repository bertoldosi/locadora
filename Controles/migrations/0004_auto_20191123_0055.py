# Generated by Django 2.2.6 on 2019-11-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Controles', '0003_auto_20191122_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=20, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=20, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=20, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=20, verbose_name='Telefone'),
        ),
    ]
