from django.db import models

# Create your models here.

class Jadwal(models.Model):
    idRuangan = models.CharField(max_length=100)
    waktu=  models.DateTimeField(auto_now_add=True)
    