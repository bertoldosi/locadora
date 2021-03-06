# Generated by Django 2.1.3 on 2019-12-03 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_aluguel', models.DateField(verbose_name='Data do aluguel')),
                ('dt_prazo', models.DateField(verbose_name='Prazo')),
                ('dt_devolucao', models.DateField(verbose_name='Data da devolução')),
                ('valor_aluguel', models.IntegerField(verbose_name='Valor do aluguel')),
                ('km_saida', models.IntegerField(verbose_name='Km de saida')),
                ('km_devolucao', models.IntegerField(verbose_name='Km de devolução')),
                ('status', models.IntegerField(default=1)),
                ('qtd_dias', models.IntegerField()),
                ('valor_total_aluguel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('estado_rg', models.CharField(max_length=2, verbose_name='Estado RG')),
                ('rua', models.CharField(max_length=150, verbose_name='Rua')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(max_length=20, verbose_name='CEP')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('renavam', models.CharField(max_length=20, verbose_name='Renavam')),
                ('placa', models.CharField(max_length=10, verbose_name='Placa')),
                ('numero_chassis', models.CharField(max_length=20, verbose_name='Número do chassis')),
                ('ano_fabricacao', models.IntegerField(verbose_name='Ano de fabricação')),
                ('cor', models.CharField(max_length=50, verbose_name='Cor')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('valor_diaria', models.IntegerField(verbose_name='Valor da diária')),
                ('status_aluguel', models.CharField(max_length=10, verbose_name='Status')),
            ],
        ),
        migrations.AddField(
            model_name='aluguel',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Controles.Cliente'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Controles.Veiculo'),
        ),
    ]
