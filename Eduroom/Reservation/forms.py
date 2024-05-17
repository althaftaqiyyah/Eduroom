from django import forms
from Room.models import Room 
from .models import Reservasi

class Reservasi_form(forms.ModelForm):
    class Meta:
        model = Reservasi
        fields = ['idRuangan', 'Tanggal_Penggunaan', 'Waktu_Mulai', 'Waktu_Selesai', 'Nama_Peminjam' ]
        widgets = {
            'Tanggal_Penggunaan': forms.DateInput(attrs={'type': 'date'}),
            'Waktu_Mulai': forms.TimeInput(attrs={'type' : 'time','style': 'width: calc(15% - 18px);'}),
            'Waktu_Selesai': forms.TimeInput(attrs={'type' : 'time','style': 'width: calc(15% - 18px);'}),
        }
    