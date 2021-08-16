from django.contrib import admin
from .models import *

class ListAmiibo(admin.ModelAdmin):
    list_display = ('character','gameSeries', 'name', 'type',)
    list_display_links = ('character',)
    search_fields = ('character','gameSeries', 'name', 'type',)
    list_filter = ('type','gameSeries',)
    list_per_page = 10

admin.site.register(Amiibo, ListAmiibo)
admin.site.register(TokenUser)