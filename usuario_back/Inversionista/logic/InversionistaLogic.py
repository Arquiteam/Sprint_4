import sys
from xml.dom import InvalidStateErr
sys.path.append("..")
from ..models import Inversionista

def get_inversionistas():
    inversionistas = Inversionista.objects.all()
    return inversionistas

def get_inversionista(var_pk):
    inversionista = Inversionista.objects.get(pk=var_pk)
    return inversionista

def update_inversionista(var_pk, new_var):
    inversionista = get_inversionista(var_pk)
    inversionista.nombreUsuario = new_var["nombreUsuario"]
    inversionista.correo = new_var["correo"]
    inversionista.set_password(new_var["password"])
    inversionista.estudiantes = new_var["estudiantes"]
    inversionista.save()
    return inversionista

def create_inversionista(var):
    inv = Inversionista.objects.filter(pk=var["correo"]).exists() 
    if inv==False:
        inversionista = Inversionista(
                                nombreUsuario=var["nombreUsuario"],
                                correo=var["correo"])
        inversionista.set_password(var["password"])
        inversionista.save()
        return inversionista
def delete_inversionista(var_pk):
    inversionista = get_inversionista(var_pk)
    inversionista.delete()