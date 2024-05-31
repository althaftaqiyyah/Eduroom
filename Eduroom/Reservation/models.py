from django.db import models

# Create your models here.

class Reservasi(models.Model):
    idRuangan = models.CharField(max_length=200)
    Tanggal_Pengajuan = models.DateTimeField(auto_now_add=True)
    Tanggal_Penggunaan = models.DateField()
    Waktu_Mulai = models.TimeField()
    Waktu_Selesai = models.TimeField()
    status_choices = [
        ('Kosong', 'Kosong'),
        ('Dalam proses', 'Dalam proses'),
        ('Diterima', 'Diterima'),
        ('Ditolak', 'Ditolak'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Belum diproses')
    Keterangan = models.CharField(max_length=500, default='-')
    Nama_Peminjam= models.CharField(max_length=200)
    def __str__(self):
        return "{} | {}".format(self.idRuangan, self.Tanggal_Penggunaan)
    