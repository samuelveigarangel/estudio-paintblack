from django.urls import path

from .views import ProcurarClienteList, AssociarServicoDetail
from .views import ExcluirServico
from .views import EditarServico, ListarServico
from .views import HistoricoCliente





app_name = 'servico'

urlpatterns = [
    path('listar-clientes/', ProcurarClienteList.as_view(), name='listar-clientes'),
    path('criar-servico/<int:pk>/', AssociarServicoDetail.as_view(), name='criar-servico'),

    path('editar/editar-servico/<int:pk>/', EditarServico.as_view(), name='editar-servico'),
    path('editar/listar-servico/<str:cliente>/', ListarServico.as_view(), name='listar-servico'),

    path('historico/<str:cliente>/', HistoricoCliente.as_view(), name='historico-cliente'),

    path('editar/listar-servico/excluir/<int:pk>/', ExcluirServico, name='excluir-servico'),
    #path('exclui/<int:pk>/', ExcluiCliente, name='excluir-cliente'),
]
