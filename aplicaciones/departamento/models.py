from django.db import models

class Departamento(models.Model):
    name=models.CharField('Nombre:', max_length=50, default=' ')
    shor_name=models.CharField('Nombre Corto:', max_length=20, default=' ')
    anulate=models.BooleanField('Anulado', default=False)
   
    def __str__(self):
        return str(self.id)+' - '+self.name + ' - ' + self.shor_name
    
