from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rede_zumbi.models import Sobrevivente, ComercioZumbiModel
from rede_zumbi.serializer import SobreviventeSerializer, ComercioZumbiSerializer
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class sobreviventeViewSet(ModelViewSet):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    http_method_names = ["GET", "POST"]


class infectadoCadastro(ModelViewSet):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer

    def create(self, request, *args, **kwargs):
        print("requeeeeeest.........:", request.data["nome"])
        pessoa = Sobrevivente.objects.get(nome=request.data["nome"])

        def check_pontos_de_infeccao(query):
            pessoa = query
            if pessoa.pontosDeInfectacao <= 2:
                pessoa.pontosDeInfectacao += 1
                pessoa.save()
            else:
                pessoa.pontosDeInfectacao += 1
                pessoa.save()
                pessoa.infectado = True
                pessoa.save()
            return pessoa

        serializer = check_pontos_de_infeccao(pessoa)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class MercadoZumbi(ModelViewSet):
    queryset = ComercioZumbiModel.objects.all()
    serializer_class = ComercioZumbiSerializer

    def create(self, request, *args, **kwargs):
        pessoa = Sobrevivente.objects.get(nome=request.data["nome"])

        def check_is_allowed(query):
            pessoa = query
            if pessoa.infectado == False:
                return True
            else:
                return False

        serializer = check_is_allowed(pessoa)
        if serializer == True:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(
                data=None,
                status=status.HTTP_403_FORBIDDEN,
            )


def view_test(request):
    return render(request, "index.html")
