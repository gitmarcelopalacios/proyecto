

from django.db import models
from aplicaciones.tipo_documento.models import Tipo_Documento
from aplicaciones.condicion_iva.models import Condicion_Iva
class Emprendedor(models.Model):
    nombre=models.CharField(max_length=100)

    tipodocumento=models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE, default=1)
    numdocumento=models.CharField(max_length=20,default=' ')   

    condicioniva=models.ForeignKey(Condicion_Iva, on_delete=models.CASCADE, default=1)
    numeroiva=models.CharField(max_length=20,default=' ')   

    email=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre+' - '+self.email

