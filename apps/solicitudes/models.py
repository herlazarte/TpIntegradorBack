from django.db import models

# Create your models here.
class Solicitud(models.Model):
    cliente=models.ForeignKey('usuarios.Cliente', on_delete=models.CASCADE)
    fecha_solicitud=models.DateTimeField(auto_now_add=True) #fecha y hora exactas cuando se crea la solicitud

#consultar la logica de tabla intermedia
class SolicitudServicio(models.Model):
    solicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    profesional_servicio=models.ForeignKey('usuarios.Profesional', on_delete=models.CASCADE)

class Turno(models.Model):
    solicitud_servicio=models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)
    fecha_turno=models.DateTimeField()
    estado_turno=models.CharField(max_length=50)#preguntar para que por prederetminado haya turno ya establecidos