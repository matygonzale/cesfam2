from dataclasses import fields
from rest_framework import serializers
from dataclasses import fields
from modulo.prescripciones.models import *

class PrescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescripcion
        fields = '__all__'
        
class Reg_EntregasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg_Entregas
        fields = '__all__'
        
class Cita_MedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita_Medica
        fields = '__all__'
