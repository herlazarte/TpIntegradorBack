from django.db import models
from core.models import PersonaModelo

# Create your models here.


 #preguntar para despues consumir de una api
# class Direccion(models.Model):
#     calle=models.CharField(max_length=255)
#     numero=models.CharField(max_length=20)#preguntar
#     piso=models.CharField(max_length=10,null=True,blank=True)#para que el campo no sea obligatorio
#     codigo_postal=models.CharField(max_length=10)#los codigos postales admiten letras tambien
#     localidad=models.CharField(max_length=255)
#     provincia=models.CharField(max_length=255)
#     pais=models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.calle} {self.numero}"

    

class Cliente(PersonaModelo):
    calle=models.CharField(max_length=255, default="")
    numero=models.CharField(max_length=20, default="")
    piso=models.CharField(max_length=10,null=True,blank=True)
    codigo_postal=models.CharField(max_length=10, default="")
    localidad=models.CharField(max_length=255, default="")
    provincia=models.CharField(max_length=255, default="")
    
    def __str__(self) -> str:
        return f"{self.nombre}"

class Profesional(PersonaModelo):
    localidad=models.CharField(max_length=255, default="")
    provincia=models.CharField(max_length=255, default="")
    servicio_profesional=models.ForeignKey('servicios.Servicio', on_delete=models.CASCADE, default=None, null=True, blank=True)
    tipo_servicio=models.ForeignKey('servicios.TipoServicio', on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.servicio_profesional}" 
    
    #creo para manejar la lista ManyToMany y despues usaerlo en el admin
    









