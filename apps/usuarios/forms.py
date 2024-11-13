from django import forms # type: ignore
from apps.usuarios.models import Cliente, Profesional

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'calle', 'numero', 'piso', 'codigo_postal', 'localidad', 'provincia']


class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre', 'apellido', 'email', 'telefono','localidad', 'provincia', 'servicio_profesional', 'tipo_servicio']
    
#agregar uno no asociado a un modelo