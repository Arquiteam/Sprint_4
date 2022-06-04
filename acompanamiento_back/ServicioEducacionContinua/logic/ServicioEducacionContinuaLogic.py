import sys
sys.path.append("..")
from ..models import ServicioEducacionContinua

def get_sedcontinuas():
    sedcontinuas = ServicioEducacionContinua.objects.all()
    return sedcontinuas

def get_sedcontinua(var_pk):
    sedcontinua = ServicioEducacionContinua.objects.get(pk=var_pk)
    return sedcontinua

def update_sedcontinua(var_pk, new_var):
    sedcontinua = get_sedcontinua(var_pk)
    sedcontinua.idText = new_var["id"]
    sedcontinua.descripcion = new_var["descripcion"]
    sedcontinua.numAsistencias = new_var["numAsistencias"]
    sedcontinua.sucursal = new_var["sucursal"]
    sedcontinua.save()
    return sedcontinua

def create_sedcontinua(var):
    sedcontinua = ServicioEducacionContinua(
                                    idText=var["idText"],
                                    descripcion=var["descripcion"],
                                    numAsistencias=var["numAsistencias"],
                                    sucursal=var["sucursal"])
    sedcontinua.save()
    return sedcontinua

def delete_sedcontinua(var_pk):
    sedcontinua = get_sedcontinua(var_pk)
    sedcontinua.delete()