from django.contrib import admin
from django.urls import path

# IMPORTO EL PAQUETE DE VISTA
from . import views

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig

class Proy_aprendizajeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.proy_aprendizaje'
    
urlpatterns = [
    path('proyvistatemplate/', views.PruebaView.as_view()),
    path('proylistatemplate/', views.PruebaListView.as_view()),
]

