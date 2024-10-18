from django.contrib import admin
from apps.solicitudes.models import Solicitud, SolicitudServicio, Turno

# Register your models here.

@admin.register(Solicitud)
class AdminSolicitud(admin.ModelAdmin):
    pass

@admin.register(SolicitudServicio)
class AdminSolicitudServicio(admin.ModelAdmin):
    pass

@admin.register(Turno)
class AdminTurno(admin.ModelAdmin):
    pass
