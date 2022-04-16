from django.db import models

# Create your models here.
class Condicion_Iva(models.Model):
    detalle=models.CharField("Detalle:",max_length=100)
    
    def __str__(self):
        return self.detalle