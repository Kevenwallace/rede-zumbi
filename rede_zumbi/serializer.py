from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rede_zumbi.models import Sobrevivente, NivelDeInfecao 


class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = '__all__'
        
class InfectadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelDeInfecao
        fields = 'nome'