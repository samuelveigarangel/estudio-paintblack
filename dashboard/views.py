from django.views.generic import ListView
from django.db.models import Q, Count, Sum
from django.shortcuts import render
from django.http import JsonResponse
from datetime import date
import locale

from servico.models import Servico


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def faturamentomes(request):
    """Função que retorna um Json o faturamento de cada mês no ano"""
    labels = ['Janeiro', 'fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    data = [None] * 12

    for i in range(1, 13):
        valor = []
        queryset = list(Servico.objects.values_list('valor_servico', flat=True).filter((Q(data_servico__month=i) & Q(marcar_servico=True) & Q(data_servico__year=date.today().year))))

        if queryset:
            for x in queryset:
                valor.append(float(x))

            data[i-1] = sum(valor)

    #print(data)
    return JsonResponse(data={'labels': labels,
                              'data': data,
                              })


def clienteatendidosmes(request):
    """Função que retorna  um Json com o total de atedimento de corte de cabelo e tatuagem"""
    total_cabelo = len(Servico.objects.filter((Q(data_servico__month=date.today().month) & Q(marcar_servico=True) & Q(lista_servico=2) & Q(data_servico__year=date.today().year))))
    total_tatuagem = len(Servico.objects.filter((Q(data_servico__month=date.today().month) & Q(marcar_servico=True) & Q(lista_servico=1))))
    data = {'total_cabelo': total_cabelo,
            'total_tatuagem': total_tatuagem,
            }
    return JsonResponse(data)


def totalestudiomes(request):
    """Funçao que retornar um Json com o total de faturamento do estúdio do mês"""
    valor = []
    queryset = list(Servico.objects.values_list('valor_servico', flat=True).filter(
        (Q(data_servico__month=date.today().month) & Q(marcar_servico=True) & Q(data_servico__year=date.today().year))))

    if queryset:
        for x in queryset:
            valor.append(float(x))

    valor_total = (sum(valor)/2)
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    data = {'valor_mes': locale.currency(valor_total, grouping=True)}

    return JsonResponse(data)


class TotalFuncionarioList(ListView):
    """Função que retorna um QuerySet com o pagamento de cada funcionário no mês"""
    template_name = 'dashboard/dashboard.html'
    model = Servico

    def get_queryset(self):
        queryset = Servico.objects.values('refferring_funcionario__nome_funcionario').annotate(preco_total=Sum('valor_servico')).annotate(total_servico=Count('lista_servico')).order_by('refferring_funcionario__nome_funcionario').filter(
        (Q(data_servico__month=date.today().month) & Q(marcar_servico=True) & Q(data_servico__year=date.today().year)))
        print(queryset)
        return queryset
