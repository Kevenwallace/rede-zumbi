from django.contrib.auth.models import User, Group
from django.contrib.auth import models

from rest_framework import serializers
from rede_zumbi.models import Sobrevivente, ComercioZumbiModel


class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = "__all__"


class ComercioZumbiSerializer(serializers.ModelSerializer):
    sobreviventes = SobreviventeSerializer(many=False)

    class Meta:
        model = ComercioZumbiModel
        fields = [
            "sobreviventes",
            "negociador_1",
            "item1_ngc1",
            "item2_ngc1",
            "negociador_2",
            "item1_ngc2",
            "item2_ngc2",
        ]
