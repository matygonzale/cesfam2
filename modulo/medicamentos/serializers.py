from rest_framework import serializers
from dataclasses import fields
from modulo.medicamentos.models import *

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'
        
class Estado_MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_Medicamento
        fields = '__all__'
        
class ProovedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proovedor
        fields = '__all__'
        
class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'
        
