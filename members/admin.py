from django.contrib import admin
from .models import Profile, ProfileAdmin
from  django.contrib.auth.models  import  Group

# Allows for the admin to see Profile

admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)
