from django.http import HttpResponse
from django.shortcuts import render
from .models import Amiibo
from .serializers import AmiiboSerializer

from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import viewsets

class AmiiboViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Amiibo.objects.all()
    serializer_class = AmiiboSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"

