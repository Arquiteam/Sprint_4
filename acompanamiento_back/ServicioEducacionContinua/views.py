from .logic import ServicioEducacionContinuaLogic as ecl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sedcontinuas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            sedcontinua_dto = ecl.get_sedcontinua(id)
            sedcontinua = serializers.serialize('json', [sedcontinua_dto,])
            return HttpResponse(sedcontinua, 'application/json')
        else:
            sedcontinuas_dto = ecl.get_sedcontinuas()
            sedcontinuas = serializers.serialize('json', sedcontinuas_dto)
            return HttpResponse(sedcontinuas, 'application/json')

    if request.method == 'POST':
        sedcontinua_dto = ecl.create_sedcontinua(json.loads(request.body))
        sedcontinua = serializers.serialize('json', [sedcontinua_dto,])
        return HttpResponse(sedcontinua, 'application/json')

@csrf_exempt
def sedcontinua_view(request, pk):
    if request.method == 'GET':
        sedcontinua_dto = ecl.get_sedcontinua(pk)
        sedcontinua = serializers.serialize('json', [sedcontinua_dto,])
        return HttpResponse(sedcontinua, 'application/json')

    if request.method == 'PUT':
        sedcontinua_dto = ecl.update_sedcontinua(pk, json.loads(request.body))
        sedcontinua = serializers.serialize('json', [sedcontinua_dto,])
        return HttpResponse(sedcontinua, 'application/json')

    if request.method == 'DELETE':
        sedcontinua_dto = ecl.get_sedcontinua(pk)
        ecl.delete_sedcontinua(pk)
        sedcontinua = serializers.serialize('json', [sedcontinua_dto,])
        return HttpResponse(sedcontinua, 'application/json')