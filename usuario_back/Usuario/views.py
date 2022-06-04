import sys
from typing import ItemsView
from urllib.request import Request
sys.path.append("..")
from Inversionista.models import Inversionista
from Estudiante.models import Estudiante
from .models import UserManager as um
from ServicioCurso.models import ServicioCurso
from ServicioMentoria.models import ServicioMentoria
from ServicioEducacionContinua.models import ServicioEducacionContinua
from ServicioBolsaEmpleo.models import ServicioBolsaEmpleo
from ServicioAtencionPsicologica.models import ServicioAtencionPsicologica
from django.db.models import Model

import Inversionista.logic.InversionistaLogic as il
import Estudiante.logic.EstudianteLogic as el
import SucursalAcompañamiento.logic.SucursalAcompañamientoLogic as scl
from .forms import UsuarioFormRegistro, UsuarioFormIngreso
from .logic import UsuarioLogic as ul
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .models import *

@csrf_exempt
def usuarios_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            usuario_dto = ul.get_usuario(id)
            usuario = serializers.serialize('json', [usuario_dto,])
            return HttpResponse(usuario, 'application/json')
        else:
            usuarios_dto = ul.get_usuarios()
            usuarios = serializers.serialize('json', usuarios_dto)
            return HttpResponse(usuarios, 'application/json')

    if request.method == 'POST':
        usuario_dto = ul.create_usuario(json.loads(request.body))
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')

@csrf_exempt
def usuario_view(request, pk):
    if request.method == 'GET':
        usuario_dto = ul.get_usuario(pk)
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')

    if request.method == 'PUT':
        usuario_dto = ul.update_usuario(pk, json.loads(request.body))
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')

    if request.method == 'DELETE':
        usuario_dto = ul.get_usuario(pk)
        ul.delete_usuario(pk)
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')

def registro(request):
    if request.method == "POST":
        form = UsuarioFormRegistro(request.POST)
        if form.is_valid():
            print("Valido")
            ul.create_usuario(form.cleaned_data)    
            role = form.cleaned_data["role"]
            print(role)
            if role == "IN":
                inv = il.create_inversionista(form.cleaned_data)
                ests = el.get_estudiantes()
                print(ests)
                for e in ests:
                    print(e)
                    inv.estudiantes.add(e)
                return redirect('usuario:ingreso')
            else: 
                form.cleaned_data["universidad"] = "Universidad"
                est = el.create_estudiante(form.cleaned_data)
                for inv in il.get_inversionistas():
                    inv.estudiantes.add(est)
                    return redirect('usuario:ingreso')
        else:
            print("invalido")
    form = UsuarioFormRegistro()
    return render(request, "registro.html", {'form':form })

def ingreso(request):
    if request.method == "POST":
        form = UsuarioFormIngreso(request.POST)
        if form.is_valid():
            print("Valido")
            role = form.cleaned_data["role"]
            if role == "ES":
                correo = form.cleaned_data["correo"]
                ppassword = form.cleaned_data["password"]
                if(el.get_estudiantes().filter(password=ppassword)!=None):
                    return redirect('usuario:estudiante', pk=correo)
                
            else: 
                correo = form.cleaned_data["correo"]
                ppassword = form.cleaned_data["password"]
                if(il.get_inversionistas().filter(password=ppassword)!=None):
                    return redirect('usuario:inversionista', pk=correo)
        else:
            print("invalido")
    form = UsuarioFormIngreso()
    return render(request, "ingreso.html", {'form':form })

