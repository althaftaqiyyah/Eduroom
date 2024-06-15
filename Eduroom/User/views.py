from django.shortcuts import render, redirect
from .models import user as User_Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import uploadImage
# Create your views here.
@login_required
def index(request):
    user_profile = User_Profile.objects.filter(NIM__icontains=request.user).first()
    context = {
        "profile" : user_profile
    }
    print(request)
    return render(request, "User/index.html", context)

@login_required
def update_profile_(request):
    if request.method == 'POST':
        current_password, new_password, repeat_new_password, Nama_, NIM_, Email_, profile_picture_, user_ = User_Profile().update_profile(request)         
        user_profile = User_Profile.objects.filter(NIM=user_.username).first()
        
        if not user_profile:
            user_profile = User_Profile(NIM=user_.username)
        
        if NIM_:
            user_.username = NIM_
            user_profile.NIM = NIM_
        
        if Nama_:
            user_profile.Nama = Nama_
        
        if Email_:
            user_.email = Email_
            user_profile.Email = Email_
        
        if profile_picture_:
            user_profile.profile_picture = profile_picture_
        
        if current_password and new_password and repeat_new_password:
            if new_password == repeat_new_password:
                if user_.check_password(current_password):
                    user_.set_password(new_password)
                    user_profile.Password = make_password(new_password)
                    user_.save()
                    user_profile.save()
                    update_session_auth_hash(request, user_)
                    messages.success(request, "Your Profile and Password have been updated.")
                else:
                    messages.error(request, 'Current password is incorrect.')
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            user_.save()
            user_profile.save()
            messages.success(request, 'Your profile has been updated!')
            
        return redirect("/Dashboard")
    
    user_profile = User_Profile.objects.filter(NIM=request.user.username).first()
    context = {
        "profile": user_profile,
    }
    return render(request, "User/index.html", context)

@login_required
def reset_image(request):
    try:
        defaultImage, user_profile = User_Profile().reset_images(request)         
        user_profile.profile_picture = defaultImage
        user_profile.save()
        return redirect("/User")
    except IntegrityError as e:
        if 'NoneType object has no attribute profile_picture' in str(e):
                
            messages.error(request, 'Belum Punya Foto Profile')
                
            return redirect('/User/')
        else:
            raise e
                