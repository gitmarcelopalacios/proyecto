from django.db import models
from aplicaciones.cuenta.models import Cuenta

def str_fix(string,  lenght):
    rest = ' ' * 1200
    string_out = string + rest
    return string_out[0:lenght]




class Detalle_Cuenta(models.Model):
    idasiento = models.IntegerField(verbose_name='Asiento:', default=0)
    idcuenta=models.ForeignKey(Cuenta, on_delete=models.CASCADE, default=1)
    fecha = models.DateField('Fecha:', auto_now=False, auto_now_add=False)
    referencia=models.CharField('Referencia:', max_length=200)
    importe = models.DecimalField('Débito/Crédito:', max_digits=10, decimal_places=2)
    observaciones=models.CharField('Observaciones:',max_length=20,default=' ')   
    
    def __str__(self):
        return (str_fix(str(self.id),10)+'   '
               +str_fix(str(self.idasiento),10)+'   '
               +self.fecha.strftime('%d/%m/%Y')+'   '
               +str_fix(str(self.idcuenta),150)+'   '
               +str_fix(self.referencia,300)+'          '
               +str(self.importe))

