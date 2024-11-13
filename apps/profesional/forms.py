from django import forms # type: ignore
from apps.profesional.models import Profesional

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre', 'apellido', 'email', 'telefono','localidad', 'provincia', 'servicio_profesional', 'tipo_servicio']
    
#agregar uno no asociado a un modelo