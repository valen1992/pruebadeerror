from django.urls import path
from clubes.views import list_clubes, create_club


urlpatterns = [
    path("list-clubes/", list_clubes),
    path('create-club/', create_club),
]