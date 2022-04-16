from django.db import models

# Create your models here.
class Cuenta(models.Model):
    detalle=models.CharField("Detalle de Cuenta:",max_length=200)
    
    def __str__(self):
        return str(self.id)+' - '+self.detalle