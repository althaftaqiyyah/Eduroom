from django.shortcuts import render, redirect
from Reservation.models import Reservasi
from Room.models import Room
from django.core.mail import send_mail
from django.contrib.auth.models import User
from User.models import user as User_Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def index(request):
    detail_history = Reservasi.objects.all()
    user_profile = User_Profile.objects.filter(NIM__icontains=request.user).first()
    context = {
        "title" : "Eduroom",
        "history": detail_history,
        "nav": [
            ["/History","History Reservasi"],
            ["/Dashboard", "Room"],
        ],
        "profile": user_profile
    }
    return render(request, "History/index.html", context)

def delete(request, room_id):
    Ruangan =  Reservasi.objects.get(id = room_id)
    Reservasi.objects.filter(id = room_id).delete()
    admins = User.objects.filter(is_superuser=True)
    email_admin = [admin.email for admin in admins]
    
    send_mail(
                "PEMBATALAN PENGAJUAN RUANGAN",
                f"Atas nama {Ruangan.Nama_Peminjam} telah membatalkan peminjaman ruangan {Ruangan.idRuangan}, silahkan dilakukan pengecekkan",
                "ilkom734@gmail.com",
                email_admin,
                fail_silently=False
            )
      
    return redirect("/History/")

def update(request, room_id):
    
    history_update = Reservasi.objects.get(id = room_id)
    admins = User.objects.filter(is_superuser=True)
    email_admin = [admin.email for admin in admins]
    data = {
        'ID Ruangan': history_update.idRuangan,
        'Tanggal Pengajuan': history_update.Tanggal_Pengajuan,
        'Tanggal Penggunaan': history_update.Tanggal_Penggunaan
        
    }
    if history_update.status == "Belum diproses": 
        #form_reservasi = Reservasi_form(request.POST or None, initial=data, instance = history_update)
        if request.method == 'POST':
            send_mail(
                "PERUBAHAN PENGAJUAN RUANGAN",
                f"Atas nama {history_update.Nama_Peminjam} telah merubah pengajuan peminjaman ruangan {history_update.idRuangan}, silahkan dilakukan pengecekkan",
                "ilkom734@gmail.com",
                email_admin,
                fail_silently=False
            )
            return redirect('/History/')
        
       
        return render(request, 'Reservation/reservasi.html')
    else : 
        messages.error(request, f'Status anda telah {history_update.status}, Pengajuan tidak bisa diubah')
        
        return redirect('/History/')