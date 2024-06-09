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
    detail_history = Reservasi.objects.filter(NIM=request.user)
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
    id = room_id
    history_update = Reservasi.objects.get(id = room_id)
    admins = User.objects.filter(is_superuser=True)
    email_admin = [admin.email for admin in admins]
    data = {
        'ID Ruangan': history_update.idRuangan,
        'History': history_update,
        'id': id,
        
    }
    
    if history_update.status == "Belum diproses":
        if request.method == 'POST':
            history_update.Nama_Peminjam =request.POST.get("borrower_name")
            history_update.idRuangan = request.POST.get("reservation_id")
            history_update.Email = request.POST.get("email")
            history_update.Purpose = request.POST.get("purpose")
            history_update.Tanggal_Penggunaan_Mulai= request.POST.get("start_date")
            history_update.Tanggal_Penggunaan_Selesai = request.POST.get("end_date")
            history_update.Waktu_Mulai = request.POST.get("start_time")
            history_update.Waktu_Selesai = request.POST.get("end_time")
            history_update.save()
            send_mail(
                "PERUBAHAN PENGAJUAN RUANGAN",
                f"Atas nama {history_update.Nama_Peminjam} telah merubah pengajuan peminjaman ruangan {history_update.idRuangan}, silahkan dilakukan pengecekkan",
                "ilkom734@gmail.com",
                email_admin,
                fail_silently=False
            )
            return redirect('/History/')
        else:
           
            context = {
                'History': history_update,
                'show_popup': True
            }
            return render(request, 'History/update.html', context)
    else:
        messages.error(request, f'Status anda telah {history_update.status}, Pengajuan tidak bisa diubah')
        return redirect("/History/")
   
  
   