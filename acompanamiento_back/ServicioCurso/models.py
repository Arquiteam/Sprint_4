from django.db import models
from django.db import models
from SucursalAcompa├▒amiento.models import SucursalAcompa├▒amiento

class ServicioCurso(models.Model):
    idText = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    numAsistencias = models.IntegerField(default = 0, null=False)
    sucursal = models.OneToOneField(SucursalAcompa├▒amiento, on_delete=models.CASCADE, null=True )
    
    def __str__(self):
        return '%s' % (self.descripcion)