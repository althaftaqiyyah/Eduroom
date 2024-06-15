from django.db import models
from Reservation.models import Reservasi
from django.contrib.auth.models import User

# Create your models here.
class History(models.Model):
    def update(self, request, room_id):
        id = room_id
        history_update = Reservasi.objects.get(id = room_id)
        admins = User.objects.filter(is_superuser=True)
        email_admin = [admin.email for admin in admins]
        data = {
            'ID Ruangan': history_update.idRuangan,
            'History': history_update,
            'id': id,
            
        }
        
        return id, history_update, admins, email_admin, data
    
    def delete_data(self, request, room_id):
        Ruangan =  Reservasi.objects.get(id = room_id)
        Reservasi.objects.filter(id = room_id).delete()
        admins = User.objects.filter(is_superuser=True)
        email_admin = [admin.email for admin in admins]
        

        return Ruangan, admins, email_admin 
