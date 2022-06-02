from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Carnet_Paciente)
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Farmaceuta)