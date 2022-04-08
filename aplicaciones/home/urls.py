from django.contrib import admin
from django.urls import path

# IMPORTO EL PAQUETE DE VISTA
from . import views

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.home'
    
urlpatterns = [
#    path('vistatemplate/', views.PruebaView.as_view()),
#    path('listatemplate/', views.PruebaListView.as_view()),
]
