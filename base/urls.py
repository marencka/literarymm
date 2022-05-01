from django.urls import path
from . import views

# This contains our URL's for this section of the website

urlpatterns = [
  path('', views.home, name="index"),
  path('userDashboard/', views.dashboard, name="dashboard"),
  path('userDashboard/meditation/', views.meditation, name="meditation"),
  path('userDashboard/pdpr/', views.pdpr, name="pdpr"), 
  path('userDashboard/history', views.history, name="history"),
  path('information/', views.information, name='information'),
  path('userDashboard/pdpr_history/', views.pdpr_history, name='pdpr_history'),
]
