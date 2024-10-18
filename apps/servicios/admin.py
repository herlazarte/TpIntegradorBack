from django.contrib import admin
from apps.servicios.models import Servicio, TipoServicio, ProfesionalServicio

# Register your models here.
@admin.register(Servicio)
class AdminServicio(admin.ModelAdmin):
    pass
@admin.register(TipoServicio)
class AdminTipoServicio(admin.ModelAdmin):
    pass
@admin.register(ProfesionalServicio)
class AdminProfesionalServicio(admin.ModelAdmin):
    pass
