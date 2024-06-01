from django.db import models

# Create your models here.
class Room(models.Model):
    IdRuangan = models.CharField(max_length=100, primary_key=True)
    NamaRuangan = models.CharField(max_length=100)
    Kapasitas = models.IntegerField()
    Lokasi = models.TextField(max_length=200)
    Foto = models.ImageField(upload_to='Room')
    
    def __str__(self):
        return "{}".format(self.IdRuangan)