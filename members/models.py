from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    wantPDQuotes = models.BooleanField(null=True)

    def __str__(self):
        return str(self.user.first_name + ' ' + self.user.last_name)

class ProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'wantPDQuotes']