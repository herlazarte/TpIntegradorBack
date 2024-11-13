
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Profesional
from apps.profesional.forms import ProfesionalForm


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