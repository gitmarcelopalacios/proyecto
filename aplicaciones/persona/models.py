from django.db import models
from aplicaciones.departamento.models import Departamento
class Persona(models.Model):
    JOB_CHOICES = ( 
                   ('0', 'Contador'),
                   ('1', 'Administrador'),
                   ('2', 'Economista'),
                   ('3', 'Otro'),
                   )
    first_name=models.CharField('Nombres',max_length=60)
    last_name=models.CharField('Apellidos',max_length=60)
    job=models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)+" - "+self.first_name+" - "+self.last_name