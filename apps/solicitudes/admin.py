from django.contrib import admin
from apps.solicitudes.models import Solicitud, Turno

# Register your models here.

@admin.register(Solicitud)
class AdminSolicitud(admin.ModelAdmin):
    list_display = ['cliente', 'tipo_servicio', 'profesional_servicio', 'fecha_solicita']
@admin.register(Turno)
class AdminTurno(admin.ModelAdmin):
    pass
