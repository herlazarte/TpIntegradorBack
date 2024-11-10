
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from apps.usuarios.forms import ClienteForm
from .models import Cliente, Profesional


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
    success_url = '/listado_clientes/'




class ListaProfesionalesView(TemplateView):
    template_name = 'listado_profesionales.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesionales'] = Profesional.objects.all()
        return context
