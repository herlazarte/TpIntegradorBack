from django.urls import path
from .views import ListaClientesView, AltaClientesView

urlpatterns = [
    path('clientes/', ListaClientesView.as_view(), name='listado_clientes'),
    path('alta_cliente/', AltaClientesView.as_view(), name='alta_cliente'),
]
