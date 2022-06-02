from rest_framework import viewsets
from .serializers import *
from .models import *

class MedicamentoViewSets(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    
class Estado_MedicamentoViewSets(viewsets.ModelViewSet):
    queryset = Estado_Medicamento.objects.all()
    serializer_class = Estado_MedicamentoSerializer
    
class ProovedorViewSets(viewsets.ModelViewSet):
    queryset = Proovedor.objects.all()
    serializer_class = ProovedorSerializer
    
class LoteViewSets(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer