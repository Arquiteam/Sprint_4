from Estudiante.models import Estudiante
from .logic import EstudianteLogic as el
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def estudiantes_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            estudiante_dto = el.get_estudiante(id)
            estudiante = serializers.serialize('json', [estudiante_dto,])
            return HttpResponse(estudiante, 'application/json')
        else:
            estudiantes_dto = el.get_estudiantes()
            estudiantes = serializers.serialize('json', estudiantes_dto)
            return HttpResponse(estudiantes, 'application/json')

    if request.method == 'POST':
        estudiante_dto = el.create_estudiante(json.loads(request.body))
        estudiante = serializers.serialize('json', [estudiante_dto,])
        return HttpResponse(estudiante, 'application/json')

@csrf_exempt
def estudiante_view(request, pk):
    if request.method == 'GET':
        estudiante_dto = el.get_estudiante(pk)
        estudiante = serializers.serialize('json', [estudiante_dto,])
        return HttpResponse(estudiante, 'application/json')

    if request.method == 'PUT':
        estudiante_dto = el.update_estudiante(pk, json.loads(request.body))
        estudiante = serializers.serialize('json', [estudiante_dto,])
        return HttpResponse(estudiante, 'application/json')

    if request.method == 'DELETE':
        estudiante_dto = el.get_estudiante(pk)
        el.delete_estudiante(pk)
        estudiante = serializers.serialize('json', [estudiante_dto,])
        return HttpResponse(estudiante, 'application/json')