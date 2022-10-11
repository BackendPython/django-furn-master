from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Blog)
class InfoTranslateOptions(TranslationOptions):
    fields = ('title', 'aboute',)

@register(Product)
class ProductTranslateOptions(TranslationOptions):
    fields = ('title',)
    
@register(Carousel)
class ProductTranslateOptions(TranslationOptions):
    fields = ('title', 'aboute')