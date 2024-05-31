from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
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

@login_required
def user_logout(request):
    if request.method == "POST":
        # Check if 'logout' is in request.POST to avoid KeyError
        if request.POST["logout"] == "Submit":
            logout(request)
        return redirect("/login/")
    return render(request, "Dashboard/logout.html")