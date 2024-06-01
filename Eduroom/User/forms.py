from django import forms
from .models import user

class uploadImage(forms.Form):
    profile_picture =forms.ImageField()