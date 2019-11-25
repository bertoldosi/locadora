from django import forms
from Controles.models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        exclude = ['km_devolucao', 'cliente', 'veiculo', 'status', 'dt_aluguel', 'dt_devolucao','valor_total_aluguel', 'qtd_dias']

class DevolucaoForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        exclude = ['dt_aluguel', 'dt_prazo', 'valor_aluguel', 'km_saida', 'cliente', 'veiculo', 'status', 'dt_devolucao']

class Devolucao_veiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['status_aluguel']