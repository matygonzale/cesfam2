from django.db import router
from django.urls import path, URLPattern
from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('api/paciente', PacienteViewSets)
router.register('api/carnet_paciente', Carnet_PacienteViewSets)
router.register('api/user', UserViewSets)
router.register('api/doctor', DoctorViewSets)
router.register('api/farmaceuta', FarmaceutaViewSets)


urlpatterns = router.urls