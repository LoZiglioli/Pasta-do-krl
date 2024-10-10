from django.db import models

class IMC(models.Model):
    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_calculo = models.DateTimeField(auto_now_add=True)

    def calcular_imc(self):
        if self.altura > 0:
            self.imc = self.peso / (self.altura ** 2)
        else:
            self.imc = None
