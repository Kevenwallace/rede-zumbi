from django.db import models

# Create your models here.
class items(models.Model):
    
    
    def __str__(self):
        return self.name
    

class sobrevivente(models.Model):
    nome = models.CharField(max_length=65)
    idade = models.IntegerField
    sexo = models.CharField(max_length=20)
    últimoLocal = models.CharField(max_length=30)
    inventario = models.ForeignKey(
         items, on_delete=models.SET_NULL, null=True
    )
    pontosDeInfectacao = models.IntegerField
    
    
