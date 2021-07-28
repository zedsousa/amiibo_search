from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen
import json
import requests

from rest_framework import viewsets
#from amiibo_search.models import Amiibo

#class AmiiboViewSet(viewsets.ModelViewSet):
#    queryset = Amiibo.objects.all().order_by('-idAmiibo')

def index(request):
    #response = requests.get("https://teste")
    #data = response.json()
    return HttpResponse("TESTE")