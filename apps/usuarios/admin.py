from django.contrib import admin
from apps.usuarios.models import Cliente,Profesional,Direccion

# Register your models here.
@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    pass
@admin.register(Profesional)
class AdminProfesional(admin.ModelAdmin):
    pass
@admin.register(Direccion)
class AdminDireccion(admin.ModelAdmin):
    pass