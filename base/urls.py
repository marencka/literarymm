from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name="index"),
  path('userDashboard/', views.dashboard, name="dashboard"),
  path('info/', views.info, name="info"),
  path('pdpr/', views.report, name="report"),
  path('userDashboard/meditation/', views.meditation, name="meditation"),
  path('userDashboard/pdpr/', views.pdpr, name="pdpr"), 
  path('userDashboard/history', views.history, name="history"),
  path('contact/', views.contact, name='contact'),
  path('information/', views.information, name='information'),
  path('userDashboard/pdpr_history/', views.pdpr_history, name='pdpr_history'),
]
