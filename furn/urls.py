from django.urls import path
from . import  views

app_name = 'furn'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:pk>/details/', views.arrivals_detail, name='arrival_detail'),
]
