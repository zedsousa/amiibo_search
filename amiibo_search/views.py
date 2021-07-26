from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen
import json
import requests

def index(request):
    #response = requests.get("https://teste")
    #data = response.json()
    return HttpResponse("TESTE")