from django.shortcuts import render, HttpResponseRedirect

from .models import Reservasi
from Room.models import Room
from django.core.mail import send_mail
from django.contrib.auth.models import User


def index(request):
    admins = User.objects.filter(is_superuser=True)
    email_admin = [admin.email for admin in admins]
    room_id = request.POST.get('reservation_id')
    data = {
        'idRuangan': room_id
    }
    if request.method == 'POST': 
            idRuangan = request.POST.get('reservation_id')
            tanggal_pengajuan = request.POST.get('Tanggal_Pengajuan')
            tanggal_penggunaan_mulai = request.POST.get('end_date')
            tanggal_penggunaan_selesai = request.POST.get('start_date')
            Nama_Peminjam = request.POST.get('borrower_name')
            Waktu_Mulai = request.POST.get('start_time')
            Waktu_Selesai = request.POST.get('end_time')
            Email = request.POST.get('email')
            Purpose =request.POST.get('purpose')
            Reservasi.objects.create(
                idRuangan=idRuangan,
                Nama_Peminjam= Nama_Peminjam, 
                Tanggal_Pengajuan=tanggal_pengajuan,
                Tanggal_Penggunaan_Mulai=tanggal_penggunaan_mulai,
                Tanggal_Penggunaan_Selesai=tanggal_penggunaan_selesai,
                Waktu_Mulai=Waktu_Mulai,
                Waktu_Selesai= Waktu_Selesai,
                Email = Email,
                Purpose = Purpose
            )
            send_mail(
                "PENGAJUAN RUANGAN",
                f"Atas nama {Nama_Peminjam} telah mengajukan peminjaman ruangan {idRuangan}, silahkan dilakukan pengecekkan",
                "ilkom734@gmail.com",
                email_admin,
                fail_silently=False
            )
      
            return HttpResponseRedirect('/History/')  # Redirect to History page after successfully creating reservation
    
    context = {
        'page_title': 'Reservasi',
        
    }
    return render(request, 'Reservation/reservasi.html', context)


