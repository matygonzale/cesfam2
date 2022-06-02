from django.db import models
from modulo.medicamentos.models import Medicamento
from modulo.usuarios.models import Farmaceuta, Carnet_Paciente, Doctor, Paciente


class Prescripcion(models.Model):
    observacion = models.CharField(max_length=300)
    fecha = models.DateField()
    idCarnet_Paciente = models.ForeignKey(Carnet_Paciente, models.DO_NOTHING, verbose_name='Sector Paciente ')
    idDoctor = models.ForeignKey(Doctor, models.DO_NOTHING)
    
class Reg_Entregas(models.Model):
    fecha = models.DateField(auto_now=True)
    idFarmaceuta = models.ForeignKey(Farmaceuta, models.DO_NOTHING)
    idMedicamento = models.ForeignKey(Medicamento, models.DO_NOTHING)
    idCarnet_Paciente = models.ForeignKey(Carnet_Paciente, models.CASCADE)
    
class Cita_Medica(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    idPaciente = models.ForeignKey(Paciente, models.CASCADE)
    idDoctor = models.ForeignKey(Doctor, models.CASCADE)
    idPrescripcion =models.ForeignKey(Prescripcion, models.DO_NOTHING)
    
    def __str__(self):
        return self.fecha

class Reserva(models.Model):
    idCarnet_Paciente = models.ForeignKey(Carnet_Paciente, models.DO_NOTHING)
    idPrescripcion = models.ForeignKey(Prescripcion, models.CASCADE)