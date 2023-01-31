from django import forms
from .models import Funcionario

class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'endereco', 'fone', 'foto']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do funcionario'}),
            'cpf': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o cpf do funcionario'}),
            'endereco': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o endereco do funcionario'}),
            'fone': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o telefone do funcionario'}),
            'foto': forms.FileInput(
                attrs={'class': 'input', 'type': 'file'}),
        }
