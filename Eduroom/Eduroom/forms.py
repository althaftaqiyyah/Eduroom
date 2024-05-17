from django import forms
class Register(forms.Form):
    Username = forms.CharField(max_length=100)
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput())
    Nama  = forms.CharField(max_length=100)
    NIM = forms.CharField(max_length=100)
    departemen = forms.CharField(max_length=100)
    No_handphone = forms.CharField(max_length=100)
    
    
class Login(forms.Form):
    Username = forms.CharField(max_length=100)
    Email = forms.EmailField()