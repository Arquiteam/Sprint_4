import sys
sys.path.append("..")
from ..models import ServicioAtencionPsicologica

def get_satpsicologicas():
    satpsicologicas = ServicioAtencionPsicologica.objects.all()
    return satpsicologicas

def get_satpsicologica(var_pk):
    satpsicologica = ServicioAtencionPsicologica.objects.get(pk=var_pk)
    return satpsicologica

def update_satpsicologica(var_pk, new_var):
    satpsicologica = get_satpsicologica(var_pk)
    satpsicologica.idText = new_var["id"]
    satpsicologica.descripcion = new_var["descripcion"]
    satpsicologica.numAsistencias = new_var["numAsistencias"]
    satpsicologica.sucursal = new_var["sucursal"]
    satpsicologica.save()
    return satpsicologica

def create_satpsicologica(var):
    satpsicologica = ServicioAtencionPsicologica(
                                                idText=var["idText"],
                                                descripcion=var["descripcion"],
                                                numAsistencias=var["numAsistencias"],
                                                sucursal=var["sucursal"])
    satpsicologica.save()
    return satpsicologica

def delete_satpsicologica(var_pk):
    satpsicologica = get_satpsicologica(var_pk)
    satpsicologica.delete()

def asistir(self):
    self.numAsistencias = self.numAsistencias+1
    return satpsicologica