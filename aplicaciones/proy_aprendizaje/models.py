from django.db import models
#from aplicaciones.emprendedor.models import Emprendedor
from aplicaciones.empresa.models import Empresa
class Proy_aprendizaje(models.Model):
    # JOB_CHOICES = ( 
    #                ('0', 'Contador'),
    #                ('1', 'Administrador'),
    #                ('2', 'Economista'),
    #                ('3', 'Otro'),
    #                )
    emprendedor=models.ForeignKey(Emprendedor, on_delete=models.CASCADE, default=1)
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return str(self.id)+" - "+str(self.emprendedor)+" - "+str(self.empresa)