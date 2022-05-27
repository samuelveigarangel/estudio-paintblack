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

    total_cabelo = len(Servico.objects.filter((Q(data_servico__month=date.today().month) & Q(marcar_servico=True) & Q(lista_servico=2) & Q(data_servico__year=date.today().year))))
    total_tatuagem = len(Servico.objects.filter((Q(data_servico__month=date.today().month) & Q(marcar_servico=True) & Q(lista_servico=1))))
    data = {'total_cabelo': total_cabelo,
            'total_tatuagem': total_tatuagem,
            }
    return JsonResponse(data)


def totalestudiomes(request):
    valor = []
    queryset = list(Servico.objects.values_list('valor_servico', flat=True).filter(
        (Q(data_servico__month=date.today().month) & Q(marcar_servico=True) & Q(data_servico__year=date.today().year))))

    if queryset:
        for x in queryset:
            valor.append(float(x))

    valor_total = (sum(valor)/2)
    locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

    data = {'valor_mes': locale.currency(valor_total, grouping=True)}

    return JsonResponse(data)


class TotalFuncionarioList(ListView):
    template_name = 'dashboard/dashboard.html'
    model = Servico

    def get_queryset(self):
        queryset = Servico.objects.values('funcionario__username').annotate(preco_total=Sum('valor_servico')).annotate(total_servico=Count('lista_servico')).order_by('funcionario__username').filter(
        (Q(data_servico__month=date.today().month) & Q(marcar_servico=True) & Q(data_servico__year=date.today().year)))
        print(queryset)
        return queryset
