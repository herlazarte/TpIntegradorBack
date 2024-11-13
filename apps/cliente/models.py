from django.db import models

from core.models import PersonaModelo

# Create your models here.
class Cliente(PersonaModelo):
    calle=models.CharField(max_length=255, default="")
    numero=models.CharField(max_length=20, default="")
    piso=models.CharField(max_length=10,null=True,blank=True)
    codigo_postal=models.CharField(max_length=10, default="")
    localidad=models.CharField(max_length=255, default="")
    provincia=models.CharField(max_length=255, default="")
    
    def __str__(self) -> str:
        return f"{self.nombre}"