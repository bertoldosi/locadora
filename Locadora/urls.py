"""Locadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Controles.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('', logar_usuario, name="login"),

    path('cadastrar_cliente', cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar_veiculo', cadastrar_veiculo, name='cadastrar_veiculo'),

    path('editar_veiculos', editar_veiculos, name='editar_veiculos'),
    path('editar_clientes', editar_clientes, name='editar_clientes'),

    path('editando_veiculo/<id>', editando_veiculo, name='editando_veiculo'),
    path('editando_cliente/<id>', editando_cliente, name='editando_cliente'),

    path('listar_veiculo/<int:id>', lista_veiculo_id, name='listar_veiculo'),
    path('listar_cliente/<int:id>', lista_cliente_id, name='listar_cliente'),

    path('alugando_veiculo/<id>/<id_cliente>', alugando_veiculo, name='alugando_veiculo'),

    path('alugados', alugados, name='alugados'),
    path('historico', historico, name='historico'),
    path('devolucao/<id_veiculo>/<id_aluguel>', devolucao, name='devolucao'),

    path('buscando_cliente/<id_veiculo>/<id_cliente>', buscando_cliente, name='buscando_cliente'),
    path('buscando_cliente_aluguel/<id>/<id_cliente>', buscando_cliente_aluguel, name='buscando_cliente_aluguel')

]
