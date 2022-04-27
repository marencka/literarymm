from django.contrib import admin
from .models import Quote, Image, Reflection, PDPR, QuoteAdmin, ImageAdmin, PDPRAdmin
# Register your models here.
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(PDPR, PDPRAdmin)