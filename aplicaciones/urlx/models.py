from django.db import models

# Create your models here.
class Urlx(models.Model):
    hipervinculo=models.CharField("Hipervinculo:",max_length=300)
    titulo=models.CharField("Título:",max_length=200)
   
    def __str__(self):
        return self.titulo