from django.db import models

# Create your models here.


 #preguntar para despues consumir de una api
class Direccion(models.Model):
    # latitud=models.FloatField()
    # longitud=models.FloatField()
    calle=models.CharField(max_length=255)
    numero=models.CharField(max_length=20)#preguntar
    piso=models.CharField(max_length=10,null=True,blank=True)#para que el campo no sea obligatorio
    codigo_postal=models.CharField(max_length=10)#los codigos postales admiten letras tambien
    localidad=models.CharField(max_length=255)
    provincia=models.CharField(max_length=255)
    pais=models.CharField(max_length=255)

    

class Cliente(models.Model):
    nombre=models.CharField(max_length=255)
    email=models.EmailField(unique=True) #para que el email que se registre sea unico y no se repita 
    contra=models.CharField(max_length=255)#hacer logica para que tenga caracteres especiales,May.Min,Num
    telefono=models.CharField(max_length=15)
    direccion=models.ForeignKey(Direccion, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.nombre}"

class Profesional(models.Model):
    nombre=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    telefono=models.CharField(max_length=15)
    contra=models.CharField(max_length=255)
    direccion=models.ForeignKey(Direccion, on_delete=models.CASCADE)
    servicio_profesional=models.ForeignKey('servicios.Servicio', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombre} {self.servicio_profesional}"









