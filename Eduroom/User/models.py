from django.db import models

# Create your models here.

class user(models.Model):
    
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Nama  = models.CharField(max_length=100)
    NIM = models.CharField(max_length=100, primary_key=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default="profile.png")
    
    def __str__(self):
        return "{}".format(self.NIM)