from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Product)

class InfoTranslateOptions(TranslationOptions):
    model = Product
    fields = ('title', )