from rest_framework import serializers
from rede_zumbi.models import Sobrevivente, ComercioZumbiModel, ItemsModel, Inventario




class SobreviventeSerializer(serializers.ModelSerializer):
    # itemsla = ItemsSerializer(many=False)
    # inventarios = InventarioSerializer(many=False)

    class Meta:
        model = Sobrevivente
        fields = [
            "nome",
            "idade",
            "sexo",
            "últimoLocal",
            "pontosDeInfectacao",
        ]
        read_only_fields = ["infectado"]

class InventarioSerializer(serializers.ModelSerializer):
    sobreviventes = SobreviventeSerializer(many=False)
    
    class Meta:
        model = Inventario
        fields = ["sobreviventes","nome_sobrevivente", "item"]

class ComercioZumbiSerializer(serializers.ModelSerializer):
    # sobreviventes = SobreviventeSerializer(many=False)

    class Meta:
        model = ComercioZumbiModel
        fields = [
            "negociador_1",
            "item1_ngc1",
            "item2_ngc1",
            "negociador_2",
            "item1_ngc2",
            "item2_ngc2",
        ]
