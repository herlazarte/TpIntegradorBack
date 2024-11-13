from django.db import models

# Create your models here.

class TipoServicio(models.Model):
    nombre_tipo_servicio=models.CharField(max_length=255)
    precio=models.FloatField()#preguntar para que se tenga un formato para el precio

    #ver tambien para que aparezca el campo precio
    def __str__(self) -> str:
        return f"{self.nombre_tipo_servicio} "
    
    

class Servicio(models.Model):
    nombre_servicio=models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.nombre_servicio}"


#preguntar tabla de muchos muchos, difinir la logica

#ver para que aparezca tipo de servicio,solo se visualiza el profesional con el servicio
class ProfesionalServicio(models.Model):
    profesional = models.ForeignKey('profesional.Profesional', on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    tipo_servicio=models.ForeignKey(TipoServicio, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return f"{self.profesional} Servicios {self.servicio} Tipo servicio {self.tipo_servicio}"
