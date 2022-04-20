from socket import fromshare
from django import forms 
from django.forms import ModelForm
from .models import Reflection 

# Create a reflection 
class ReflectionForm(ModelForm):
  class Meta:
    model = Reflection 
    fields = ('text',)
    exclude = ('user',)