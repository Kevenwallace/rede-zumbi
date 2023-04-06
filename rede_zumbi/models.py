from django.db import models

# Create your models here.
class Items(models.Model):
    pass
    

class Sobrevivente(models.Model):
    nome = models.CharField(max_length=65, unique=True)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=20)
    últimoLocal = models.CharField(max_length=30)
    inventario = models.ForeignKey(
        Items, on_delete=models.SET_NULL, null=True
    )
    pontosDeInfectacao = models.IntegerField()
    infectado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
    
class NivelDeInfecao(models.Model):
    nome = models.ForeignKey(
        Sobrevivente, on_delete=models.CASCADE, null = False
    )
    pontosDeInfectacao = models.IntegerField()
    

    def __str__(self):
        return self.nome