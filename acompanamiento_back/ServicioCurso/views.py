from .logic import ServicioCursoLogic as cl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def scursos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            scurso_dto = cl.get_scurso(id)
            scurso = serializers.serialize('json', [scurso_dto,])
            return HttpResponse(scurso, 'application/json')
        else:
            scursos_dto = cl.get_scursos()
            scursos = serializers.serialize('json', scursos_dto)
            return HttpResponse(scursos, 'application/json')

    if request.method == 'POST':
        scurso_dto = cl.create_scurso(json.loads(request.body))
        scurso = serializers.serialize('json', [scurso_dto,])
        return HttpResponse(scurso, 'application/json')

@csrf_exempt
def scurso_view(request, pk):
    if request.method == 'GET':
        scurso_dto = cl.get_scurso(pk)
        scurso = serializers.serialize('json', [scurso_dto,])
        return HttpResponse(scurso, 'application/json')

    if request.method == 'PUT':
        scurso_dto = cl.update_scurso(pk, json.loads(request.body))
        scurso = serializers.serialize('json', [scurso_dto,])
        return HttpResponse(scurso, 'application/json')

    if request.method == 'DELETE':
        scurso_dto = cl.get_scurso(pk)
        cl.delete_scurso(pk)
        scurso = serializers.serialize('json', [scurso_dto,])
        return HttpResponse(scurso, 'application/json')