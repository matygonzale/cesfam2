from rest_framework import viewsets
from .serializers import *
from .models import *

class PacienteViewSets(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    
class Carnet_PacienteViewSets(viewsets.ModelViewSet):
    queryset = Carnet_Paciente.objects.all()
    serializer_class = Carnet_PacienteSerializer

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DoctorViewSets(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
class FarmaceutaViewSets(viewsets.ModelViewSet):
    queryset = Farmaceuta.objects.all()
    serializer_class = FarmaceutaSerializer
    
    