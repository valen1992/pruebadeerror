from django.shortcuts import render
from django.http import HttpResponse

from clubes.models import Clubes


from clubes.forms import ClubesForm

# Create your views here.
def create_club(request):
    if request.method == "GET":
        context= {
            "form": ClubesForm()
        }
        return render(request, "clubes/create_club.html", context =context)
    elif request.method == "POST":
        form = ClubesForm(request.POST)
        if form.is_valid():
            Clubes.objects.create(
                name = form.cleaned_data["name"],
                fundacion = form.cleaned_data["fundacion"],
                
            )
            context = {
                "message": "Club creado exitosamente"
            }
            return render(request, "clubes/create_club.html", context =context)
        else:
            context= {
                "form_errors": form.errors,
                "form": ClubesForm
            }
            return render(request, "clubes/create_club.html", context =context)
 


def list_clubes(request):
    all_clubes= Clubes.objects.all()
    context= {
    "clubes" : all_clubes
        }
    return render(request, "clubes/list_clubes.html", context=context)
