from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

# This is the profile model which a user signs up with and gets their user information and whether or not they want 
# Parkinson quotes
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    wantPDQuotes = models.BooleanField(null=True)

    def __str__(self):
        return str(self.user.first_name + ' ' + self.user.last_name)

# Changes the way the admin sees profiles
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'wantPDQuotes']