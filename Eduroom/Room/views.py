from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
from .models import Room
from .forms import createRoom, PencarianForm
from Reservation.models import Reservasi
# Create your views here.


def index(request):
    ruangan  = Room.objects.all() 
    context ={
        "title": "Eduroom",
        "room": ruangan,
    }
    return render(request, "Room/index.html", context)

def detailRuangan(request):
    IdRuangan = request.GET.get('IdRuangan')
    
    if IdRuangan:
        detail = Room.objects.filter(IdRuangan=IdRuangan)
        detail_history = Reservasi.objects.filter(idRuangan=IdRuangan).order_by('Tanggal_Pengajuan')
        context = {
            "title": "Eduroom",
            "detailRuangan": detail,
            "historyRuangan": detail_history
        }
        return render(request, "Room/detailRuangan.html", context) 
    else:
        # Handle jika parameter IdRuangan tidak ada
        return HttpResponse("Parameter IdRuangan tidak ditemukan")


def createRuangan(request):
    form_room = createRoom()
    if request.method == 'POST':
       
        Room.objects.create(        
            IdRuangan = request.POST.get('IdRuangan'),
            NamaRuangan = request.POST.get('NamaRuangan'),
            Kapasitas = request.POST.get('Kapasitas'),
            Lokasi = request.POST.get('Lokasi'),
            Foto = request.POST.get('Foto')
        )
        return HttpResponseRedirect('/Room/')
    context = {
        'form_room': form_room,
    }
    
    return render(request,'Room/createRoom.html', context)


def HasilPencarian(request): 
    # Ambil kueri pencarian dari parameter GET
    query = request.GET.get('query')

    # Filter objek Room berdasarkan kueri pencarian
    if query:
        qs = Room.objects.filter(IdRuangan__icontains=query)
    else:
        # Jika tidak ada kueri pencarian, tampilkan semua objek Room
        qs = Room.objects.all()

    context = {
        'queryset': qs,
        'query': query  # Sertakan kueri pencarian dalam konteks untuk menampilkan kembali pada formulir pencarian di halaman HTML
    }
  
    return render(request, 'Room/hasilPencarian.html', context)