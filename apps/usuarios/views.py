
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Cliente, Profesional
from apps.usuarios.forms import ClienteForm, ProfesionalForm



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


class AltaProfesionalView(CreateView):
    model = Profesional
    form_class = ProfesionalForm
    template_name = 'alta_profesional.html'
    success_url = '/alta_profesional/'


class ListaProfesionalesView(TemplateView):
    template_name = 'listado_profesionales.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesionales'] = Profesional.objects.all()
        return context


class HomeView(TemplateView):
    template_name = "base.html"