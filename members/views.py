from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm

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
    form = UserCreationForm(request.POST)
    if form.is_valid(): 
      form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('logged_in')
  else:
    form = UserCreationForm()
    print("I got here")
    return render(request, 'register.html/', {
      'form': form,
  })
