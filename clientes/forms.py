from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome_cliente', 'telefone', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})

    def clean(self):
        super().clean()
        email = self.cleaned_data.get('email')

        if Cliente.objects.filter(email=email).exists():
            self.add_error('email', 'Email já existe')