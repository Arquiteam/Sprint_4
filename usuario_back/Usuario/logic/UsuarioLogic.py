from genericpath import exists
import sys
sys.path.append("..")
from ..models import Usuario

def get_usuarios():
    usuarios = Usuario.objects.all()
    return usuarios

def get_usuario(var_pk):
    usuario = Usuario.objects.get(pk=var_pk)
    return usuario

def update_usuario(var_pk, new_var):
    usuario = get_usuario(var_pk)
    usuario.nombreUsuario = new_var["nombreUsuario"]
    usuario.correo = new_var["correo"]
    usuario.contrasena = new_var["contrasena"]
    usuario.save()
    return usuario

def create_usuario(var):
    user = Usuario.objects.filter(pk=var["correo"]).exists()
    if user==False: 
        usuario = Usuario(
                      nombreUsuario=var["nombreUsuario"],
                      correo=var["correo"])
        usuario.set_password(   var["password"])
        usuario.save()
        return usuario

def delete_usuario(var_pk):
    usuario = get_usuario(var_pk)
    usuario.delete()