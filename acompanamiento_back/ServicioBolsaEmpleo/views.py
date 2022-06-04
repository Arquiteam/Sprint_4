from .logic import ServicioBolsaEmpleoLogic as bel
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sboempleos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            sboempleo_dto = bel.get_sboempleo(id)
            sboempleo = serializers.serialize('json', [sboempleo_dto,])
            return HttpResponse(sboempleo, 'application/json')
        else:
            sboempleos_dto = bel.get_sboempleos()
            sboempleos = serializers.serialize('json', sboempleos_dto)
            return HttpResponse(sboempleos, 'application/json')

    if request.method == 'POST':
        sboempleo_dto = bel.create_sboempleo(json.loads(request.body))
        sboempleo = serializers.serialize('json', [sboempleo_dto,])
        return HttpResponse(sboempleo, 'application/json')

@csrf_exempt
def sboempleo_view(request, pk):
    if request.method == 'GET':
        sboempleo_dto = bel.get_sboempleo(pk)
        sboempleo = serializers.serialize('json', [sboempleo_dto,])
        return HttpResponse(sboempleo, 'application/json')

    if request.method == 'PUT':
        sboempleo_dto = bel.update_sboempleo(pk, json.loads(request.body))
        sboempleo = serializers.serialize('json', [sboempleo_dto,])
        return HttpResponse(sboempleo, 'application/json')

    if request.method == 'DELETE':
        sboempleo_dto = bel.get_sboempleo(pk)
        bel.delete_sboempleo(pk)
        sboempleo = serializers.serialize('json', [sboempleo_dto,])
        return HttpResponse(sboempleo, 'application/json')