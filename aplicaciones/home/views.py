from dataclasses import fields
from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


# imports model
from .models import Prueba

class PruebaView(TemplateView):
    template_name = "home/prueba.html"

class EjecutoVista(TemplateView):
    template_name = "home/sebastian.html"

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = "lista"
    queryset = ['Herrera', 'Viotti', 'Almada', 'Bertero']

class ListarPrueba(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html"
    context_object_name = "lista"    

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    fields = ['titulo','subtitulo','cantidad']
  
    

    