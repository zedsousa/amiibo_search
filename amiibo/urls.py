from rest_framework.routers import DefaultRouter
from django.urls import include, path
from amiibo import views

router  = DefaultRouter()

router.register("amiibo_list", views.AmiiboViewSet)
urlpatterns = [
    path("", include(router.urls)),
]