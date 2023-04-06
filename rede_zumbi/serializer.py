from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rede_zumbi.models import sobrevivente


class sobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = sobrevivente
        fields = '__all__'