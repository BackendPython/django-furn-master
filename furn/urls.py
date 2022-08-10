from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

app_name = 'furn'

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_redirect, name='logout-redirect'),
    path('logout-link', LogoutView.as_view(), name='logout-link'),
    path('<int:pk>/details/', arrivals_detail, name='arrival_detail'),
]
