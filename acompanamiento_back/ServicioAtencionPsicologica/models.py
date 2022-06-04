from django.db import models
from SucursalAcompañamiento.models import SucursalAcompañamiento

class ServicioAtencionPsicologica(models.Model):
    idText = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    numAsistencias = models.IntegerField(default = 0, null=False)
    sucursal = models.OneToOneField(SucursalAcompañamiento, on_delete=models.CASCADE, null=True )

    def __str__(self):
        return '%s' % (self.descripcion)