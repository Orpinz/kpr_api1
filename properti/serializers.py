from rest_framework import serializers
from .models import JenisKPR, PengajuanKPR, Cicilan, CicilanDeveloper


class JenisKPRSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenisKPR
        fields = '__all__'


class CicilanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cicilan
        fields = '__all__'


class CicilanDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = CicilanDeveloper
        fields = '__all__'


class PengajuanKPRSerializer(serializers.ModelSerializer):
    jenis_kpr_nama = serializers.CharField(source='jenis_kpr.nama_jenis', read_only=True)
    tipe_kpr = serializers.CharField(source='jenis_kpr.tipe', read_only=True)
    cicilan = CicilanSerializer(many=True, read_only=True)
    cicilan_developer = CicilanDeveloperSerializer(many=True, read_only=True)

    class Meta:
        model = PengajuanKPR
        fields = '__all__'