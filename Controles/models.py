from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100, )
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=20)
    cpf = models.CharField('CPF', max_length=20)
    rg = models.CharField('RG', max_length=20)
    estado_rg = models.CharField('Estado RG', max_length=2)
    rua = models.CharField('Rua', max_length=150)
    numero = models.IntegerField('Número')
    cidade = models.CharField('Cidade', max_length=150)
    estado = models.CharField('Estado', max_length=2)
    cep = models.CharField('CEP',max_length=20)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.CharField('Marca', max_length=100)
    modelo = models.CharField('Modelo', max_length=100)
    renavam = models.CharField('Renavam', max_length=20)
    placa = models.CharField('Placa', max_length=10)
    numero_chassis = models.CharField('Número do chassis', max_length=20)
    ano_fabricacao = models.IntegerField('Ano de fabricação')
    cor = models.CharField('Cor', max_length=50)
    cidade = models.CharField('Cidade', max_length=150)
    estado = models.CharField('Estado', max_length=2)
    valor_diaria = models.IntegerField('Valor da diária')
    status_aluguel = models.CharField('Status', max_length=10)


    def __str__(self):
        return self.marca

class Aluguel(models.Model):
    dt_aluguel = models.DateField('Data do aluguel')
    dt_prazo = models.DateField('Prazo')
    dt_devolucao = models.DateField('Data da devolução', blank=True, null=True)
    valor_aluguel = models.IntegerField('Valor do aluguel')
    km_saida = models.IntegerField('Km de saida')
    km_devolucao = models.IntegerField('Km de devolução', blank=True, null=True)
    status = models.IntegerField(default=1)
    qtd_dias = models.IntegerField(blank=True, null=True)
    valor_total_aluguel = models.IntegerField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if self.veiculo.status_aluguel == '0':
    #         veiculo = Veiculo.objects.get(id=self.veiculo.id)
    #         veiculo.status_aluguel = '1'
    #         veiculo.save()
    #
    #     super(Aluguel, self).save(*args, **kwargs)

