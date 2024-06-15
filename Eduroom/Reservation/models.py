from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reservasi(models.Model):
    idRuangan = models.CharField(max_length=200)
    NIM = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Purpose = models.TextField()
    Tanggal_Pengajuan = models.DateTimeField(auto_now_add=True)
    Tanggal_Penggunaan_Mulai = models.DateField()
    Tanggal_Penggunaan_Selesai = models.DateField()
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
        return "{} | {}".format(self.idRuangan, self.Tanggal_Penggunaan_Mulai)
    
    def reserve(self, request):
        admins = User.objects.filter(is_superuser=True)
        email_admin = [admin.email for admin in admins]
        room_id = request.POST.get('reservation_id')
        return email_admin, room_id