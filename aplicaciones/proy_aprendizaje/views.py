from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView 


class PruebaView(TemplateView):
    template_name = "home/VistaTemplateView.html"

class PruebaListView(ListView):
    template_name = "home/VistaListView.html"
    context_object_name = "listaNumeros"
    queryset = ['AppReloj', 'AppAcute', 'AppPuertas', 'AppMuni']
    