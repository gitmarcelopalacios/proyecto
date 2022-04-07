from django.contrib import admin
from django.urls import path

# IMPORTO EL PAQUETE DE VISTA
# from .migrations import views
from . import views

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.urlx'
    
urlpatterns = [
   # path('clientetemplateview/', views.ClaseClienteView.as_view()),
    path('urlxlistview/', views.ClaseUrlxListView.as_view()),
]