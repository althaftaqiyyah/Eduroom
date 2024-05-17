from django import forms
from .models import Room
class createRoom(forms.Form):
    IdRuangan = forms.CharField(max_length=100)
    NamaRuangan = forms.CharField(max_length=100)
    Kapasitas = forms.IntegerField()
    Lokasi = forms.CharField(max_length=200,  widget = forms.Textarea())
    Foto = forms.ImageField()
    
class PencarianForm(forms.Form):
    query = forms.CharField(label='Cari IdRuangan', max_length=100)
