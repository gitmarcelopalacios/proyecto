from django.contrib import admin
from django.urls import path

# IMPORTO EL PAQUETE DE VISTA
from . import views

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig

class Estado_TareaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.estado_tarea'
    
urlpatterns = [
#    path('estado_tarea/', views.ClaseEstado_TareaView.as_view()),
]
