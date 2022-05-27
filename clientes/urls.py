from .views import CadastroCreate, DadosCliente
from django.urls import path

app_name = 'clientes'

urlpatterns = [
    path('', CadastroCreate.as_view(), name='cadastro'),
    path('dados-cliente/<int:pk>/', DadosCliente.as_view(), name='dados-cliente'),
]
