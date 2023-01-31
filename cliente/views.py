from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from cliente.forms import ClienteModelForm
from cliente.models import Cliente

class ClienteView(ListView):
    model = Cliente
    template_name = 'clientes.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClienteView, self).get_queryset(* args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        paginator = Paginator(qs, 3)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

class ClienteAddView(CreateView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ClienteUpDateView(UpdateView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_apagar.html'
    success_url = reverse_lazy('clientes')

