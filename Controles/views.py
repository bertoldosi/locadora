from datetime import date

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Controles.forms import *
from .models import *

@login_required(login_url='login')
def index(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'index.html', locals())

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect(reverse_lazy('index'))
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', locals())

@login_required(login_url='login')
def cadastrar_cliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('editar_clientes'))
        else:
            HttpResponse('Deu errado!')
    return render(request, 'cadastrar_cliente.html', locals())

@login_required(login_url='login')
def cadastrar_veiculo(request):
    form = VeiculoForm()
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('editar_veiculos'))
        else:
            HttpResponse('Deu errado!')
    return render(request, 'cadastrar_veiculo.html', locals())

@login_required(login_url='login')
def editar_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'editar_veiculo.html', locals())
@login_required(login_url='login')
def editar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'editar_cliente.html', locals())

@login_required(login_url='login')
def editando_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    if form.is_valid():
        form.save()
        return redirect(reverse_lazy('editar_veiculos'))
    return render(request, 'listar_veiculo.html', locals())

@login_required(login_url='login')
def editando_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect(reverse_lazy('editar_clientes'))
    return render(request, 'listar_cliente.html', locals())

@login_required(login_url='login')
def lista_veiculo_id(request, id):
    veiculo = Veiculo.objects.get(id=id)
    return render(request, 'listar_veiculo.html', locals())

@login_required(login_url='login')
def lista_cliente_id(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'listar_cliente.html', locals())

@login_required(login_url='login')
def alugando_veiculo(request, id, id_cliente):
    veiculo = Veiculo.objects.get(id=id)
    clientes = Cliente.objects.all()
    request.session['cpf_cliente'] = id_cliente

    return render(request, 'alugando_veiculo.html', locals())

@login_required(login_url='login')
def buscando_cliente(request, id_veiculo, id_cliente):
    clientes = Cliente.objects.all()

    cliente = Cliente.objects.get(id=id_cliente)
    veiculo = Veiculo.objects.get(id=id_veiculo)
    aluguel = Aluguel(
        veiculo=veiculo,
        cliente=cliente)

    #mudar status
    carro = Veiculo.objects.get(id=aluguel.veiculo.id)
    carro.status_aluguel = '1'

    aluguel.dt_aluguel = date.today()


    form = AluguelForm(instance=aluguel)
    if request.method == 'POST':
        form = AluguelForm(request.POST, instance=aluguel)
        if form.is_valid():
            form.save()
            aluguel.save()
            carro.save()
            return redirect(reverse_lazy('index'))
    return render(request, 'buscando_cliente.html', locals())

@login_required(login_url='login')
def buscando_cliente_aluguel(request, id_veiculo, id_cliente):
    clientes = Cliente.objects.get(cpf=id_cliente)
    veiculo = Veiculo.objects.get(id=id_veiculo)
    request.session['cpf_cliente'] = id_cliente
    return render(request, 'buscando_cliente_aluguel.html', locals())

@login_required(login_url='login')
def alugados(request):
    alugados = Aluguel.objects.filter(status=1)
    return render(request, 'alugados.html', locals())

@login_required(login_url='login')
def historico(request):
    historico = Aluguel.objects.filter(status=0)

    return render(request, 'historico.html', locals())

@login_required(login_url='login')
def devolucao(request, id_veiculo, id_aluguel):
    aluguel = Aluguel.objects.get(id=id_aluguel)

    #mudar status
    carro = Veiculo.objects.get(id=id_veiculo)
    carro.status_aluguel = '0'

    taxa = 50

    #operação para calcular os dias alugados
    aluguel.dt_devolucao = date.today()
    dias = (aluguel.dt_devolucao-aluguel.dt_aluguel).days
    multa = (aluguel.dt_aluguel-aluguel.dt_devolucao).days

    #teste para saber se existe multa na entrega
    if multa <0:
        #transformando o numero de atrasos em positivo para realizar a operação.
        multa = multa*(-1)
        taxa = taxa*multa

        valor_total = (dias*aluguel.valor_aluguel)+taxa
        status_multa = taxa
    else:
        valor_total = (dias*aluguel.valor_aluguel)
        status_multa = 0

    aluguel.qtd_dias = dias
    aluguel.valor_total_aluguel = valor_total

    form = DevolucaoForm(instance=aluguel)
    if request.method == 'POST':
        form = DevolucaoForm(request.POST, instance=aluguel)
        if form.is_valid():
            aluguel.status = 0
            form.save()
            carro.save()
            aluguel.save()
            return redirect(reverse_lazy('alugados'))

    return render(request, 'devolucao.html', locals())