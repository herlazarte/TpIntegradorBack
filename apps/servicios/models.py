from django.db import models

# Create your models here.

class TipoServicio(models.Model):
    nombre_tipo_servicio=models.CharField(max_length=255)
    precio=models.FloatField()#preguntar para que se tenga un formato para el precio

class Servicio(models.Model):
    nombre_servicio=models.CharField(max_length=255)
    tipo_servicio=models.ForeignKey(TipoServicio, on_delete=models.CASCADE)

class ProfesionalServicio(models.Model):
    profesional=models.ForeignKey('usuarios.Profesional', on_delete=models.CASCADE)
    servicio=models.ForeignKey(Servicio, on_delete=models.CASCADE)