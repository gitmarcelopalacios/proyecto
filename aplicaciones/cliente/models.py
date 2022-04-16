from django.db import models
from aplicaciones.tipo_documento.models import Tipo_Documento
from aplicaciones.condicion_iva.models import Condicion_Iva

# Create your models here.
class Cliente(models.Model):
    apellido=models.CharField("Apellido(s):",max_length=100)
    nombre=models.CharField("Nombre(s):",max_length=100)
    email=models.EmailField("Email:",max_length=200)
    domicilio=models.CharField("Domicilio:",max_length=100)
    
    tipodocumento=models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE, default=1)
    numdocumento=models.CharField(max_length=20,default=' ')   
        
    condicioniva=models.ForeignKey(Condicion_Iva, on_delete=models.CASCADE, default=1)
    cuilcuit=models.CharField("Número:",max_length=20)
    
    def __str__(self):
        return self.apellido+", "+self.nombre+" - "+self.email+" - "+self.domicilio+" - "+self.numdocumento+" - "+self.cuilcuit