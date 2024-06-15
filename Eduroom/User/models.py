from django.db import models

# Create your models here.

class user(models.Model):
    
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Nama  = models.CharField(max_length=100)
    NIM = models.CharField(max_length=100, primary_key=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default="profile_pictures/profile.png")
    
    def __str__(self):
        return "{}".format(self.NIM)
    
    def update_profile(self, request):
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        repeat_new_password = request.POST.get('repeat_new_password')
        Nama_ = request.POST.get('Nama')
        NIM_ = request.POST.get('NIM')
        Email_ = request.POST.get("Email")
        profile_picture_ = request.FILES.get("profile_picture")
        user_ = request.user
        
        return current_password, new_password, repeat_new_password, Nama_, NIM_, Email_, profile_picture_, user_
    
    def reset_images(self, request):
        defaultImage = "/profile_pictures/profile.png"
        user_profile = user.objects.filter(NIM__icontains=request.user).first()
        return defaultImage, user_profile