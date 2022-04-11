from django.contrib import admin
from django.urls import path
# IMPORTO EL PAQUETE DE VISTA
from . import views
from .models import Persona

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig


class PersonaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "aplicaciones.persona"
    
urlpatterns = [
     path('personatemplateview/', views.ClasePersonaTemplateView.as_view()),
    # path('departamentolistview1/', views.ClaseEmpleadoListView1.as_view()),
    # path('departamentolistview2/', views.ClaseEmpleadoListView2.as_view()),
    # path('departamentolistar/', views.ClaseDepartamentoListar.as_view()),
    # path('departamentoagregar/', views.ClaseDepartamentoCreateView.as_view()),
]
