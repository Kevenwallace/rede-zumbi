from django.db import models


# Create your models here.
class ItemsModel(models.Model):
    nome = models.CharField(max_length=15, unique=True)
    valor = models.IntegerField()


class Sobrevivente(models.Model):
    nome = models.CharField(max_length=65, unique=True)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=20)
    últimoLocal = models.CharField(max_length=30)
    pontosDeInfectacao = models.IntegerField(null=True)
    infectado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Inventario(models.Model):
    nome_sobrevivente = models.ForeignKey(
        Sobrevivente, on_delete=models.CASCADE, null=False, related_name="nome_sobrevivente" 
    )
    item = models.ForeignKey(ItemsModel, on_delete=models.CASCADE, null=True)


class ComercioZumbiModel(models.Model):
    negociador_1 = models.ForeignKey(
        Sobrevivente,
        on_delete=models.CASCADE,
        null=False,
        related_name="negoiciado_um",
    )
    item1_ngc1 = models.CharField(max_length=15)
    item2_ngc1 = models.CharField(max_length=15)

    negociador_2 = models.ForeignKey(
        Sobrevivente,
        on_delete=models.CASCADE,
        null=False,
        related_name="negociador_dois",
    )
    item1_ngc2 = models.CharField(max_length=15)
    item2_ngc2 = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
