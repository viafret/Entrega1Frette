from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechaNac = models.DateField()