from django.db import models

class Estado_Tarea(models.Model):
    detalle=models.CharField('Detalle:', max_length=200)
    
    def __str__(self):
        return (
            str(self.id)+' - '+
            str(self.detalle)
        )

