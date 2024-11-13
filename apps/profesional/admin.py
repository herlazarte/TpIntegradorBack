from django.contrib import admin
from apps.profesional.models import Profesional

# Register your models here.    
   

@admin.register(Profesional)
class AdminProfesional(admin.ModelAdmin):
    #creo para manejar la lista ManyToMany y despues usarla en el list_display
    
    list_display = ['nombre','servicio_profesional','apellido', 'email']

    
# @admin.register(Direccion)
# class AdminDireccion(admin.ModelAdmin):
#     pass