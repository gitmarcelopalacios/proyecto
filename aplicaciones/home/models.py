from django.db import models

# Create your models here.
class Home(models.Model):
    titulo=models.CharField(max_length=120)
    subtitulo=models.CharField(max_length=70)
    cantidad=models.IntegerField()
    
    def __str__(self):
        return self.titulo
    
    