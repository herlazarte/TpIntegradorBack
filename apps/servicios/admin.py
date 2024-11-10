from django.contrib import admin
from apps.servicios.models import Servicio, TipoServicio, ProfesionalServicio

# Register your models here.
@admin.register(Servicio)
class AdminServicio(admin.ModelAdmin):
    list_display = ['nombre_servicio','tipo_servicio']

@admin.register(TipoServicio)
class AdminTipoServicio(admin.ModelAdmin):
    list_display = ['nombre_tipo_servicio','precio']
@admin.register(ProfesionalServicio)
class AdminProfesionalServicio(admin.ModelAdmin):
    list_display = ['profesional','servicio','tipo_servicio']
