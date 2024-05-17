from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('delete/<int:room_id>/', views.delete, name = 'delete'),
    path('update/<int:room_id>/', views.update, name = 'update')
]
