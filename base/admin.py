from django.contrib import admin
from .models import Quote, Image, Reflection, PDPR, QuoteAdmin, ImageAdmin, PDPRAdmin
# /* Written by Alexis Danz */
# This allows for the admin/client to see the databases of Quotes, Imags, and PDPR's. 
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(PDPR, PDPRAdmin)