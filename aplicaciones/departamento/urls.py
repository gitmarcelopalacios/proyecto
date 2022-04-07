from django.contrib import auth
from django.urls import path
from . import views 
from django.apps import AppConfig
    
urlpatterns = [
    path('listardepartamentos/', views.ListarDepartamento.as_view()),
]