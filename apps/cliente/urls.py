from django.urls import path
from .views import ListaClientesView, AltaClientesView, DashboardClientesView

urlpatterns = [
    path('listado_clientes/', ListaClientesView.as_view(), name='listado_clientes'),
    path('alta_cliente/', AltaClientesView.as_view(), name='alta_cliente'),
    path('', DashboardClientesView.as_view(), name='dashboard_cliente'),
]
