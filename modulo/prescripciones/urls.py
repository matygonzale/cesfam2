from django.db import router
from django.urls import path, URLPattern
from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('api/prescripcion', PrescripcionViewSets)
router.register('api/reg_entregas', Reg_EntregasViewSets)
router.register('api/cita_medica', Cita_MedicaViewSets)

urlpatterns = router.urls