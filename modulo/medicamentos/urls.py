from django.db import router
from django.urls import path, URLPattern
from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('api/medicamento', MedicamentoViewSets)
router.register('api/estado_medicamento', Estado_MedicamentoViewSets)
router.register('api/proovedor', ProovedorViewSets)
router.register('api/lote', LoteViewSets)

urlpatterns = router.urls