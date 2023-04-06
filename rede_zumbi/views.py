from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rede_zumbi.models import Sobrevivente, NivelDeInfecao
from rede_zumbi.serializer import SobreviventeSerializer, InfectadoSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class sobreviventeViewSet(ModelViewSet):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    
    
    
    
class infectadoCadastro(ModelViewSet):
    queryset = Sobrevivente.objects.all()
    serializer_class = InfectadoSerializer

    def create(self, request, *args, **kwargs):
        print("requeeeeeest.........:", request.data['nome'])
        pessoa = Sobrevivente.objects.get(nome=request.data['nome'])
        def check_pontos_de_infeccao(query):
            pessoa = query
            if pessoa.pontosDeInfectacao <= 2:
                pessoa.pontosDeInfectacao +=1
                pessoa.save()
            else:
                pessoa.pontosDeInfectacao +=1
                pessoa.save()
                pessoa.infectado = True
                pessoa.save()
        check_pontos_de_infeccao(pessoa)    
        
        print("pesoa.........................:", pessoa)
        print("adiçãoooooooo.......:",pessoa.pontosDeInfectacao)
        print("adiçãoooooooo.......:",pessoa.infectado)
        
        # serializer = self.serializer_class(data=request.data)
        
        # serializer.is_valid(raise_exception=True)
        # serializer.save(author=self.request.user)
        # headers = self.get_success_headers(serializer.data)
        # return Response(
        #     serializer.data,
        #     status=status.HTTP_201_CREATED,
        #     headers=headers
        # )

    



def view_test(request):
    return render(request, 'index.html')
    
    