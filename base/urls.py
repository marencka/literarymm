from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name="index"),
  path('loggedin.html/', views.logged_in, name="logged_in"),
  
]
