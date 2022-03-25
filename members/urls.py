from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login_user, name="login"),
  path('register/', views.register_user, name="register"),
  path('signup/', views.sign_up_start, name="sign_up_start_info"),
  path('index/', views.returnHome, name="return_to_homepage"),
]
