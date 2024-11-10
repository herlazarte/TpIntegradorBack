from django.urls import path
from .views import ListaClientesView , ListaProfesionalesView, AltaClientesView, AltaProfesionalView

urlpatterns = [
    path('profesionales/', ListaProfesionalesView.as_view(), name='listado_profesionales'),
    path('clientes/', ListaClientesView.as_view(), name='listado_clientes'),
    path('alta_cliente/', AltaClientesView.as_view(), name='alta_cliente'),
    path('alta_profesional/', AltaProfesionalView.as_view(), name='alta_profesional')
]

