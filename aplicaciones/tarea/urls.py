from django.contrib import admin
from django.urls import path

# IMPORTO EL PAQUETE DE VISTA
from . import views

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig

class TareaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.tarea'
    
urlpatterns = [
#    path('tarea/', views.ClaseTareaView.as_view()),
]
