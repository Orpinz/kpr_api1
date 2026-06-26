from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JenisKPRViewSet, PengajuanKPRViewSet, CicilanViewSet, CicilanDeveloperViewSet

router = DefaultRouter()
router.register(r'jenis-kpr', JenisKPRViewSet)
router.register(r'pengajuan-kpr', PengajuanKPRViewSet)
router.register(r'cicilan', CicilanViewSet)
router.register(r'cicilan-developer', CicilanDeveloperViewSet)

urlpatterns = [
    path('', include(router.urls)),
]