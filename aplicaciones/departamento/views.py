from msilib.schema import ListView
from pyexpat import model
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from aplicaciones.departamento.models import Departamento

class ListarDepartamento(ListView):
    template_name = "departamento/listar.html"
    model=Departamento
    contexto_object_name = "lista"
    

