from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView 


class PruebaView(TemplateView):
    template_name = "home/ClienteTemplateView.html"

class PruebaListView(ListView):
    template_name = "home/ClienteListView.html"
    context_object_name = "listaClientes"
    queryset = ['Herrera', 'Viotti', 'Almada', 'Bertero']
    