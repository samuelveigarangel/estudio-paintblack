from django import forms
from tempus_dominus.widgets import DatePicker


class FiltroDateForm(forms.Form):
    Agenda = forms.DateField(widget=DatePicker(), required=False)
