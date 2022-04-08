from django.contrib import admin
from django.contrib import auth
from django.urls import path

#from proyecto.aplicaciones.departamento.models import Departamento 

# IMPORTO EL PAQUETE DE VISTA
from . import views
#from proyecto.aplicaciones.departamento.models import Departamento 

# REGISTRO AQUI MI MODELO
from django.apps import AppConfig


class DepartamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "aplicaciones.departamento"
    
urlpatterns = [
    path('departamentotemplateview/', views.ClaseDepartamentoTemplateView.as_view()),
    path('departamentolistview1/', views.ClaseDepartamentoListView1.as_view()),
    path('departamentolistview2/', views.ClaseDepartamentoListView2.as_view()),
    path('departamentolistar/', views.ClaseDepartamentoListar.as_view()),
    path('departamentoagregar/', views.ClaseDepartamentoCreateView.as_view()),
]



