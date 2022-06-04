from django.db import models
from Usuario.models import Usuario
from SucursalAcompañamiento.models import SucursalAcompañamiento


class Estudiante(Usuario):
    universidad = models.CharField(max_length=150, null=True)
    sucursal = models.OneToOneField(SucursalAcompañamiento, on_delete=models.SET_NULL, related_name='+', default=None, null=True )

    def __str__(self):
        return '{}'.format(self.nombreUsuario)  