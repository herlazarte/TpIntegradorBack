from django import forms # type: ignore
from apps.usuarios.models import Cliente, Profesional

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']


