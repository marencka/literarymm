from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Quote, Image, Reflection, PDPR
from .forms import ReflectionForm, PDPRForm


# This is the base home view that a user sees when loading website
def home(request):
  return render(request, 'base/index.html', {})

# This is the user specific dashboard when they login
def dashboard(request):
  return render(request, 'base/dashboard.html', {})

# This loads the webpage for the meditation
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

# This loads the wepage for the progress disease report
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
      return redirect('dashboard')
  else:
    form = PDPRForm
  return render(request, 'base/pdpr.html', {'all': all, 'form': form})

# This loads the webpage for the past reflections of the specific requesting user
def history(request):
  past_reflections = Reflection.objects.order_by('-date').filter(user=request.user)
  return render(request, 'base/history.html', {"all": past_reflections})

# This loads the page for base information of literarymm
def information(request):
  return render(request, 'base/information.html', {})

# Loads the information for past PDPR's. 
def pdpr_history(request):
  # Five most recent entries 
  all = PDPR.objects.all().filter(user=request.user).count()
  if all >= 5:
    long_enough = True
    five = PDPR.objects.order_by('-date').filter(user=request.user)[0] 
    four = PDPR.objects.order_by('-date').filter(user=request.user)[1] 
    three = PDPR.objects.order_by('-date').filter(user=request.user)[2] 
    two = PDPR.objects.order_by('-date').filter(user=request.user)[3] 
    one = PDPR.objects.order_by('-date').filter(user=request.user)[4] 
    return render(request, 'base/pdpr_history.html', {'bool':long_enough, 'five': five, 'four':four, 'three':three, 'two':two, 'one':one})
  else: 
    long_enough = False
    all = PDPR.objects.all().order_by('-date').filter(user=request.user)
    return render(request, 'base/pdpr_history.html', {'bool':long_enough, 'all':all})