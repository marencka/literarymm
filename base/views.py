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

def pdpr2(request):
  return render(request, 'base/pdpr2.html', {})

def report(request):
  return render(request, 'base/pdpr.html', {})

def meditation(request):
  quote = Quote.getRandomQuoteWithPD()
  nonPDQuote = Quote.getRandomQuoteNoPD()
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

    pic = Image.objects.all().order_by("?").first()

  return render(request, 'base/meditation.html', {'all': all, 'form': form, "quote":quote, 'nonPDQuote':nonPDQuote, 'picture':pic})

def pdpr(request):
  all = PDPR.objects.filter(user=request.user)
  if request.method == "POST":
    form = PDPRForm(request.POST)
    if form.is_valid():
      pdpr = form.save(commit=False)
      pdpr.user = request.user
      pdpr.life_skills_total = pdpr.q1 + pdpr.q2 + pdpr.q3 + pdpr.q4 + pdpr.q5 + pdpr.q6 + pdpr.q7 + pdpr.q8
      pdpr.life_stress_total = pdpr.q9 + pdpr.q10 + pdpr.q11 + pdpr.q12 + pdpr.q13 
      pdpr.life_coping_total = pdpr.q14 + pdpr.q15
      pdpr.quality_of_life = pdpr.q1 + pdpr.q2 + pdpr.q3 + pdpr.q4 + pdpr.q5 + pdpr.q6 + pdpr.q7 + pdpr.q8 + pdpr.q9 + pdpr.q10 + pdpr.q11 + pdpr.q12 + pdpr.q13 + pdpr.q14 + pdpr.q15
      pdpr.save()
      messages.success(request, ("Your reflection has been saved"))
      return redirect('dashboard')
  else:
    form = PDPRForm
  return render(request, 'base/pdpr.html', {'all': all, 'form': form})


def history(request):
  past_reflections = Reflection.objects.order_by('-date').filter(user=request.user)
  return render(request, 'base/history.html', {"all": past_reflections})

def contact(request):
  return render(request, 'base/contact.html', {})

def information(request):
  return render(request, 'base/information.html', {})