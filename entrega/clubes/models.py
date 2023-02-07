from django.db import models

# Create your models here.

class Clubes(models.Model):
    name = models.CharField(max_length= 50)
    fundacion = models.FloatField(max_length= 5)
