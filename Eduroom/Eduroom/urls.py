from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("register/", views.register),
    path("login/", views.login),
    path('Dashboard/', include("Dashboard.urls")),
    path('Room/', include("Room.urls")),
    path('History/', include("History.urls")),
    path('User/', include("User.urls")),
    path('reservasi/', include("Reservation.urls"))
]
