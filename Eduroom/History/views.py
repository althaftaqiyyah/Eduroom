from django.shortcuts import render, redirect
from Reservation.models import Reservasi
from Reservation.forms import Reservasi_form
from Room.models import Room
# Create your views here.

def index(request):
    detail_history = Reservasi.objects.all()
    
    context = {
        "title" : "Eduroom",
        "history": detail_history
    }
    return render(request, "History/index.html", context)

def delete(request, room_id):
    Reservasi.objects.filter(id = room_id).delete()
    return redirect("/History/")

def update(request, room_id):
    
    history_update = Reservasi.objects.get(id = room_id)
    data = {
        'ID Ruangan': history_update.idRuangan,
        'Tanggal Pengajuan': history_update.Tanggal_Pengajuan,
        'Tanggal Penggunaan': history_update.Tanggal_Penggunaan
        
    }
    
    form_reservasi = Reservasi_form(request.POST or None, initial=data, instance = history_update)
    if request.method == 'POST':
        if form_reservasi.is_valid():
            form_reservasi.save()
        return redirect('/History/')
    
    context = {
        'form_reservasi': form_reservasi
        }
    return render(request, 'Reservation/reservasi.html', context)