def estudiante(request, pk):
    estudiante = el.get_estudiante(pk)
    sucursal = estudiante.sucursal

    sAtPsicologica = estudiante.sucursal.sAtPsicologica.numAsistencias
    sBoEmpleo  = estudiante.sucursal.sBoEmpleo.numAsistencias
    sCurso = estudiante.sucursal.sCurso.numAsistencias
    sMentoria = estudiante.sucursal.sMentoria.numAsistencias
    sEdContinua = estudiante.sucursal.sEdContinua.numAsistencias

    if  'asistirsAtPsicologica' in request.POST:
        ServicioAtencionPsicologica.objects.filter(id=estudiante.sucursal.sAtPsicologica.id).update(numAsistencias=estudiante.sucursal.sAtPsicologica.numAsistencias+1)
        return render(request, "estudianteInicio.html", {"sAtPsicologica":estudiante.sucursal.sAtPsicologica.numAsistencias+1 , 
                                                        "sBoEmpleo":sBoEmpleo , 
                                                        "sCurso": sCurso, 
                                                        "sMentoria":sMentoria , 
                                                        "sEdContinua":sEdContinua })          
    if 'asistirssBoEmpleo' in request.POST:
        ServicioBolsaEmpleo.objects.filter(id=estudiante.sucursal.sBoEmpleo.id).update(numAsistencias=estudiante.sucursal.sBoEmpleo.numAsistencias+1)
        return render(request, "estudianteInicio.html", {"sAtPsicologica":sAtPsicologica , 
                                                        "sBoEmpleo":estudiante.sucursal.sBoEmpleo.numAsistencias+1 , 
                                                        "sCurso": sCurso, 
                                                        "sMentoria":sMentoria , 
                                                        "sEdContinua":sEdContinua })
    if 'asistirsCurso' in request.POST:
        ServicioCurso.objects.filter(id=estudiante.sucursal.sCurso.id).update(numAsistencias=estudiante.sucursal.sCurso.numAsistencias+1)
        return render(request, "estudianteInicio.html", {"sAtPsicologica":sAtPsicologica , 
                                                        "sBoEmpleo":sBoEmpleo , 
                                                        "sCurso": estudiante.sucursal.sCurso.numAsistencias+1, 
                                                        "sMentoria":sMentoria , 
                                                        "sEdContinua":sEdContinua })
    if 'asistirsMentoria' in request.POST:
        ServicioMentoria.objects.filter(id=estudiante.sucursal.sMentoria.id).update(numAsistencias=estudiante.sucursal.sMentoria.numAsistencias+1)
        return render(request, "estudianteInicio.html", {"sAtPsicologica":sAtPsicologica , 
                                                        "sBoEmpleo":sBoEmpleo , 
                                                        "sCurso": sCurso, 
                                                        "sMentoria":estudiante.sucursal.sMentoria.numAsistencias+1 , 
                                                        "sEdContinua":sEdContinua })
    if 'asistirsEdContinua' in request.POST:
        ServicioEducacionContinua.objects.filter(id=estudiante.sucursal.sEdContinua.id).update(numAsistencias=estudiante.sucursal.sEdContinua.numAsistencias+1)
        return render(request, "estudianteInicio.html", {"sAtPsicologica":sAtPsicologica, 
                                                        "sBoEmpleo":sBoEmpleo , 
                                                        "sCurso": sCurso, 
                                                        "sMentoria":sMentoria , 
                                                        "sEdContinua":estudiante.sucursal.sEdContinua.numAsistencias+1  }) 
         
    return render(request, "estudianteInicio.html", {"sAtPsicologica":sAtPsicologica , "sBoEmpleo":sBoEmpleo , "sCurso": sCurso, "sMentoria":sMentoria , "sEdContinua":sEdContinua })          

def inversionista(request, pk):
    inversionista = il.get_inversionista(pk) 
    contsAtPsicologica = 0
    contsBoEmpleo = 0
    contsEdContinua = 0
    contsSMentoria = 0
    contsCurso = 0

    for est in inversionista.estudiantes.all():
        contsAtPsicologica += est.sucursal.sAtPsicologica.numAsistencias
        contsBoEmpleo +=  est.sucursal.sBoEmpleo.numAsistencias
        contsEdContinua += est.sucursal.sEdContinua.numAsistencias
        contsSMentoria += est.sucursal.sMentoria.numAsistencias
        contsCurso += est.sucursal.sCurso.numAsistencias

    print(contsAtPsicologica)
    
    promsAtPsicologica = contsAtPsicologica/len(inversionista.estudiantes.all())
    promsBoEmpleo = contsBoEmpleo/len(inversionista.estudiantes.all())
    promsCurso = contsCurso/len(inversionista.estudiantes.all())
    promsMentoria = contsSMentoria/len(inversionista.estudiantes.all()) 
    promsEdContinua = contsEdContinua/len(inversionista.estudiantes.all())

    return render(request, "inversionistaInicio.html", {"promsAtPsicologica": promsAtPsicologica, 
                                                "promsBoEmpleo": promsBoEmpleo, 
                                                "promsCurso": promsCurso, 
                                                "promsMentoria": promsMentoria, 
                                                "promsEdContinua": promsEdContinua})