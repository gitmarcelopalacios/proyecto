from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView 


class ClaseClienteView(TemplateView):
    template_name = "cliente/ClienteTemplateView.html"

class ClaseClienteListView(ListView):
    template_name = "cliente/ClienteListView.html"
    context_object_name = "listaClientes"
    queryset = ['Herrera', 'Perez', 'Gonzalez', 'Alegre']
    