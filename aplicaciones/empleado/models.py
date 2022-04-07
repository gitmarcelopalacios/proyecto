from django.db import models
# Create your models here.
class Empleado(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    dni=models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre+" - "+self.dni+" - "+self.email
