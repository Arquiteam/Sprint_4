import sys
sys.path.append("..")
from ..models import ServicioMentoria

def get_smentorias():
    smentorias = ServicioMentoria.objects.all()
    return smentorias

def get_smentoria(var_pk):
    smentoria = ServicioMentoria.objects.get(pk=var_pk)
    return smentoria

def update_smentoria(var_pk, new_var):
    smentoria = get_smentoria(var_pk)
    smentoria.idText = new_var["id"]
    smentoria.descripcion = new_var["descripcion"]
    smentoria.numAsistencias = new_var["numAsistencias"]
    smentoria.sucursal = new_var["sucursal"]
    smentoria.save()
    return smentoria

def create_smentoria(var):
    smentoria = ServicioMentoria(
                                idText=var["idText"],
                                descripcion=var["descripcion"],
                                numAsistencias=var["numAsistencias"],
                                sucursal=var["sucursal"])
    smentoria.save()
    return smentoria

def delete_smentoria(var_pk):
    smentoria = get_smentoria(var_pk)
    smentoria.delete()