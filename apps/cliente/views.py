
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Cliente
from apps.cliente.forms import ClienteForm

class ListaClientesView(TemplateView):
    template_name = 'listado_clientes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context

class AltaClientesView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'alta_cliente.html'
    success_url = '/alta_cliente/'

class DashboardClientesView(TemplateView):
    template_name = 'dashboard_cliente.html'

class HomeView(TemplateView):
    template_name = "base.html"