from .logic import ServicioAtencionPsicologicaLogic as apl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def satpsicologicas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            satpsicologica_dto = apl.get_satpsicologica(id)
            satpsicologica = serializers.serialize('json', [satpsicologica_dto,])
            return HttpResponse(satpsicologica, 'application/json')
        else:
            satpsicologicas_dto = apl.get_satpsicologicas()
            satpsicologicas = serializers.serialize('json', satpsicologicas_dto)
            return HttpResponse(satpsicologicas, 'application/json')

    if request.method == 'POST':
        satpsicologica_dto = apl.create_satpsicologica(json.loads(request.body))
        satpsicologica = serializers.serialize('json', [satpsicologica_dto,])
        return HttpResponse(satpsicologica, 'application/json')

@csrf_exempt
def satpsicologica_view(request, pk):
    if request.method == 'GET':
        satpsicologica_dto = apl.get_satpsicologica(pk)
        satpsicologica = serializers.serialize('json', [satpsicologica_dto,])
        return HttpResponse(satpsicologica, 'application/json')

    if request.method == 'PUT':
        satpsicologica_dto = apl.update_satpsicologica(pk, json.loads(request.body))
        satpsicologica = serializers.serialize('json', [satpsicologica_dto,])
        return HttpResponse(satpsicologica, 'application/json')

    if request.method == 'DELETE':
        satpsicologica_dto = apl.get_satpsicologica(pk)
        apl.delete_satpsicologica(pk)
        satpsicologica = serializers.serialize('json', [satpsicologica_dto,])
        return HttpResponse(satpsicologica, 'application/json')