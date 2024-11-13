from django.contrib import admin
from apps.usuarios.models import Cliente,Profesional

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
   

@admin.register(Profesional)
class AdminProfesional(admin.ModelAdmin):
    #creo para manejar la lista ManyToMany y despues usarla en el list_display
    
    list_display = ['nombre','servicio_profesional','apellido', 'email']

    
# @admin.register(Direccion)
# class AdminDireccion(admin.ModelAdmin):
#     pass