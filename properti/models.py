from django.db import models

class JenisKPR(models.Model):
    TIPE_CHOICES = [
        ('subsidi', 'KPR Subsidi'),
        ('komersil', 'KPR Komersil'),
    ]
    nama_jenis = models.CharField(max_length=100)
    tipe = models.CharField(max_length=20, choices=TIPE_CHOICES)
    bunga_per_tahun = models.DecimalField(max_digits=5, decimal_places=2)
    tenor_maksimal_tahun = models.IntegerField()
    deskripsi = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nama_jenis} ({self.tipe})"

    class Meta:
        verbose_name = "Jenis KPR"
        verbose_name_plural = "Jenis KPR"


class PengajuanKPR(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('diproses', 'Diproses'),
        ('disetujui', 'Disetujui'),
        ('ditolak', 'Ditolak'),
    ]
    nama_pemohon = models.CharField(max_length=200)
    nik = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    telepon = models.CharField(max_length=20)
    jenis_kpr = models.ForeignKey(JenisKPR, on_delete=models.PROTECT, related_name='pengajuan')
    harga_properti = models.DecimalField(max_digits=15, decimal_places=2)
    uang_muka = models.DecimalField(max_digits=15, decimal_places=2)
    tenor_tahun = models.IntegerField()
    penghasilan_bulanan = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    tanggal_pengajuan = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nama_pemohon} - {self.nik}"

    class Meta:
        verbose_name = "Pengajuan KPR"
        verbose_name_plural = "Pengajuan KPR"


class Cicilan(models.Model):
    pengajuan = models.ForeignKey(PengajuanKPR, on_delete=models.CASCADE, related_name='cicilan')
    bulan_ke = models.IntegerField()
    tanggal_jatuh_tempo = models.DateField()
    jumlah_cicilan = models.DecimalField(max_digits=15, decimal_places=2)
    pokok = models.DecimalField(max_digits=15, decimal_places=2)
    bunga = models.DecimalField(max_digits=15, decimal_places=2)
    status_bayar = models.BooleanField(default=False)
    tanggal_bayar = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cicilan ke-{self.bulan_ke} - {self.pengajuan.nama_pemohon}"

    class Meta:
        verbose_name = "Cicilan"
        verbose_name_plural = "Cicilan"
        ordering = ['bulan_ke']


class CicilanDeveloper(models.Model):
    pengajuan = models.ForeignKey(PengajuanKPR, on_delete=models.CASCADE, related_name='cicilan_developer')
    bulan_ke = models.IntegerField()
    tanggal_jatuh_tempo = models.DateField()
    jumlah_cicilan = models.DecimalField(max_digits=15, decimal_places=2)
    status_bayar = models.BooleanField(default=False)
    tanggal_bayar = models.DateField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cicilan Developer ke-{self.bulan_ke} - {self.pengajuan.nama_pemohon}"

    class Meta:
        verbose_name = "Cicilan Developer"
        verbose_name_plural = "Cicilan Developer"
        ordering = ['bulan_ke']