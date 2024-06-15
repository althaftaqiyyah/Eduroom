from django.db import models
from Reservation.models import Reservasi
class Room(models.Model):
    IdRuangan = models.CharField(max_length=100, primary_key=True)
    NamaRuangan = models.CharField(max_length=100)
    Kapasitas = models.IntegerField()
    Lokasi = models.TextField(max_length=200)
    Foto = models.ImageField(upload_to='Room')
    
    def __str__(self):
        return "{}".format(self.IdRuangan)
    
    def detail_ruangan(IdRuangan):
        detail = Room.objects.filter(IdRuangan=IdRuangan).first()
        reservasi = Reservasi.objects.filter(idRuangan=IdRuangan).order_by('Tanggal_Pengajuan')
        return detail, reservasi