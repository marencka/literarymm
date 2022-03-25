from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
  return render(request, 'base/index.html', {})

def logged_in(request):
  return render(request, 'base/loggedin.html', {})
