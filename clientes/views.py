from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

from .forms import ClienteForm
from .models import Cliente


class CadastroCreate(CreateView):
    template_name = 'cliente/cadastro.html'
    form_class = ClienteForm
    success_url = reverse_lazy('pages:home')


class DadosCliente(DetailView):
    model = Cliente
    template_name = 'cliente/dados_cliente.html'
