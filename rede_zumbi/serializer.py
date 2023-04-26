from rest_framework import serializers
from rede_zumbi.models import Sobrevivente, ComercioZumbiModel, ItemsModel, InventarioModel


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsModel
        fields = ["nome", "valor"]


class InventarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventarioModel
        fields = [
            "item"
        ]
        

class SobreviventeSerializer(serializers.ModelSerializer):
    Inventario = InventarioSerializer(many=True)


    class Meta:
        model = Sobrevivente
        fields = [
            "id",
            "Inventario",
            "nome",
            "idade",
            "sexo",
            "ultimoLocal",
            "pontosDeInfectacao",
            "infectado"
        ]
        
    def update(self, instance, validated_data):
        instance.ultimoLocal = validated_data.get("ultimoLocal", instance.ultimoLocal)
        instance.save()

        return instance
        

class ComercioZumbiSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComercioZumbiModel
        fields = [
            "negociador_1",
            "itens_ngc1",
            "negociador_2",
            "itens_ngc2",
        ]
