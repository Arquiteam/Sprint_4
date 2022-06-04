from .logic import ServicioMentoriaLogic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def smentorias_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            smentoria_dto = ml.get_smentoria(id)
            smentoria = serializers.serialize('json', [smentoria_dto,])
            return HttpResponse(smentoria, 'application/json')
        else:
            smentorias_dto = ml.get_smentorias()
            smentorias = serializers.serialize('json', smentorias_dto)
            return HttpResponse(smentorias, 'application/json')

    if request.method == 'POST':
        smentoria_dto = ml.create_smentoria(json.loads(request.body))
        smentoria = serializers.serialize('json', [smentoria_dto,])
        return HttpResponse(smentoria, 'application/json')

@csrf_exempt
def smentoria_view(request, pk):
    if request.method == 'GET':
        smentoria_dto = ml.get_smentoria(pk)
        smentoria = serializers.serialize('json', [smentoria_dto,])
        return HttpResponse(smentoria, 'application/json')

    if request.method == 'PUT':
        smentoria_dto = ml.update_smentoria(pk, json.loads(request.body))
        smentoria = serializers.serialize('json', [smentoria_dto,])
        return HttpResponse(smentoria, 'application/json')

    if request.method == 'DELETE':
        smentoria_dto = ml.get_smentoria(pk)
        ml.delete_smentoria(pk)
        smentoria = serializers.serialize('json', [smentoria_dto,])
        return HttpResponse(smentoria, 'application/json')