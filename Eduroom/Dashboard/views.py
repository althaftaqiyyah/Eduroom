from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title" : "Eduroom",
        "nav": [
            ["/Room","Reservasi Ruangan"],
            ["/History","Cek History Reservasi"],
            ["/User", "Profile"]
        ]
    }
    return render(request, "Dashboard/index.html", context)