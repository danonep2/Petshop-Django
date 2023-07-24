from django.db import models

# Create your models here.

class Animal( models.Model ):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=255, null=False, blank=False)
    animal = models.CharField(max_length=255, null=False, blank=False)
    idade = models.IntegerField(null=False, blank=False)
    servico = models.CharField(max_length=255, null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    pagamento = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.cliente} === {self.animal}'