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