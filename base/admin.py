from django.contrib import admin
from .models import Quote, Image, Reflection, PDPR
# Register your models here.
admin.site.register(Quote)
admin.site.register(Image)
admin.site.register(Reflection)
admin.site.register(PDPR)