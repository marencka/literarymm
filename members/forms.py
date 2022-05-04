# Written by Alexis Danz
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.forms import ModelForm
from .models import Profile

# This is the register user form which allows a user to sign up
class RegisterUserForm(UserCreationForm):
  email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

  class Meta:
    model = Profile 
    fields = ('email', 'username', 'password1', 'password2')
