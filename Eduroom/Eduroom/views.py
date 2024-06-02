from django.shortcuts import render, HttpResponseRedirect,redirect
from User.models import user as userProfile
from .forms import *
from django.contrib.auth.models import User 
from django.contrib.auth import login , authenticate
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib import messages

def index(request):
    context ={
        'title':"Eduroom"
    }
    return render(request, 'index.html', context)


def user_login(request):
    context = {
        'title': 'Login',
    }
    print(request.POST)
    if request.method == "POST":
        username_login = request.POST.get('NIM')
        password_login = request.POST.get('Password')
        user = authenticate(request, username=username_login, password=password_login)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/Dashboard/')
        else:
            print("salah")
            messages.error(request, 'Username atau password salah.')
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
            
            
            user = User.objects.create_user(username=nim, password=password,first_name=nama )
        
        except IntegrityError as e:
            
            if 'UNIQUE constraint failed: User_user.NIM' in str(e):
                
                messages.error(request, 'NIM yang anda masukkan telah terdaftar')
                
                return redirect('/login/')
            else:
                raise e
        
    username_login = request.POST.get('NIM')
    password_login = request.POST.get('Password')
    user = authenticate(request, username=username_login, password=password_login)
    login(request, user)
    return redirect('/Dashboard/')
