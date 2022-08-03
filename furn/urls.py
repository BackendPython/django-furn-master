from django.urls import path
from .views import *

app_name = 'furn'

urlpatterns = [
    path('', home, name="home"),
    path('signup', signup, name='signup'),
    path('<int:pk>/details/', arrivals_detail, name='arrival_detail',),
]
