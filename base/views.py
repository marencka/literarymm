from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Quote, Image, Reflection, PDPR
from .forms import ReflectionForm, PDPRForm


# Create your views here.
def home(request):
  return render(request, 'base/index.html', {})

def dashboard(request):
  return render(request, 'base/dashboard.html', {})

def info(request):
  return render(request, 'base/info.html', {})

def meditation(request):
  quote = Quote.objects.order_by("?").first()
  all = Reflection.objects.filter(user=request.user)
  if request.method == "POST":
    form = ReflectionForm(request.POST)
    if form.is_valid():
      reflection = form.save(commit=False)
      reflection.user = request.user
      reflection.save()
      messages.success(request, ("Your reflection has been saved"))
      return redirect('dashboard')
  else:
    form = ReflectionForm
  return render(request, 'base/meditation.html', {'all': all, 'form': form, "quote":quote})

def pdpr(request):
  all = PDPR.objects.filter(user=request.user)
  submitted = False 
  if request.method == "POST":
    form = PDPRForm(request.POST)
    if form.is_valid():
      reflection = form.save(commit=False)
      reflection.user = request.user
      reflection.save()
      messages.success(request, ("Your reflection has been saved"))
      return redirect('dashboard')
  else:
    form = PDPRForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, 'base/db.html', {'all': all, 'form': form})


def history(request):
  past_reflections = Reflection.objects.filter(user=request.user) 
  return render(request, 'base/history.html', {"all": past_reflections})
