from django.shortcuts import render
from django.http import HttpResponse

from modelos.models import Jugadores
from modelos.forms import JugadoresForm

# Create your views here.
def create_jugador(request):
    if request.method == "GET":
        context= {
            "form": JugadoresForm()
        }
        return render(request, "modelos/create_jugador.html", context =context)
    elif request.method == "POST":
        form = JugadoresForm(request.POST)
        if form.is_valid():
            Jugadores.objects.create(
                name = form.cleaned_data["name"],
                price = form.cleaned_data["price"],
                
            )
            context = {
                "message": "Jugador creado exitosamente"
            }
            return render(request, "modelos/create_jugador.html", context =context)
        else:
            context= {
                "form_errors": form.errors,
                "form": JugadoresForm
            }
            return render(request, "modelos/create_jugador.html", context =context)

        #Jugadores.objects.create(name= request.POST["name"], price= request.POST["price"])
        #return render(request, "modelos/create_jugador.html", context ={})

 


# def list_jugadores(request):
#     if "search" in request.GET:
#         search = request.GET["search"]
#         jugadores= Jugadores.objects.filter(name__icontains = search)
#     else:
#         jugadores= Jugadores.objects.all()
#         context= {
#         "jugadores" : jugadores
#         }
#     return render(request, "modelos/list_jugadores.html", context=context)
    
def list_jugadores(request):
    if 'search' in request.GET:
        search = request.GET['search']
        jugadores = Jugadores.objects.filter(name__icontains=search)
    else:
        jugadores = Jugadores.objects.all()
    context = {
        'jugadores':jugadores,
    }
    return render(request, 'modelos/list_jugadores.html', context=context)