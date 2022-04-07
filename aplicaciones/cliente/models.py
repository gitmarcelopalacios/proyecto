from django.db import models

# Create your models here.
class Cliente(models.Model):
    apellido=models.CharField("Apellido(s):",max_length=100)
    nombre=models.CharField("Nombre(s):",max_length=100)
    email=models.EmailField("Email:",max_length=200)
    domicilio=models.CharField("Domicilio:",max_length=100)
    dni=models.CharField("DNI:",max_length=20)
    cuilcuit=models.CharField("CUIL O CUIT:",max_length=20)
    
    def __str__(self):
        return self.apellido+", "+self.nombre+" - "+self.email+" - "+self.domicilio+" - "+self.dni+" - "+self.cuilcuit