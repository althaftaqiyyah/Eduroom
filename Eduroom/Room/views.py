from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
from .models import Room
from .forms import createRoom, PencarianForm
from Reservation.models import Reservasi
from User.models import user as User_Profile
# Create your views here.


def index(request):
    ruangan  = Room.objects.all() 
    context ={
        "title": "Eduroom",
        "room": ruangan,
    }
    return render(request, "Room/index.html", context)
"""
def detailRuangan(request):
    IdRuangan = request.GET.get('IdRuangan')
    user_profile = User_Profile.objects.filter(NIM__icontains=request.user).first()
    if IdRuangan:
        detail = Room.objects.filter(IdRuangan=IdRuangan).first()
        detail_history = Reservasi.objects.filter(idRuangan=IdRuangan).order_by('Tanggal_Pengajuan')
        context = {
            "title": "Eduroom",
            "detailRuangan": detail,
            "historyRuangan": detail_history,
            "profile": user_profile,
            "nav": [
            ["/History","History Reservasi"],
            ["/Dashboard", "Room"],
        ],
        }
        return render(request, "Room/detailRuangan.html", context) 
    else:
        # Handle jika parameter IdRuangan tidak ada
        return HttpResponse("Parameter IdRuangan tidak ditemukan")

"""

def detailRuangan(request):
    IdRuangan = request.GET.get('IdRuangan')
    user_profile = User_Profile.objects.filter(NIM__icontains=request.user).first()
    if IdRuangan:
        detail, detail_history = Room.detail_ruangan(IdRuangan)
        context = {
            "title": "Eduroom",
            "detailRuangan": detail,
            "historyRuangan": detail_history,
            "profile": user_profile,
            "nav": [
            ["/History","History Reservasi"],
            ["/Dashboard", "Room"],
        ],
        }
        return render(request, "Room/detailRuangan.html", context) 
    else:
        # Handle jika parameter IdRuangan tidak ada
        return HttpResponse("Parameter IdRuangan tidak ditemukan")
