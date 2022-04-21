from django.contrib import admin
from .models import Quote, Image, Reflection, PDPR, QuoteAdmin, ImageAdmin
# Register your models here.
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Reflection)
admin.site.register(PDPR)