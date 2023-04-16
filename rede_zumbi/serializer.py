from rest_framework import serializers
from rede_zumbi.models import Sobrevivente, ComercioZumbiModel, ItemsModel, InventarioModel


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsModel
        fields = ["nome", "valor"]


class InventarioSerializer(serializers.ModelSerializer):
    # sobreviventes = SobreviventeSerializer(many=False)

    class Meta:
        model = InventarioModel
        fields = [
            # "sobreviventes",
            "item"
        ]



class SobreviventeSerializer(serializers.ModelSerializer):
    # itemsla = ItemsSerializer(many=False)
    Inventario = InventarioSerializer(many=True)

    class Meta:
        model = Sobrevivente
        fields = [
            "Inventario",
            "nome",
            "idade",
            "sexo",
            "últimoLocal",
            "pontosDeInfectacao",
        ]
        read_only_fields = ["infectado"]




class ComercioZumbiSerializer(serializers.ModelSerializer):
    # sobreviventes = SobreviventeSerializer(many=False)

    class Meta:
        model = ComercioZumbiModel
        fields = [
            "negociador_1",
            "itens_ngc1",
            "negociador_2",
            "itens_ngc2",
        ]
