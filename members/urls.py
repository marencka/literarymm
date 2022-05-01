from django.urls import path
from . import views

# these are the url patterns for logging in, registering, and signing up 
urlpatterns = [
  path('login/', views.login_user, name="log_in"),
  path('register/', views.register_user, name="register"),
  path('signup/', views.sign_up_start, name="sign_up_start"),
  path('signupCont/', views.signupCont, name="signupCont"),
]
