from django.contrib import admin
from django.urls import path
def PruebaEmpleado(self):
    print(f"**** Prueba desde Empleado ****")
    
urlpatterns = [
    path('empleado/', PruebaEmpleado),
]