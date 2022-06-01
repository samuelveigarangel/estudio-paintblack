from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from clientes.models import Cliente
from .models import Servico
from .forms import ServicoForms, EditarServicoForms


class ProcurarClienteList(ListView):
    """Class que herda ListView e retorna os clientes cadastrados."""
    model = Cliente
    template_name = 'servico/listar_clientes_list.html'
    paginate_by = 10

    def get_queryset(self):
        txt_pesquisa = self.request.GET.get('pesquisa')


        if txt_pesquisa:
            cliente = Cliente.objects.filter(nome_cliente__icontains=txt_pesquisa.strip()).order_by('nome_cliente')
        else:
            cliente = Cliente.objects.all().order_by('nome_cliente')

        return cliente


class AssociarServicoDetail(CreateView):
    """Class que herda CreateView e cria um formulário para associar um serviço a determinado cliente.
    Ex: Associar um corte de cabelo ou tatuagem para cliente X.
    """
    model = Cliente
    template_name = 'servico/criar_servico_ou_editar_detail.html'
    form_class = ServicoForms
    success_url = reverse_lazy('servico:listar-clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = get_object_or_404(Cliente, pk=self.kwargs['pk'])
        context['cliente'] = obj
        return context

    def form_valid(self, form):
        '''valor_servico = form.cleaned_data['valor_servico']
        if form.cleaned_data['modo_pagamento']:
            form.instance.valor_servico = int(valor_servico)*0.966'''
        form.instance.cliente_id = self.kwargs['pk']
        return super().form_valid(form)


class ListarServico(ListView):
    """Class que recebe ListView responsável por listar todos os servicos associados a determinado cliente.
    """
    model = Servico
    template_name = 'servico/listar_servicos.html'
    paginate_by = 10

    def get_queryset(self):
        servicos = Servico.objects.filter(cliente__nome_cliente=self.kwargs.get('cliente')).order_by('data_servico')
        return servicos


class EditarServico(UpdateView):
    """Class que herda UpdateView e edita os serviços associados a determinado cliente."""
    login_url = 'pages:home'
    form_class = EditarServicoForms
    template_name = 'servico/criar_servico_ou_editar_detail.html'
    success_url = reverse_lazy('servico:listar-clientes')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk') or self.request.GET.get('pk') or None
        obj = get_object_or_404(Servico, pk=pk)
        return obj


class HistoricoCliente(ListView):
    """Class que herda Listview e lista todos os serviços associado a determinado cliente."""
    model = Servico
    template_name = 'servico/historico_cliente.html'
    paginate_by = 6

    def get_queryset(self):
        historico = Servico.objects.filter(cliente__nome_cliente=self.kwargs.get('cliente')).order_by('data_servico')
        return historico


def ExcluirServico(request, pk):
    """Função que recebe o id do serviço e exclui."""
    servicos = get_object_or_404(Servico, pk=pk)
    parm_cliente = servicos.cliente
    servicos.delete()
    return redirect('servico:listar-servico', parm_cliente)


'''def ExcluiCliente(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    cliente.delete()
    return redirect('pages:home')'''