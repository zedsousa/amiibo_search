from django.http import HttpResponse
from django.shortcuts import render
from .models import Amiibo

def list_amiibos(request):
    context = {'amiibos_list': Amiibo.objects.all()}
    return render(request, 'amiibos/amiibos_list.html', context)

def list_amiibos_byId(request, id):
    context = {'amiibos_list': Amiibo.objects.all().get(id=id)}
    return render(request, 'amiibos/amiibos_byId_list.html', context)

def list_amiibos_byCharacter(request, character):
    context = {'amiibos_list': Amiibo.objects.all().filter(character=character)}
    return render(request, 'amiibos/amiibos_byCharacter_list.html', context)

def list_amiibos_byGame(request, game):
    context = {'amiibos_list': Amiibo.objects.all().filter(gameSeries=game)}
    return render(request, 'amiibos/amiibos_byGame_list.html', context)

def list_amiibos_byName(request, name):
    context = {'amiibos_list': Amiibo.objects.all().filter(name=name)}
    return render(request, 'amiibos/amiibos_byName_list.html', context)

def list_amiibos_byType(request, type):
    context = {'amiibos_list': Amiibo.objects.all().filter(type=type)}
    return render(request, 'amiibos/amiibos_byType_list.html', context)