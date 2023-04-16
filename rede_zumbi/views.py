from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rede_zumbi.models import Sobrevivente, ComercioZumbiModel, InventarioModel, ItemsModel
from rede_zumbi.serializer import (
    SobreviventeSerializer,
    ComercioZumbiSerializer,
    InventarioSerializer,
    ItemsSerializer,
)
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class sobreviventeViewSet(ModelViewSet):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    http_method_names = ["get", "post"]
    
    def retrieve(self, request, *args, **kwargs):
        instance = Sobrevivente.Inventario.filter(nome='keven')
        serializer = self.get_serializer(instance)
        print(serializer)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        Inventario_items = request.data.pop('Inventario')
        sobrevivente = Sobrevivente(
            nome=request.data['nome'],
            idade=request.data['idade'],
            sexo=request.data['sexo'],
            últimoLocal=request.data['últimoLocal'],
            pontosDeInfectacao=request.data['pontosDeInfectacao']
            )
        sobrevivente.save()
        nome = Sobrevivente.objects.get(nome=request.data['nome'])
        bulk_aux = list()
        print(Inventario_items)
        
        for item_qtd in Inventario_items[0]['item']:
            print(item_qtd)
            for x, y in item_qtd.items():
                print(x)
                print(y)
                instace = InventarioModel(
                    nome_sobrevivente=nome,
                    item=ItemsModel.objects.get(nome=x),
                    quantidade=y                
                )
                bulk_aux.append(instace)
        InventarioModel.objects.bulk_create(bulk_aux)
        
        
        return Response(
            status=status.HTTP_201_CREATED,
        )


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

        def case_of_trades(serializerData):
            print(serializerData)
            pessoa1 = Sobrevivente.objects.get(nome=request.data["negociador_1"])
            pessoa2 = Sobrevivente.objects.get(nome=request.data["negociador_2"])
            
            
            lista_items1 = serializerData['itens_ngc1']
            lista_items1_ids = list()
            count1 = 0
            for x in lista_items1:
                itens_ngc1 = ItemsModel.objects.get(nome=x)
                print(itens_ngc1, "...", itens_ngc1.id)
                count1 += itens_ngc1.valor
                lista_items1_ids.append(itens_ngc1.id)
            
            lista_items2 = serializerData['itens_ngc2']
            lista_items2_ids = list()
            count2 = 0
            for x in lista_items2:
                itens_ngc2 = ItemsModel.objects.get(nome=x)
                print(itens_ngc2, "...", itens_ngc2.id)
                count2 += itens_ngc2.valor
                lista_items2_ids.append(itens_ngc2.id)
            
            print("sobre os items do primeiro negociante, lista_itens:", lista_items1, "lista_itens_ids:", lista_items1_ids, "count...:", count1)
            
            print("sobre os items do segundo negociante, lista_itens:", lista_items2, "lista_itens_ids:", lista_items2_ids, "count...:", count2)
            
            if count1 == count2:
            
                for x, ide in enumerate(lista_items1_ids):
                    ngc1_inventario = InventarioModel.objects.filter(
                        nome_sobrevivente_id=pessoa1.id,
                        item_id=ide).first()
                    print(ide)
                    print("antes do if..........:",ngc1_inventario)
                    if ngc1_inventario.quantidade <= 0: return Response(status=status.HTTP_412_PRECONDITION_FAILED)
                    ngc1_inventario.quantidade -= 1
                    ngc1_inventario.save()
                    
                    ngc1_inventario = InventarioModel.objects.filter(
                        nome_sobrevivente_id=pessoa1.id,
                        item_id=lista_items2_ids[x]).first()
                    
                    if ngc1_inventario == None:
                        ngc1_inventario = InventarioModel(
                            nome_sobrevivente_id=pessoa1.id,
                            item_id=lista_items2_ids[x])
                        ngc1_inventario.save()
                    else:
                        ngc1_inventario.quantidade += 1
                        ngc1_inventario.save()
            
                for x, ide in enumerate(lista_items2_ids):
                    ngc2_inventario = InventarioModel.objects.filter(
                        nome_sobrevivente_id=pessoa2.id,
                        item_id=ide).first()
                    if ngc2_inventario.quantidade <= 0: return Response(status=status.HTTP_412_PRECONDITION_FAILED)
                    ngc2_inventario.quantidade -= 1
                    ngc2_inventario.save()
                    
                    ngc2_inventario = InventarioModel.objects.filter(
                        nome_sobrevivente_id=pessoa2.id,
                        item_id=lista_items1_ids[x]).first()
                    
                    if ngc2_inventario == None:
                        ngc2_inventario = InventarioModel(
                            nome_sobrevivente_id=pessoa2.id,
                            item_id=lista_items1_ids[x])
                        ngc1_inventario.save()
                    else:
                        ngc1_inventario.quantidade += 1
                        ngc1_inventario.save()            
        
        case_of_trades(request.data)
        
        
    #     return Response(
    #         serializer.data, status=status.HTTP_201_CREATED, headers=headers
    #     )
    # else:
    #     return Response(
    #         data=None,
    #         status=status.HTTP_403_FORBIDDEN,
    #     )


class ItemsViewSet(ModelViewSet):
    queryset = ItemsModel.objects.all()
    serializer_class = ItemsSerializer


class InventarioViewSet(ModelViewSet):
    queryset = InventarioModel.objects.all()
    serializer_class = InventarioSerializer
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        # nome = request.data['sobreviventes.nome']
        # idade = request.data['sobreviventes.idade']
        # sexo = request.data['sobreviventes.sexo']
        # últimoLocal = request.data['sobreviventes.últimoLocal']
        # pontosDeInfectacao = request.data['sobreviventes.pontosDeInfectacao']
        
        # sobrevivente = Sobrevivente(
        #     nome=nome,
        #     idade=idade,
        #     sexo=sexo,
        #     últimoLocal=últimoLocal,
        #     pontosDeInfectacao=pontosDeInfectacao,
        # )
        # sobrevivente.save()
        
        # nome_sobrevivente = Sobrevivente.objects.get(nome=request.data['sobreviventes.nome'])
        # item1 = ItemsModel.objects.get(id=request.data['item1'])
        # item2 = ItemsModel.objects.get(id=request.data['item2'])
        # item3 = ItemsModel.objects.get(id=request.data['item3'])
        # item4 = ItemsModel.objects.get(id=request.data['item4'])
        # teste = Inventario(
        #     nome_sobrevivente=nome_sobrevivente,
        #     item1=item1
        #     )
        
        # teste.save()

        
        # return super().create(request, *args, **kwargs)


def view_test(request):
    return render(request, "index.html")
