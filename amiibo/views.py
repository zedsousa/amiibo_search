from rest_framework.response import Response
from .models import Amiibo, TokenUser
from .serializers import *
from rest_framework import viewsets

from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.response import Response
from .models import Amiibo
from .serializers import *
from rest_framework import viewsets

from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import viewsets

class AmiiboViewSet(viewsets.ReadOnlyModelViewSet):
   
 
    queryset = Amiibo.objects.all()
    serializer_class = AmiiboSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        if request.method == 'GET':
            token = request.META.get('HTTP_AUTHORIZATION', None)

        if token and TokenUser.objects.filter(token = token):
            return Response(serializer.data)  
                  
        raise serializers.ValidationError("Token Error or Need Authorization")


    