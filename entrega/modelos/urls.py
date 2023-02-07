from django.urls import path
from modelos.views import create_jugador, list_jugadores


urlpatterns = [
    path('create-jugador/', create_jugador),
    path('list-jugadores/', list_jugadores),

    ]