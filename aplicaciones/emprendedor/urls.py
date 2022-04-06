from django.contrib import admin
from django.urls import path
def PruebaEmprendedor(self):
    print(f"**** Prueba desde emprendedor ****")
    
urlpatterns = [
    path('emprendedor/', PruebaEmprendedor),
]
