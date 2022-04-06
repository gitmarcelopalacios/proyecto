from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
class PruebaView(TemplateView):
    template_name = "prueba.html"