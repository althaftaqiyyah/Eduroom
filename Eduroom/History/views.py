from django.shortcuts import render, redirect
from Reservation.models import Reservasi
from Reservation.forms import Reservasi_form
from Room.models import Room
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    detail_history = Reservasi.objects.all()
    
    context = {
        "title" : "Eduroom",
        "history": detail_history
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
        form_reservasi = Reservasi_form(request.POST or None, initial=data, instance = history_update)
        if request.method == 'POST':
            if form_reservasi.is_valid():
                form_reservasi.save()
                send_mail(
                "PERUBAHAN PENGAJUAN RUANGAN",
                f"Atas nama {history_update.Nama_Peminjam} telah merubah pengajuan peminjaman ruangan {history_update.idRuangan}, silahkan dilakukan pengecekkan",
                "ilkom734@gmail.com",
                email_admin,
                fail_silently=False
            )
            return redirect('/History/')
        
        context = {
            'form_reservasi': form_reservasi
            }
        return render(request, 'Reservation/reservasi.html', context)
    else : 
        context ={
            'status': history_update.status
        }
        return render(request, "History/notUpdate.html", context)