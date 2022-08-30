from django.urls import path
from .views import home, login, agendar_visita_terreno, crear_capacitacion, crear_mejora, crear_asesoria

urlpatterns = [
    path('', home, name="home"),
    path('', login, name="login"),
    path('agendar_visita_terreno/', agendar_visita_terreno, name="agendar_visita_terreno"),
    path('crear_capacitacion/', crear_capacitacion, name="crear_capacitacion"),
    path('crear_mejora/', crear_mejora, name="crear_mejora"),
    path('crear_asesoria/', crear_asesoria, name="crear_asesoria"),
]