from django.urls import path
from .views import home, login, agendar_visita_terreno

urlpatterns = [
    path('', home, name="home"),
    path('', login, name="login"),
    path('agendar_visita_terreno/', agendar_visita_terreno, name="agendar_visita_terreno"),
]