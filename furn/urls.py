from django.urls import path
from . import  views

app_name = 'furn'

urlpatterns = [
    path('', views.home, name="home")
]
