from django.urls import path
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_home, name='home'),
    path('buttons/', buttons, name='buttons'),
    path('cards/', cards, name='cards'),
    path('colors/', colors, name='colors'),
    path('border/', border, name='border'),
    path('other/', other, name='other'),
    path('animation/', animation, name='animation'),
    path('login/', dashboard_login, name='login'),
    path('password/', forgot_password, name='password'),
    path('register/', register, name='register'),
    path('charts/', charts, name='charts'),
    path('tables/', tables, name='tables'),
    path('404/', page_404, name='page_404'),
    path('blank/', blank, name='blank'),
]