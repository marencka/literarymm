from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name="index"),
  path('userDashboard/', views.logged_in, name="logged_in"),
  path('info/', views.info, name="info"),
  path('userDashboard/meditation/', views.meditation, name="meditation"),

]
