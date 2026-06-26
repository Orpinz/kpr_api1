from django.contrib import admin
from .models import JenisKPR, PengajuanKPR, Cicilan, CicilanDeveloper

admin.site.register(JenisKPR)
admin.site.register(PengajuanKPR)
admin.site.register(Cicilan)
admin.site.register(CicilanDeveloper)