from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen
import json
import requests


def index(request):
    return HttpResponse("TESTE")