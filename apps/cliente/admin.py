from django.contrib import admin

from apps.cliente.models import Cliente

# Register your models here.
@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    # se debera buscar por mas de un campo a eleccion
    # se debera poder filtrar 
    # se debera poder ordenar
    list_display = ['nombre','apellido', 'email']
    search_fields = ['nombre','apellido', 'email']
    list_filter = ['nombre','apellido', 'email']
    ordering = ['nombre','apellido', 'email']