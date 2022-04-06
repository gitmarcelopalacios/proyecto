from django.contrib import admin
from django.urls import path
def PruebaEmpresa(self):
    print(f"**** Prueba desde empresa ****")
    
urlpatterns = [
    path('empresa/', PruebaEmpresa),
]
