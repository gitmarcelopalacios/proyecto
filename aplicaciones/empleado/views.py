# from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView



class ClaseDepartamentoTemplateView(TemplateView):
    template_name = "departamento/DepartamentoTemplateView.html"

class ClaseDepartamentoListView1(ListView):
    template_name = "departamento/DepartamentoListView1.html"
    context_object_name = "lista"
    queryset = ['Contabilidad', 'Marketing','Finanzas','Inventario','Compras']

class ClaseDepartamentoListView2(ListView):
    template_name = "departamento/DepartamentoListView2.html"
    context_object_name = "lista"
    queryset = ['Contabilidad', 'Marketing','Finanzas','Inventario','Compras']

class ClaseDepartamentoListar(ListView):
    from .models import Departamento 
    template_name = "departamento/DepartamentoListView2.html"
    model = Departamento
    context_object_name = "lista"
    
class ClaseDepartamentoCreateView(CreateView):
    from django.views.generic.edit import CreateView
    #template_name = "departamento/departamentocreateview.html"
    template_name = "departamento/createview.html"
    from .models import Departamento 
    model = Departamento
    fields = ["nombre"]
    
