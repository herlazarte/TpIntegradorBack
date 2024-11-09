from django.urls import path
from .views import ListaClientesView , ListaProfesionalesView

urlpatterns = [
    path('profesionales/', ListaProfesionalesView.as_view(), name='listado_profesionales'),
    path('clientes/', ListaClientesView.as_view(), name='listado_clientes'),
]

