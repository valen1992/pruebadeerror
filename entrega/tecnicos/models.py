from django.db import models

# Create your models here.

class Tecnicos(models.Model):
    name = models.CharField(max_length= 50)
    club = models.CharField(max_length= 50)
