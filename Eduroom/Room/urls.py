from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('detailRuangan/', views.detailRuangan,name='detailRuangan'),
    path('createRoom/', views.createRuangan),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)