from django.shortcuts import render, HttpResponseRedirect
from User.models import user 
from .forms import *

def index(request):
    context ={
        'title':"Eduroom"
    }
    return render(request, 'index.html', context)


def login(request):
    form_login = Login()
    context = {
        'title':'Login',
        'form_login':form_login
    }
    return render(request, 'login.html', context)


def register(request):
    form_register = Register()
    user_model = user()
    
    context = {
        'title': 'Register',
        'form_register' : form_register
    } 
    print(request.method)
    if request.method == 'POST':
        user.objects.create(
            Username = request.POST.get('Username'),
            Email = request.POST.get('Email'),
            Password = request.POST.get('Password'),
            Nama  = request.POST.get('Nama'),
            NIM = request.POST.get('NIM'),
            departemen = request.POST.get('departemen'),
            No_handphone = request.POST.get('No_handphone')
        )
        return HttpResponseRedirect('/login/')
    return render(request, 'register.html', context=context)