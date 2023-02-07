from django.urls import path
from tecnicos.views import list_tecnicos, create_tecnico


urlpatterns = [
    path("list-tecnicos/", list_tecnicos),
    path('create-tecnico/', create_tecnico),

    ]