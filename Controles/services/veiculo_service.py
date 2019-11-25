from ..models import *


def listar_veiculo_id(id):
    veiculo = Veiculo.objects.get(id=id)
    return veiculo

def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.sexo = cliente_novo.sexo
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.email = cliente_novo.email
    cliente.profissao = cliente_novo.profissao
    cliente.save(force_update=True)