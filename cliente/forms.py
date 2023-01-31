from django import forms
from .models import Cliente

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'fone', 'cpf', 'cnpj']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do cliente'}),
            'endereco': forms.TextInput(
                 attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o endereço do cliente'}),
            'fone': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o telefone do cliente'}),
            'cpf': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o CPF do cliente'}),
            'cnpj': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o CNPJ do cliente'}),

        }

    error_messages = {
        'nome': {'required': 'O nome do cliente é um campo obrigatório'},
        'endereço': {'required': 'O endereço do cliente é um campo obrigatório'},
        'fone': {'required': 'O telefone do cliente é um campo obrigatório'},
    }
