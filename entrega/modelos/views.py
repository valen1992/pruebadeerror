from django.shortcuts import render
from django.http import HttpResponse

from modelos.models import Jugadores

# Create your views here.
def create_jugador(request):
    new_jugador= Jugadores.objects.create(name= "Juanfer quintero", price = 20)
    print(new_jugador)
    return HttpResponse("Se creo el nuevo jugador Jugador")


def list_jugadores(request):
    all_jugadores= Jugadores.objects.all()
    context= {
    "jugadores" : all_jugadores
        }
    return render(request, "list_jugadores.html", context=context)
