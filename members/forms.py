
from django import forms
from django.contrib.auth.forms import UserCreationForm 

from members.models import Account

class RegisterUserForm(UserCreationForm):
  email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

  class Meta:
    model = Account 
    fields = ('email', 'username', 'password1', 'password2')