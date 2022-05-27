from django import forms
from tempus_dominus.widgets import DateTimePicker
from datetime import datetime

from .models import Servico


class ServicoForms(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ['funcionario', 'lista_servico', 'valor_servico', 'data_servico', 'marcar_servico', 'modo_pagamento']

        widgets = {'data_servico': DateTimePicker(options={'minDate': datetime.today().strftime('%m-%d-%Y')}),
                 }


class EditarServicoForms(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ['funcionario', 'lista_servico', 'valor_servico', 'data_servico', 'marcar_servico']

        widgets={'data_servico': DateTimePicker()}
