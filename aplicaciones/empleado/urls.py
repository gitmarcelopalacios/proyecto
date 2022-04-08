from django.contrib import admin
from django.contrib import auth
from django.urls import path

#from proyecto.aplicaciones.departamento.models import Departamento 

# IMPORTO EL PAQUETE DE VISTA
from . import views


#from proyecto.aplicaciones.departamento.models import Departamento 

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig


class EmpleadoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "aplicaciones.empleado"

    urlpatterns = [
        path('empleadotemplateview/', views.ClaseEmpleadoTemplateView.as_view()),
        path('empleadolistview1/', views.ClaseEmpleadoListView1.as_view()),
        path('empleadolistview2/', views.ClaseEmpleadoListView2.as_view()),
        path('empleadolistar/', views.ClaseEmpleadoListar.as_view()),
        path('empleadoagregar/', views.ClaseEmpleadoCreateView.as_view()),
        ]

