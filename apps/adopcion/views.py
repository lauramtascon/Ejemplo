from django.shortcuts import render

from django.http  import HttpResponse

def index_adopcion (request):
    return HttpResponse("Soy la página principal de la app adopción") #Mostrar en la pagina principal el texto index 