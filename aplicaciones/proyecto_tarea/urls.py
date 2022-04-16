from django.contrib import admin
from django.urls import path

# IMPORTO EL PAQUETE DE VISTA
from . import views

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig

class Proyecto_TareaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.proyecto_tarea'
    
urlpatterns = [
#    path('proyecto_tarea/', views.ClaseProyecto_TareaView.as_view()),
]
