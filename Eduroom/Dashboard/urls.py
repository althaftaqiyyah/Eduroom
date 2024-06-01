from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('hasilPencarian', views.HasilPencarian, name='hasilPencarian')
]
