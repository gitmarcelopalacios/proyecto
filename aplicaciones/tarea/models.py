from django.db import models
from aplicaciones.estado_tarea.models import Estado_Tarea
from aplicaciones.proyecto_tarea.models import Proyecto_Tarea

class Tarea(models.Model):
    fecha = models.DateField('Fecha:', auto_now=False, auto_now_add=True)
    id_proyecto_tarea=models.ForeignKey(Proyecto_Tarea, on_delete=models.CASCADE, default=1)
    id_estado_tarea=models.ForeignKey(Estado_Tarea, on_delete=models.CASCADE, default=1)
    detalle=models.CharField('Detalle:', max_length=200)
    observaciones=models.CharField('Observaciones:',max_length=20,default='')   
    
    def __str__(self):
        return (
            str(self.id) + '   ' + 
            str(self.id_proyecto_tarea) + '   ' + 
            str(self.id_estado_tarea) + '   ' + 
            str(self.detalle) + '   ' + 
            self.observaciones
        )
                

