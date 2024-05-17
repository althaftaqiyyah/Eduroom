from django.urls import path
from . import views
urlpatterns = [
    path('reservasi/<str:room_id>/', views.index, name='reservasi')
]
