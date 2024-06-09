from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from Room.models import Room
from User.models import user as User_Profile
# Create your views here.
@login_required
def index(request):
    ruangan  = Room.objects.all() 
    user_profile = User_Profile.objects.filter(NIM__icontains=request.user).first()
    context = {
        "room": ruangan,
        "title" : "Eduroom",
        "nav": [
            ["/History","History Reservasi"],
            ["/Dashboard", "Room"],
        ],
        "profile": user_profile
    }
    print(user_profile.profile_picture.url)
    return render(request, "Dashboard/index.html", context)

@login_required
def user_logout(request):
    if request.method == "POST":
       
        if request.POST["logout"] == "Logout":
            print("logout")
            logout(request)
            request.session.flush()
        return redirect("/login/")
    return render(request, "Dashboard/logout.html")
@login_required
def HasilPencarian(request): 
    
    query = request.GET.get('query')
    user_profile = User_Profile.objects.filter(NIM__icontains=request.user).first()
    
    if query:
        qs = Room.objects.filter(IdRuangan__icontains=query)
    else:
        
        qs = Room.objects.all()

    context = {
        'queryset': qs,
        'query': query, 
        "nav": [
            ["/History","History Reservasi"],
            
        ],
        "profile": user_profile
    }
  
    return render(request, 'Dashboard/index.html', context)