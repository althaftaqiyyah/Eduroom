from . import views
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 
urlpatterns = [
    path('', views.index),
    path('hasilPencarian', views.HasilPencarian, name='hasilPencarian')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)