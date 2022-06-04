from Inversionista.models import Inversionista
from .logic import InversionistaLogic as il
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def inversionistas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            inversionista_dto = il.get_inversionista(id)
            inversionista = serializers.serialize('json', [inversionista_dto,])
            return HttpResponse(inversionista, 'application/json')
        else:   
            inversionistas_dto = il.get_inversionistas()
            inversionistas = serializers.serialize('json', inversionistas_dto)
            return HttpResponse(inversionistas, 'application/json')

    if request.method == 'POST':
        inversionista_dto = il.create_inversionista(json.loads(request.body))
        inversionista = serializers.serialize('json', [inversionista_dto,])
        return HttpResponse(inversionista, 'application/json')

@csrf_exempt
def inversionista_view(request, pk):
    if request.method == 'GET':
        inversionista_dto = il.get_inversionista(pk)
        inversionista = serializers.serialize('json', [inversionista_dto,])
        return HttpResponse(inversionista, 'application/json')

    if request.method == 'PUT':
        inversionista_dto = il.update_inversionista(pk, json.loads(request.body))
        inversionista = serializers.serialize('json', [inversionista_dto,])
        return HttpResponse(inversionista, 'application/json')

    if request.method == 'DELETE':
        inversionista_dto = il.get_inversionista(pk)
        il.delete_inversionista(pk)
        inversionista = serializers.serialize('json', [inversionista_dto,])
        return HttpResponse(inversionista, 'application/json')