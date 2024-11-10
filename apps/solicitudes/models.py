from django.db import models
from django.utils import timezone

# Create your models here.
class Solicitud(models.Model):
    cliente=models.ForeignKey('usuarios.Cliente', on_delete=models.CASCADE)
    fecha_solicita=models.DateTimeField()
    tipo_servicio=models.ForeignKey('servicios.Servicio', on_delete=models.CASCADE)
    profesional_servicio=models.ForeignKey('usuarios.Profesional', on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return f"{self.cliente}"

class Turno(models.Model):
    ESTADOS_TURNOS = {
        ('A','Aceptado'),
        ('R','Rechazado'),
        ('EN','En transcurso'),
    }
    solicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE, default=None)
    fecha_Asignacion_Turno=models.DateTimeField()
    estado_turno=models.CharField(max_length=3, choices=ESTADOS_TURNOS)#preguntar para que por prederetminado haya turno ya establecidos

    def __str__(self) -> str:
        return f"{self.fecha_turno} {self.estado_turno}"