from django.contrib import admin
from .models import Profile, ProfileAdmin
from  django.contrib.auth.models  import  Group

# Register your models here.

admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)
