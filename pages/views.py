from django.views.generic import ListView
from datetime import date, datetime
from django.db.models import Q

from .forms import FiltroDateForm
from servico.models import Servico


class TaskList(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        data_pesquisa = self.request.GET.get('Agenda')

        if data_pesquisa:
            # Transformar data em formato americano
            data_aux = data_pesquisa.split()
            d = datetime.strptime(data_aux[0], "%d/%m/%Y")
            data_us = d.strftime('%Y-%m-%d')
            print(data_us)
            queryset = {'tatuagens': Servico.objects.filter(
                (Q(data_servico__date=data_us) & Q(lista_servico=1))).order_by('data_servico'),
                        'cortes_cabelo': Servico.objects.filter(
                            (Q(data_servico__date=data_us) & Q(lista_servico=2))).order_by('data_servico')
                        }
            print(queryset)
        else:
            queryset = {
                'tatuagens': Servico.objects.filter((Q(data_servico__date=date.today()) & Q(lista_servico=1))).order_by(
                    'data_servico'),
                'cortes_cabelo': Servico.objects.filter(
                    (Q(data_servico__date=date.today()) & Q(lista_servico=2))).order_by('data_servico')
                }
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        context['form'] = FiltroDateForm()
        return context
