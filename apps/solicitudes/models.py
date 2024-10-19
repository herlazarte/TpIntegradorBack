from django.db import models

# Create your models here.
class Solicitud(models.Model):
    cliente=models.ForeignKey('usuarios.Cliente', on_delete=models.CASCADE)
    #definir formato de la fecha
    fecha_solicitud=models.DateTimeField() #fecha y hora exactas cuando se crea la solicitud
    tipo_servicio=models.ForeignKey('servicios.Servicio', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.cliente} {self.fecha_solicitud} {self.tipo_servicio}"

#consultar la logica de tabla intermedia
class SolicitudServicio(models.Model):
    solicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    profesional_servicio=models.ForeignKey('usuarios.Profesional', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.solicitud} {self.profesional_servicio}"

class Turno(models.Model):
    solicitud_servicio=models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)
    fecha_turno=models.DateTimeField()
    estado_turno=models.CharField(max_length=50)#preguntar para que por prederetminado haya turno ya establecidos

    def __str__(self) -> str:
        return f"{self.solicitud_servicio} {self.fecha_turno} {self.estado_turno}"