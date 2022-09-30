from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Blog)

class InfoTranslateOptions(TranslationOptions):
    fields = ('title', 'aboute',)