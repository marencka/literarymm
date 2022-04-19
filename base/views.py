from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Quote

# Create your views here.
def home(request):
  return render(request, 'base/index.html', {})

def logged_in(request):
  all_quotes = Quote.objects.all 
  return render(request, 'base/dashboard.html', {'all': all_quotes})

def info(request):
  return render(request, 'base/info.html', {})

def meditation(request):
  return render(request, 'base/meditation.html', {})