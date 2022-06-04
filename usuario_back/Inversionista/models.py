from statistics import mode
from django.db import models
from Usuario.models import Usuario

class Inversionista(Usuario):
    estudiantes = models.ManyToManyField(to="Estudiante.Estudiante", related_name='est+')

    def __str__(self):
        return '{}'.format(self.nombreUsuario) 