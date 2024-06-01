from . import views
from django.urls import path

urlpatterns = [
    path('', views.index , name = "index"),
    path('update_profile', views.update_profile_, name="update_profile"),
    path('reset_image', views.reset_image, name="reset_image"),
]
