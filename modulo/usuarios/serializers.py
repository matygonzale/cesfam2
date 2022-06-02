from rest_framework import serializers
from dataclasses import fields
from modulo.usuarios.models import *

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class Carnet_PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carnet_Paciente
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class FarmaceutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmaceuta
        fields = '__all__'
        