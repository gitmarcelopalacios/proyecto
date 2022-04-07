from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView 


class ClaseProveedorView(TemplateView):
    template_name = "proveedor/ProveedorTemplateView.html"

class ClaseProveedorListView(ListView):
    template_name = "´proveedor/ProveedorListView.html"
    context_object_name = "listaClientes"
    queryset = ['Sebastián', 'Mario', 'Luciano', 'Matías']
    