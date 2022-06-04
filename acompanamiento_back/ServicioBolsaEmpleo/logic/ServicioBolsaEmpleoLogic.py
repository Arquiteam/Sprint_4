import sys
sys.path.append("..")
from ..models import ServicioBolsaEmpleo

def get_sboempleos():
    sboempleos = ServicioBolsaEmpleo.objects.all()
    return sboempleos

def get_sboempleo(var_pk):
    sboempleo = ServicioBolsaEmpleo.objects.get(pk=var_pk)
    return sboempleo

def update_sboempleo(var_pk, new_var):
    sboempleo = get_sboempleo(var_pk)
    sboempleo.idText = new_var["id"]
    sboempleo.descripcion = new_var["descripcion"]
    sboempleo.numAsistencias = new_var["numAsistencias"]
    sboempleo.sucursal = new_var["sucursal"]
    sboempleo.save()
    return sboempleo

def create_sboempleo(var):
    sboempleo = ServicioBolsaEmpleo(
                                    idText=var["idText"],
                                    descripcion=var["descripcion"],
                                    numAsistencias=var["numAsistencias"],
                                    sucursal=var["sucursal"])
    sboempleo.save()
    return sboempleo

def delete_sboempleo(var_pk):
    sboempleo = get_sboempleo(var_pk)
    sboempleo.delete()