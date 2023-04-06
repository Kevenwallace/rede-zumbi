from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rede_zumbi.models import sobrevivente
from rede_zumbi.serializer import sobreviventeSerializer

# Create your views here.
class sobreviventeViewSet(ModelViewSet):
    queryset = sobrevivente.objects.all()
    serializer_class = sobreviventeSerializer
    
def view_test(request):
    return render(request, 'index.html')
    
    