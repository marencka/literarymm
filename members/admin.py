# Written by Jill O'Dell
from django.contrib import admin
from .models import Profile, ProfileAdmin
from  django.contrib.auth.models  import  Group

# Allows for the admin to see Profile Database in specified way
admin.site.register(Profile, ProfileAdmin)

# Removes unused Group section that was preinstalled on admin panel 
admin.site.unregister(Group)
