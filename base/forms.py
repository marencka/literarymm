from socket import fromshare
from django import forms 
from django.forms import ModelForm
from .models import Reflection, PDPR

# Create a reflection 
class ReflectionForm(ModelForm):
  class Meta:
    model = Reflection 
    fields = ('text',)
    exclude = ('user',)

class PDPRForm(ModelForm):
  class Meta:
    model = PDPR
    fields = ('q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15',)
    exclude = ('user',)
