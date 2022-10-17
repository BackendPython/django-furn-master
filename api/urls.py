from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [
    path('carousel', carousel_api, name='carousel')
]