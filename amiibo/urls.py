from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_amiibos),
    path('list/<int:id>', views.list_amiibos_byId, name='list_amiibos_byId'),
    path('list/<str:character>', views.list_amiibos_byCharacter, name='list_amiibos_byCharacter'),
    path('list/<str:game>', views.list_amiibos_byGame, name='list_amiibos_byGame'),
    path('list/<str:name>', views.list_amiibos_byName, name='list_amiibos_byName'),
    path('list/<str:type>', views.list_amiibos_byType, name='list_amiibos_byType'),
]