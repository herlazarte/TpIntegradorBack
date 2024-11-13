from django import forms
from apps.cliente.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido','NombreDeUsuario','contra' ,'email', 'telefono', 'calle', 'numero', 'piso', 'codigo_postal', 'localidad', 'provincia']