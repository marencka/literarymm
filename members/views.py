from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def login_user(request):
  if request.method == "POST":
    username = request.POST.get('username', 'default_value') 
    password = request.POST.get('password', 'default_value') 
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('logged_in')

    else: 
      messages.success(request, ("There was an error logging in. Try again..."))
      return redirect('login')
  else:
    return render(request, 'login.html', {})


def register_user(request):
  if request.method == 'POST':
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    #check to see if username already exists
    if User.objects.filter(username=username).exists():
      #if it does, return error message and try again
      messages.success(request, ("Sorry, someone already has that username. Try again..."))
      return redirect('register')
    else:
      #creating a user object:
      user = User.objects.create_user(first_name=fname, last_name=lname, email= email, username=username, password=password)

      #save the user to the database
      user.save()

      #log the newly created user in and redirect
      login(request, user)
      return redirect('logged_in')

  else:
    return render(request, 'register.html')


def sign_up_start(request):
  return render(request, 'signup.html')

def returnHome(request):
  return redirect('index')