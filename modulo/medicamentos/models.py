from mailbox import NoSuchMailboxError
from statistics import correlation
from django.db import models
from django.forms import CharField



# Create your models here.

class Estado_Medicamento(models.Model):
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class Proovedor(models.Model):
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=13)
    direccion = models.CharField(max_length=70)
    correo = models.CharField(max_length=70)
    
    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    peso = models.CharField(max_length=30)
    fecha_caducidad = models.DateField()
    marca = models.CharField(max_length=45)
    stock = models.PositiveSmallIntegerField()
    precio = models.PositiveSmallIntegerField()
    idEstado_Medicamento = models.ForeignKey(Estado_Medicamento, models.DO_NOTHING)
    idProovedor = models.ForeignKey(Proovedor, models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre

class Lote(models.Model):
    descripcion = models.CharField(max_length=45)
    idMedicamento = models.ForeignKey(Medicamento, models.CASCADE)
    
    def __str__(self):
        return self.descripcion