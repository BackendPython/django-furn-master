from furn.translate import InfoTranslateOptions
from django.contrib import admin
from .models import *

admin.site.register(MyUser)
admin.site.register(Carousel)
admin.site.register(Arrival)
admin.site.register(Blog)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Contact)