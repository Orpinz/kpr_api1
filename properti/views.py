from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import JenisKPR, PengajuanKPR, Cicilan, CicilanDeveloper
from .serializers import (
    JenisKPRSerializer, PengajuanKPRSerializer,
    CicilanSerializer, CicilanDeveloperSerializer
)


class JenisKPRViewSet(viewsets.ModelViewSet):
    queryset = JenisKPR.objects.all().order_by('-created_at')
    serializer_class = JenisKPRSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipe']


class PengajuanKPRViewSet(viewsets.ModelViewSet):
    queryset = PengajuanKPR.objects.all().order_by('-created_at')
    serializer_class = PengajuanKPRSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'jenis_kpr']


class CicilanViewSet(viewsets.ModelViewSet):
    queryset = Cicilan.objects.all().order_by('bulan_ke')
    serializer_class = CicilanSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pengajuan', 'status_bayar']


class CicilanDeveloperViewSet(viewsets.ModelViewSet):
    queryset = CicilanDeveloper.objects.all().order_by('bulan_ke')
    serializer_class = CicilanDeveloperSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pengajuan', 'status_bayar']