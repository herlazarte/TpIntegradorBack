from django.db import models
from core.models import PersonaModelo

# Create your models here.


 #preguntar para despues consumir de una api
class Direccion(models.Model):
    calle=models.CharField(max_length=255)
    numero=models.CharField(max_length=20)#preguntar
    piso=models.CharField(max_length=10,null=True,blank=True)#para que el campo no sea obligatorio
    codigo_postal=models.CharField(max_length=10)#los codigos postales admiten letras tambien
    localidad=models.CharField(max_length=255)
    provincia=models.CharField(max_length=255)
    pais=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.calle} {self.numero}"

    

class Cliente(PersonaModelo):
    direccion=models.ManyToManyField(Direccion,default=None) 
    
    def __str__(self) -> str:
        return f"{self.nombre}"

class Profesional(PersonaModelo):
    direccion=models.ManyToManyField(Direccion,default=None)
    servicio_profesional=models.ManyToManyField('servicios.Servicio')

    def __str__(self) -> str:
        return f"{self.nombre}" 
    
    #creo para manejar la lista ManyToMany y despues usaerlo en el admin
    def Servicio(self):    
        return ', '.join([str(s) for s in self.servicio_profesional.all()])









