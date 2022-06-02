from errno import EADDRNOTAVAIL
from django.db import models
from django.contrib.auth.models import User


class Carnet_Paciente(models.Model):
    color = models.CharField(max_length=30, verbose_name='Rojo/Amarillo/Verde')
    
    def __str__(self):
        return self.color
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)
    nacimiento = models.DateField()
    direccion = models.CharField(max_length=70)
    genero = models.CharField(max_length=1, verbose_name='Genero:(M / F)')
    correo = models.EmailField(max_length=150, unique=True)
    idCarnet_Paciente = models.ForeignKey(Carnet_Paciente, models.CASCADE)
    idUser = models.OneToOneField(User, models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.nombre
    
class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, verbose_name='M / F')
    nacimiento = models.DateField()
    especialidad = models.CharField(max_length=50)
    correo = models.EmailField(max_length=150, unique=True)
    telefono = models.CharField(max_length=13)
    direccion = models.CharField(max_length=70)
    idUser = models.OneToOneField(User, models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.nombre
    
class Farmaceuta(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField()
    telefono = models.CharField(max_length=13)
    genero = models.CharField(max_length=1, verbose_name='M / F')
    puesto = models.CharField(max_length=50)
    idUser = models.OneToOneField(User, models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.nombre