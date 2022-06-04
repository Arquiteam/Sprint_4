from logging.handlers import SYSLOG_UDP_PORT
import sys

sys.path.append("..")
from ..models import Estudiante
from SucursalAcompañamiento.logic import SucursalAcompañamientoLogic as sl

def get_estudiantes():
    estudiantes = Estudiante.objects.all()
    return estudiantes

def get_estudiante(var_pk):
    estudiante = Estudiante.objects.get(pk=var_pk)
    return estudiante

def update_estudiante(var_pk, new_var):
    estudiante = get_estudiante(var_pk)
    estudiante.nombreUsuario = new_var["nombreUsuario"]
    estudiante.correo = new_var["correo"]
    estudiante.set_password(new_var["password"])
    estudiante.universidad = new_var["universidad"]
    estudiante.sucursal = sl.create_sucursalacompañamiento()
    estudiante.save()
    return estudiante

def create_estudiante(var):
    est = Estudiante.objects.filter(pk=var["correo"]).exists()
    if est == False:
        sucursalInstancia = sl.create_sucursalacompañamiento({
        "numAsistencias": 0
        })
        estudiante = Estudiante(
                                nombreUsuario=var["nombreUsuario"],
                                correo=var["correo"],
                                universidad=var["universidad"],
                                sucursal=sucursalInstancia)
        estudiante.set_password(var["password"])
        estudiante.save()
        return estudiante

def delete_estudiante(var_pk):
    estudiante = get_estudiante(var_pk)
    estudiante.delete()

def asistir(self):
    self.contrasena = "xd"