from django.urls import path
from .views import *

app_name = 'furn'

urlpatterns = [
    path('', home, name="home"),
    path('signup', Registration.as_view(), name='signup'),
    path('<int:pk>/details/', arrivals_detail, name='arrival_detail'),
]
