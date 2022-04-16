from django.contrib import admin
from django.urls import path

# IMPORTO EL PAQUETE DE VISTA
from . import views

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig

class CuentaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.cuenta'
    
urlpatterns = [
#    path('cuenta/', views.ClaseCuentaView.as_view()),
]
