from django.shortcuts import render, redirect
from Reservation.models import Reservasi
from Room.models import Room
from django.core.mail import send_mail
from django.contrib.auth.models import User
from User.models import user as User_Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import History
# Create your views here.
@login_required
def index(request):
    detail_history = Reservasi.objects.filter(NIM=request.user).order_by("-Tanggal_Pengajuan")
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


@login_required
def delete(request, room_id):
    history = History()

    Ruangan, admins, email_admin  = history.delete_data(request, room_id)
    send_mail(
                "PEMBATALAN PENGAJUAN RUANGAN",
                f"Atas nama {Ruangan.Nama_Peminjam} telah membatalkan peminjaman ruangan {Ruangan.idRuangan}, silahkan dilakukan pengecekkan",
                "ilkom734@gmail.com",
                email_admin,
                fail_silently=False
            )
    messages.success(request, "Reservasi berhasil dihapus")
    return redirect("/History/")


@login_required
def update(request, room_id):
    history = History()
    id, history_update, admins, email_admin, data= history.update(request, room_id)
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
            messages.success(request, "Reservasi berhasil diubah")
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
   