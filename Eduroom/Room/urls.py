from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('detailRuangan/', views.detailRuangan,name='detailRuangan'),
    path('createRoom/', views.createRuangan),
    path('hasilPencarian', views.HasilPencarian, name='hasilPencarian')
]