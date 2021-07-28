from django.http import HttpResponse
from django.shortcuts import render
from .models import Amiibo

def list_amiibos(request):
    context = {'amiibos_list': Amiibo.objects.all()}
    return render(request, 'amiibos/amiibos_list.html', context)

def list_amiibos_byCharacter(request, character):
    context = {'amiibos_byCharacter_list': Amiibo.objects.get(character=character)}
    return render(request, 'amiibos/amiibos_byCharacter_list.html', context)

def list_amiibos_byGame(request, game):
    context = {'amiibos_byGame_list': Amiibo.objects.get(gameSeries=game)}
    return render(request, 'amiibos/amiibos_byGame_list.html', context)

def list_amiibos_byName(request, name):
    context = {'amiibos_byName_list': Amiibo.objects.get(name=name)}
    return render(request, 'amiibos/amiibos_byName_list.html', context)