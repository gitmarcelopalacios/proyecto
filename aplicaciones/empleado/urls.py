from django.contrib import admin
from django.urls import path
# IMPORTO EL PAQUETE DE VISTA
from . import views
from .models import Empleado

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig


class EmpleadoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "aplicaciones.empleado"
    
urlpatterns = [
     path('empleadotemplateview/', views.ClaseEmpleadoTemplateView.as_view()),
    # path('departamentolistview1/', views.ClaseEmpleadoListView1.as_view()),
    # path('departamentolistview2/', views.ClaseEmpleadoListView2.as_view()),
    # path('departamentolistar/', views.ClaseDepartamentoListar.as_view()),
    # path('departamentoagregar/', views.ClaseDepartamentoCreateView.as_view()),
]
