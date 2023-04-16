from django.db import models


# Create your models here.
class ItemsModel(models.Model):
    nome = models.CharField(max_length=15, unique=True)
    valor = models.IntegerField()

    def __str__(self) :
        return self.nome

class Sobrevivente(models.Model):
    nome = models.CharField(max_length=65, unique=True)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=20)
    últimoLocal = models.CharField(max_length=30)
    pontosDeInfectacao = models.IntegerField(null=True)
    infectado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class InventarioModel(models.Model):
    nome_sobrevivente = models.ForeignKey(
        Sobrevivente,
        on_delete=models.CASCADE,
        null=False,
        related_name="Inventario",
    )
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE, null=True)
    quantidade = models.IntegerField(null=True)
    
   
    


class ComercioZumbiModel(models.Model):
    negociador_1 = models.ForeignKey(
        Sobrevivente,
        on_delete=models.CASCADE,
        null=False,
        related_name="negoiciado_um",
    )
    itens_ngc1 = models.CharField(max_length=15)
    

    negociador_2 = models.ForeignKey(
        Sobrevivente,
        on_delete=models.CASCADE,
        null=False,
        related_name="negociador_dois",
    )
    itens_ngc2 = models.CharField(max_length=15)
    

    # def __str__(self):
    #     return self.nome
