from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Proovedor)
admin.site.register(Medicamento)
admin.site.register(Estado_Medicamento)
admin.site.register(Lote)