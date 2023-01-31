from django import forms

from .models import Veiculo

class VeiculoModelForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'placa', 'cor', 'qtdPneu']
        widgets = {
            'modelo': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o modelo do veiculo'}),
            'placa': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a placa do veiculo'}),
            'cor': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digitea cor do veiculo'}),
            'qtdPneu': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a quantidade do veiculo'}),
        }
