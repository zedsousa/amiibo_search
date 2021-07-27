from django.http import HttpResponse
from django.shortcuts import render
from .models import Amiibo

def list_amiibos(request):
    context = {'amiibos_list': Amiibo.objects.all()};
    return render(request, 'amiibos/amiibos_list.html', context)    