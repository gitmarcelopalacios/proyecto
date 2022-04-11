# from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView



class ClasePersonaTemplateView(TemplateView):
    template_name = "persona/TemplateView.html"

# class ClaseEmpleadoListView1(ListView):
#     template_name = "empleado/ListView.html"
#     context_object_name = "lista"
#     queryset = ['Contabilidad', 'Marketing','Finanzas','Inventario','Compras']

# class ClaseEmpleadoListView2(ListView):
#     template_name = "empleado/ListView.html"
#     context_object_name = "lista"
#     queryset = ['Contabilidad', 'Marketing','Finanzas','Inventario','Compras']

# class ClaseEmpleadoListar(ListView):
#     from .models import Empleado
#     template_name = "empleado/ListView.html"
#     model = Empleado
#     context_object_name = "lista"
    
# class ClaseEmpleadoCreateView(CreateView):
#     from django.views.generic.edit import CreateView
#     #template_name = "Empleado/empleadocreateview.html"
#     template_name = "Empleado/createview.html"
#     from .models import Empleado
#     model = Empleado
#     fields = ["nombre"]
    