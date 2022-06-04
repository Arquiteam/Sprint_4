import sys
sys.path.append("..")
from ..models import ServicioCurso

def get_scursos():
    scursos = ServicioCurso.objects.all()
    return scursos

def get_scurso(var_pk):
    scurso = ServicioCurso.objects.get(pk=var_pk)
    return scurso

def update_scurso(var_pk, new_var):
    scurso = get_scurso(var_pk)
    scurso.descripcion = new_var["descripcion"]
    scurso.numAsistencias = new_var["numAsistencias"]
    scurso.sucursal = new_var["sucursal"]
    scurso.save()
    return scurso

def create_scurso(var):
    scurso = ServicioCurso(
                                    idText=var["idText"],
                                    descripcion=var["descripcion"],
                                    numAsistencias=var["numAsistencias"],
                                    sucursal=var["sucursal"])
    scurso.save()
    return scurso

def delete_scurso(var_pk):
    scurso = get_scurso(var_pk)
    scurso.delete()

def asistir(self):
    self.numAsistencias = self.numAsistencias+1
    return self