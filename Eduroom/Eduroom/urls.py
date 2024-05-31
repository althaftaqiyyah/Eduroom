from . import views
from Dashboard import views as views_dashboard
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("register/", views.register, name = 'register'),
    path("Dashboard/logout/",views_dashboard.user_logout, name='logout'),
    path("login/", views.user_login, name= 'login'),
    path('Dashboard/', include("Dashboard.urls")),
    path('Room/', include("Room.urls")),
    path('History/', include("History.urls")),
    path('User/', include("User.urls")),
    path('reservasi/', include("Reservation.urls"))
] 
