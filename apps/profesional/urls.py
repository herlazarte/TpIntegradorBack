from django.urls import path
from .views import ListaProfesionalesView, AltaProfesionalView

urlpatterns = [
    path('lista_profesionales/', ListaProfesionalesView.as_view(), name='lista_profesionales'),
    path('alta_profesional/', AltaProfesionalView.as_view(), name='alta_profesional'),
]

