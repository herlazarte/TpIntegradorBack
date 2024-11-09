from django.db import models

class PersonaModelo(models.Model):
    class Meta:
        abstract=True
    
    nombre=models.CharField(max_length=255)
    email=models.EmailField(unique=True) #para que el email que se registre sea unico y no se repita 
    contra=models.CharField(max_length=255)#hacer logica para que tenga caracteres especiales,May.Min,Num
    telefono=models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return f"{self.nombre}"