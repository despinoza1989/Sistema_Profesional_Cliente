from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

#   VISITA


def agendar_visita_terreno(request):
    return render(request, 'app/visita/agendar_visita_terreno.html')

#  CAPACITACION

def crear_capacitacion(request):
    return render(request, 'app/capacitacion/crear_capacitacion.html')

#  MEJORA

def crear_mejora(request):
    return render(request, 'app/mejora/crear_mejora.html')

#  ASESORIA

def crear_asesoria(request):
    return render(request, 'app/asesoria/crear_asesoria.html')

#   LISTADOS



