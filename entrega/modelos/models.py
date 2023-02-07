from django.db import models

# Create your models here.

class Jugadores(models.Model):
    name = models.CharField(max_length= 50)
    price = models.FloatField()
    
    def __str__(self):
        return self.name