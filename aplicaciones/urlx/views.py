from re import template
from django.shortcuts import render

# Create your views here.
#from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

# class ClaseClienteView(TemplateView):
#     template_name = "cliente/ClienteTemplateView.html"

class ClaseUrlxListView(ListView):
    template_name = "urlx/UrlxListView.html"
    context_object_name = "listaTitulos"
    queryset = ['Google', 'Django Official', 'MySQL']
    
