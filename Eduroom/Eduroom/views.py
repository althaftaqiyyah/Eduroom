from django.shortcuts import render, HttpResponseRedirect,redirect
from User.models import user as userProfile
from .forms import *
from django.contrib.auth.models import User 
from django.contrib.auth import login , authenticate
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError


def index(request):
    context ={
        'title':"Eduroom"
    }
    return render(request, 'index.html', context)


def user_login(request):
    context = {
        'title': 'Login',
    }
    
    if request.method == "POST":
        username_login = request.POST.get('NIM')
        password_login = request.POST.get('Password')
        user = authenticate(request, username=username_login, password=password_login)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/Dashboard/')
        else:
            
            return redirect('login')
    
    return render(request, 'login.html', context)
    

def register(request):
    if request.method == 'POST':
        password = request.POST.get('Password')
        email = request.POST.get('Email')
        nama = request.POST.get('Nama')
        nim = request.POST.get('NIM')
        
        try:
            # Buat objek UserProfile dan simpan ke database
            user_profile = userProfile.objects.create(
                Email=email,
                Password=make_password(password),
                Nama=nama,
                NIM=nim,
            )
            
            # Buat objek User untuk autentikasi dan simpan ke database
            user = User.objects.create_user(username=nim, password=password)
        
        except IntegrityError as e:
            # Tangani jika username sudah ada
            if 'UNIQUE constraint failed: auth_user.username' in str(e):
                # Tambahkan pesan error untuk ditampilkan di template
                context = {
                    'error': 'Username (NIM) sudah ada. Silakan gunakan NIM lain.',
                }
                return redirect(request, '/login/', context)
            else:
                raise e
        
    
    return render(request, 'regist.html')