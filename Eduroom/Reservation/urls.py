from django.urls import path
from . import views
urlpatterns = [
    path('reservasi/', views.index, name='reservasi')
]
