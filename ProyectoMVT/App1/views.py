from django.shortcuts import render
from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from App1.models import Familia

# Create your views here.

def familiares(self):

    familiar1 = Familia.objects.get(pk=1)

    diccionario = {"familiar1": familiar1}

    familiar2 = Familia.objects.get(pk=2)

    diccionario["familiar2"] = familiar2

    familiar3 = Familia.objects.get(pk=3)

    diccionario["familiar3"] = familiar3

    plantilla = loader.get_template('plantilla1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def plantillaMVT(self):

    nombre = "Victor"
    apellido = "Frette"
    dia = datetime.now()
    notas = [5, 6, 3, 9, 2]

    diccionario = {"nombre":nombre, "apellido":apellido, "fecha":dia, "notas":notas}

    #miHtml = open("C:/Users/victo/Documents/Python/Django/Proyecto1/ProyectoUno/ProyectoUno/plantillas/template1.html")

    #plantilla = Template(miHtml.read())

    #miHtml.close()

    plantilla = loader.get_template('plantilla1.html')

    
    #miContexto = Context(diccionario)

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)   