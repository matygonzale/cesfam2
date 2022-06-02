from rest_framework import viewsets
from .serializers import *
from .models import *

class PrescripcionViewSets(viewsets.ModelViewSet):
    queryset = Prescripcion.objects.all()
    serializer_class = PrescripcionSerializer
    
class Reg_EntregasViewSets(viewsets.ModelViewSet):
    queryset = Reg_Entregas.objects.all()
    serializer_class = Reg_EntregasSerializer
    
class Cita_MedicaViewSets(viewsets.ModelViewSet):
    queryset = Cita_Medica.objects.all()
    serializer_class = Cita_MedicaSerializer