from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from .models import Reservasi
from Room.models import Room
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    reservasi_room = Reservasi()
    email_admin, room_id = reservasi_room.reserve(request)
  
    data = {
        'idRuangan': room_id
    }
    if request.method == 'POST': 
            
            idRuangan = request.POST.get('reservation_id')
            base_url = 'http://127.0.0.1:8000/Room/detailRuangan/'
            redirect_url = f"{base_url}?IdRuangan={idRuangan}"
            tanggal_pengajuan = request.POST.get('Tanggal_Pengajuan')
            tanggal_penggunaan_mulai = request.POST.get('start_date')
            tanggal_penggunaan_selesai = request.POST.get('end_date')
            Nama_Peminjam = request.POST.get('borrower_name')
            Waktu_Mulai = request.POST.get('start_time')
            Waktu_Selesai = request.POST.get('end_time')
            Email = request.POST.get('email')
            Purpose =request.POST.get('purpose')
            if tanggal_penggunaan_mulai <= tanggal_penggunaan_selesai: 
                if tanggal_penggunaan_mulai == tanggal_penggunaan_selesai:
                    if Waktu_Mulai < Waktu_Selesai: 
                        Reservasi.objects.create(
                            NIM = request.user,
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
                        messages.success(request, "Reservasi berhasil")
                        return HttpResponseRedirect('/History/')  # Redirect to History page after successfully creating reservation
                    else : 
                        messages.error(request, "Invalid Time Input")
                        return redirect(redirect_url) 
                Reservasi.objects.create(
                            NIM = request.user,
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
            else : 
                messages.error(request, "Invalid Date Input")
                return redirect(redirect_url) 
    context = {
        'page_title': 'Reservasi',
        
    }
    return render(request, 'Reservation/reservasi.html', context)


