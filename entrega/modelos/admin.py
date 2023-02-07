from django.contrib import admin

# Register your models here.

from modelos.models import Jugadores

#admin.site.register(Jugadores)

@admin.register(Jugadores)
class JugadoresAdmin(admin.ModelAdmin):
    list_display= ("name", "price")
    list_filter = ( "price",)
    search_fields = ("name", "price")