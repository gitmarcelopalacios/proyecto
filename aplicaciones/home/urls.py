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
   path('seba/', views.EjecutoVista.as_view()),
   path('prueba/', views.PruebaView.as_view()),
   path('lista/', views.PruebaListView.as_view()),
   path('lista-prueba/', views.ListarPrueba.as_view()),
   path('add/', views.PruebaCreateView.as_view()),
]
