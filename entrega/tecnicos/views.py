from django.shortcuts import render
from django.http import HttpResponse

from tecnicos.models import Tecnicos


from tecnicos.forms import TecnicosForm

# Create your views here.
def create_tecnico(request):
    if request.method == "GET":
        context= {
            "form": TecnicosForm()
        }
        return render(request, "tecnicos/create_tecnico.html", context =context)
    elif request.method == "POST":
        form = TecnicosForm(request.POST)
        if form.is_valid():
            Tecnicos.objects.create(
                name = form.cleaned_data["name"],
                club = form.cleaned_data["club"],
                
            )
            context = {
                "message": "Tecnico creado exitosamente"
            }
            return render(request, "tecnicos/create_tecnico.html", context =context)
        else:
            context= {
                "form_errors": form.errors,
                "form": TecnicosForm
            }
            return render(request, "tecnicos/create_tecnico.html", context =context)

        #Jugadores.objects.create(name= request.POST["name"], price= request.POST["price"])
        #return render(request, "modelos/create_jugador.html", context ={})

 


def list_jugadores(request):
    all_jugadores= Tecnicos.objects.all()
    context= {
    "jugadores" : all_jugadores
        }
    return render(request, "modelos/list_jugadores.html", context=context)

def list_tecnicos(request):
    all_tecnicos= Tecnicos.objects.all()
    context= {
    "tecnicos" : all_tecnicos
        }
    return render(request, "tecnicos/list_tecnicos.html", context=context)