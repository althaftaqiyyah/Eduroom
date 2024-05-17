from django.db import models

# Create your models here.

class user(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Nama  = models.CharField(max_length=100)
    NIM = models.CharField(max_length=100)
    departemen = models.CharField(max_length=100)
    No_handphone = models.CharField(max_length=100)
    
    def __str__(self):
        return "{}".format(self.Username)