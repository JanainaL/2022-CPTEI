from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .forms import VeiculoModelForm
from .models import Veiculo


class VeiculosView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(VeiculosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(placa__icontains=buscar)
    

        paginator = Paginator(qs, 3)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

class VeiculoAddView(CreateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')


class VeiculoUpDateView(UpdateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'veiculo_apagar.html'
    success_url = reverse_lazy('veiculos')
