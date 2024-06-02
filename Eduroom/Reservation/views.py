from django.shortcuts import render, HttpResponseRedirect
from .forms import Reservasi_form
from .models import Reservasi
from Room.models import Room
from django.core.mail import send_mail
from django.contrib.auth.models import User


def index(request, room_id):
    admins = User.objects.filter(is_superuser=True)
    email_admin = [admin.email for admin in admins]
    
    data = {
        'idRuangan': room_id
    }
    if request.method == 'POST': 
        form_reservasi = Reservasi_form(request.POST)
        if form_reservasi.is_valid():  # Check if form is valid
            idRuangan = form_reservasi.cleaned_data.get('idRuangan')
            tanggal_pengajuan = form_reservasi.cleaned_data.get('Tanggal_Pengajuan')
            tanggal_penggunaan = form_reservasi.cleaned_data.get('Tanggal_Penggunaan')
            Nama_Peminjam = form_reservasi.cleaned_data.get('Nama_Peminjam')
            Waktu_Mulai = form_reservasi.cleaned_data.get('Waktu_Mulai')
            Waktu_Selesai = form_reservasi.cleaned_data.get('Waktu_Selesai')
            
            Reservasi.objects.create(
                idRuangan=idRuangan,
                Nama_Peminjam= Nama_Peminjam, 
                Tanggal_Pengajuan=tanggal_pengajuan,
                Tanggal_Penggunaan=tanggal_penggunaan,
                Waktu_Mulai=Waktu_Mulai,
                Waktu_Selesai= Waktu_Selesai
            )
            send_mail(
                "PENGAJUAN RUANGAN",
                f"Atas nama {Nama_Peminjam} telah mengajukan peminjaman ruangan {idRuangan}, silahkan dilakukan pengecekkan",
                "ilkom734@gmail.com",
                email_admin,
                fail_silently=False
            )
      
            return HttpResponseRedirect('/History/')  # Redirect to History page after successfully creating reservation
    else:
        form_reservasi = Reservasi_form(initial=data)  # Initialize form if request method is not POST
    
    context = {
        'page_title': 'Reservasi',
        'form_reservasi': form_reservasi,
    }
    return render(request, 'Reservation/reservasi.html', context)

