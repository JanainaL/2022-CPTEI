from django import forms

from cliente.models import Cliente
from funcionario.models import Funcionario
from servico.models import Servico
from veiculo.models import Veiculo


class ServicoListForm(forms.Form):
    SITUACAO_OPCOES = (
        ('T', '-----------'),
        ('A', 'Agendado'),
        ('R', 'Realizado'),
        ('C', 'Cancelado')
    )
    cliente = forms.ModelChoiceField(label='Cliente:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Cliente.objects.all(), required=False)

    funcionario = forms.ModelChoiceField(label='Funcionário:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Funcionario.objects.all(), required=False)

    veiculo = forms.ModelChoiceField(label='Veículo:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Veiculo.objects.all(), required=False)

    situacao = forms.ChoiceField(label='Situação:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), choices=SITUACAO_OPCOES, required=False)


class ServicoModelForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['horario', 'cliente', 'funcionario', 'veiculo', 'situacao', 'preco']
        widgets = {
            'horario': forms.DateTimeInput(
              attrs={'class': 'input', 'placeholder': 'Digite a hora do servico'}),
            'cliente': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione o nome do cliente'}),
            'funcionario': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione o nome do funcionário'}),
            'veiculo': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione o veículo'}),
            'situacao': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione a situação do atendimento'}),
            'preco': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione o preço do atendimento'}),
            'preco': forms.NumberInput(
                attrs={'class': 'input', 'type': 'number', 'placeholder': 'Digite o preço do serviço'}),
        }
